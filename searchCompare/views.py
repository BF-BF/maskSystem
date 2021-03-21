from django.http import JsonResponse
import pypinyin
from common import redis_con
from common import get_common_data

# 连接数据库
r = redis_con.Redis()

mask_names = ['yunifang', 'yiyezi', 'zirantang', 'queling', 'dijiating', 'olaiya', 'meidihuier', 'chunyu', 'fuerjia', 'jm',
              'keyanshi', 'gelai', 'fuleishi', 'swisse', 'lanzhi']
# -------面膜搜索-------
# 文字转拼音
def pinyin(word):
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
    return s

def mask_search(request):
    mask_name = request.GET["maskName"]
    if pinyin(mask_name).lower() not in mask_names:
        return JsonResponse({'rCode': 1, 'msg': '搜索结果为空'})
    else:
        maskResultDict = dict()
        # 返回20条好评
        pos_comments = get_common_data.all_pos_com(mask_name)[0, 20]
        maskResultDict["PosComments"] = pos_comments

        # 返回20条差评
        nav_comments = get_common_data.all_nav_com(mask_name)
        maskResultDict["NavComments"] = nav_comments

        # 返回词频
        word_tf = get_common_data.all_word_tfs(mask_name)
        maskResultDict["WordTfs"] = word_tf

        # 返回20个二元组
        pair_words = get_common_data.all_bigrams(mask_name)[0, 20]
        maskResultDict["PairWords"] = pair_words

        # 返回词云
        wc_name = get_common_data.all_wc(mask_name)
        maskResultDict["WCPictName"] = wc_name

        return JsonResponse(maskResultDict)

# -------关键词搜索--------
def keywords_search(request):
    search_keyword = request.GET["searchKeyword"]
    keywordResultDict = dict()

    all_kw_com_result = []
    result_mask = []
    for x in range(len(mask_names)):
        comments = get_common_data.all_com(mask_names)
        kw_com_result = []
        for com in comments:
            if search_keyword in com:
                kw_com_result.append(com)
        if kw_com_result:
            all_kw_com_result.append(kw_com_result)
            result_mask.append(mask_names[x])

    if all_kw_com_result:
        keywordResultDict["KeywordResult"] = all_kw_com_result
        return JsonResponse(keywordResultDict)
    else:
        return JsonResponse({'rCode': 1, 'msg': '搜索结果为空'})

# 商品比较
def compare(request):
    mask1 = request.GET["maskName1"]
    mask2 = request.GET["maskName2"]
    if pinyin(mask1).lower() not in mask_names or pinyin(mask2).lower() not in mask_names:
        return JsonResponse({'rCode': 1, 'msg': '比较结果为空'})
    else:
        firstMaskDict = dict()
        secondMaskDict = dict()
        # 返回相同主题词所在的评论
        mask_topic1 = get_common_data.all_topics(mask1)
        mask_topic2 = get_common_data.all_topics(mask2)
        all_mask_topic1 = []
        all_mask_topic2 = []
        for x in range(len(mask_topic1)):
            all_mask_topic1 += mask_topic1[x].split()
            all_mask_topic2 += mask_topic2[x].split()
        same_topics = []
        for topic in all_mask_topic1:
            if topic in all_mask_topic2:
                same_topics.append(topic)
        comment1 = get_common_data.all_com(mask1)
        comment2 = get_common_data.all_com(mask2)
        same_topic_coms1 = []
        same_topic_coms2 = []
        for topic in same_topics:
            for com in comment1:
                if topic in com:
                    same_topic_coms1.append(com)
            for com in comment2:
                if topic in com:
                    same_topic_coms2.append(com)

        firstMaskDict["SameTopicComment"] = same_topic_coms1
        secondMaskDict["SameTopicComment"] = same_topic_coms2

        # 返回相同形容词及其词频
        adj_words1 = get_common_data.all_adj_words(mask1)
        adj_words2 = get_common_data.all_adj_words(mask2)
        same_adj_words1 = []
        same_adj_words2 = []
        for word in adj_words1:
            if word in adj_words2:
                same_adj_words1.append((word, adj_words1.count(word)))
                same_adj_words2.append((word, adj_words2.count(word)))

        firstMaskDict["SameAdjWordTF"] = same_adj_words1
        secondMaskDict["SameAdjWordTF"] = same_adj_words2

        return JsonResponse(firstMaskDict), JsonResponse(secondMaskDict)





