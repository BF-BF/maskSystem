import pypinyin
from common import redis_con

# 连接数据库
r = redis_con.Redis()

# 所有面膜名称
def get_all_mask_name():
    all_mask_name = ['yunifang', 'yiyezi', 'zirantang', 'queling', 'dijiating', 'olaiya', 'meidihuier', 'chunyu',
                     'fuerjia', 'jm', 'keyanshi', 'gelai', 'fuleishi', 'swisse', 'lanzhi']
    return all_mask_name

# 文字转拼音
def pinyin(word):
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
    return s

# 返回面膜所有评论
def all_com(mask_name):
    comments = r.lrange(pinyin(mask_name).lower() + "_comments", 0, -1)
    com = []
    for x in range(len(comments)):
        comments[x] = comments[x].decode()
        com.append(comments[x].split(',\n')[0].replace('"', ''))
    return com

# 返回好评
def all_pos_com(mask_name):
    pos_comments = r.lrange(pinyin(mask_name).lower() + "_pos_comments", 0, -1)
    pos_com = []
    for x in range(len(pos_comments)):
        pos_comments[x] = pos_comments[x].decode()
        pos_com.append(pos_comments[x].split(',\n')[0].replace('"', ''))
    return pos_com

# 返回差评
def all_nav_com(mask_name):
    nav_comments = r.lrange(pinyin(mask_name).lower() + "_nav_comments", 0, -1)
    nav_com = []
    for x in range(len(nav_comments)):
        nav_comments[x] = nav_comments[x].decode()
        nav_com.append(nav_comments[x].split(',\n')[0].replace('"', ''))
    return nav_com

# 返回词频
def all_word_tfs(mask_name):
    words = r.hkeys(pinyin(mask_name).lower() + "_word_tf")
    tfs = r.hvals(pinyin(mask_name).lower() + "_word_tf")
    word_tf = []
    for x in range(len(words)):
        words[x] = words[x].decode()
        tfs[x] = tfs[x].decode()
        word_tf.append((words[x], tfs[x]))
    return word_tf

# 返回主题词
def all_topics(mask_name):
    topics = r.lrange(pinyin(mask_name).lower() + "_theme", 0, -1)
    all_topics = []
    for x in range(len(topics)):
        topics[x] = topics[x].decode()
        all_topics += topics[x].split()
    return all_topics

# 返回二元组
def all_bigrams(mask_name):
    pair_words = r.lrange(pinyin(mask_name).lower() + "_bigram", 0, 20)
    for x in range(len(pair_words)):
        pair_words[x] = pair_words[x].decode()
    return pair_words


# 返回词云
def all_wc(mask_name):
    wc_name = r.lrange(pinyin(mask_name).lower() + "_wc", 0, -1)
    for x in range(len(wc_name)):
        wc_name[x] = wc_name[x].decode()
    return wc_name

# 返回形容词
def all_adj_words(mask_name):
    adj_words = r.lrange(pinyin(mask_name).lower() + "_adj_words", 0, -1)
    for x in range(len(adj_words)):
        adj_words[x] = adj_words[x].decode()
    return adj_words

# 返回用户名
def all_username():
    username = r.hkeys("user")
    for x in range(len(username)):
        username[x] = username[x].decode()
    return username

# 返回备选面膜urls
def all_urls():
    can_mask_names = r.hkeys("mask_urls")
    mask_urls = r.hvals("mask_urls")
    name_urls = dict()
    for x in range(len(can_mask_names)):
        can_mask_names[x] = can_mask_names[x].decode()
        mask_urls[x] = mask_urls[x].decode()
        name_urls[can_mask_names[x]] = mask_urls[x]
    return name_urls

# 返回备选面膜01列表
def all_can_mask_01():
    can_mask_names = r.hkeys("can_mask_01")
    mask_01 = r.hvals("can_mask_01")
    mask_01_dict = dict()
    for x in range(len(can_mask_names)):
        can_mask_names[x] = can_mask_names[x].decode()
        mask_01[x] = mask_01[x].decode()
        list_mask_01 = list(mask_01[x])
        final_mask_01 = []
        for text in list_mask_01:
            if text == '1' or text == '0':
                final_mask_01.append(int(text))
        mask_01_dict[can_mask_names[x]] = final_mask_01
    return mask_01_dict

# print(all_can_mask_01())