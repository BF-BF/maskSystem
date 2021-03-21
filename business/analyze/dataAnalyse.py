# coding:utf8
import nltk
import jieba
import jieba.analyse
from jieba import posseg
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from snownlp import SnowNLP
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from time import time

# 评论情感分析
def snownlp(all_comments):
    all_pos_comments = []
    all_nav_comments = []
    for com_list in all_comments:
        pos_comments = []
        nav_comments = []
        for com in com_list:
            if com != "":
                s = SnowNLP(com)
                if s.sentiments > 0.5:
                    pos_comments.append(com)
                else:
                    nav_comments.append(com)
        all_pos_comments.append(pos_comments)
        all_nav_comments.append(nav_comments)
    return all_pos_comments, all_nav_comments

# 停用词列表
def stopwords_list():
    stopwords = []
    with open('E:\\backend\\business\stopwords', 'r', encoding='utf8') as f:
        for line in f.readlines():
            stopwords.append(line.replace('\n', ''))
    return stopwords

# 分词并去除停用词
def tokenize(all_comments, stopwords):
    all_tokens = []
    for comments in all_comments:
        tokens = []
        for text in comments:
            words = jieba.lcut(text)
            for word in words:
                if word not in stopwords and word != " " and word != '\n':
                    tokens.append(word)
        all_tokens.append(tokens)
    return all_tokens

# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]
# 统计词频(词频排名前50的词语)
def tf(all_tokens):
    all_word_tf = []
    for tokens in all_tokens:
        single_word_tf = []
        fd = nltk.FreqDist(tokens)
        words = list(fd.keys())
        tfs = list(fd.values())
        for x in range(len(words)):
            word_tf = (words[x], tfs[x])
            single_word_tf.append(word_tf)
        single_word_tf.sort(key=takeSecond, reverse=True)
        all_word_tf.append(single_word_tf[:50])
    return all_word_tf

# 词性标注并提取形容词集
def adj_words(all_comments):
    all_adj_words = []
    for comment in all_comments:
        adj_words = []
        for com in comment:
            tag_words = list(posseg.cut(com.strip()))
            for words in tag_words:
                if words.flag == 'a' or words.flag == 'ad' or words.flag == 'an' \
                        or words.flag == 'ag' or words.flag == 'al':
                    adj_words.append(words.word)
        all_adj_words.append(adj_words)
    return all_adj_words

# 提取关键词及其权重
def keywords(all_comments, all_adj_words):
    all_keywords = []
    for comment in all_comments:
        str_com = ''
        for com in comment:
            str_com = str_com + com + '\n'
        # 单一所有评论
        keywords = jieba.analyse.extract_tags(str_com, topK=10, withWeight=True, allowPOS=())
        all_keywords.append(keywords)

    # # 形容词集
    # all_adj_keywords = []
    # for words in all_adj_words:
    #     str_adj_words = ''
    #     for word in words:
    #         str_adj_words = str_adj_words + word + '\n'
    #     adj_keywords = jieba.analyse.extract_tags(str_adj_words, topK=30, withWeight=True, allowPOS=())
    # all_adj_keywords.append(adj_keywords)

    return all_keywords

# 建立词性的bigrams
def bigrams(all_tokens, all_theme):
    all_topic_words = []
    all_word_pair = []
    for theme in all_theme:
        topic_word = []
        for word_text in theme:
            topic_word += word_text.split()
        all_topic_words.append(topic_word)

    for i in range(len(all_tokens)):
        pos_pairs = []
        for x in range(len(all_tokens[i])-1):
            if all_tokens[i][x] in all_topic_words[i]:
                pos1 = all_tokens[i][x]
                pos2 = all_tokens[i][x+1]
                word_pair = str(pos1) + str(pos2)
                pos_pairs.append(word_pair)
        all_word_pair.append(pos_pairs)
    return all_word_pair

# 词云
def make_word_cloud(all_word_pair):
    w = WordCloud(background_color="white", font_path="simsun.ttc", max_font_size=250, width=500, height=500)
    for x in range(len(all_word_pair)):
        word_text = ''
        for word in all_word_pair[x]:
            word_text = word_text + word + ' '
        w.generate(word_text)
        w.to_file('wordCloud' + str(x) + '.png')

# def make_bar( param, y):
#     # 显示中文字符
#     plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
#     # 生成画布
#     plt.figure(figsize=(20, 8), dpi=80)
#
#     x = range(len(param))
#     plt.bar(x, y, width=0.5, color=['b', 'r', 'g', 'y', 'c', 'm', 'y', 'k', 'c', 'g', 'g'])
#     plt.xticks(x, param)
#
#     plt.show()

# 打开文件并进行预处理
def pos_tag(all_comments, stopwords):
    all_na_tokens = []
    for comment in all_comments:
        na_token = []
        for com in comment:
            tokens = list(posseg.lcut(com))
            pos_tokens = ''
            for word, tag in tokens:
                if word not in stopwords:
                    if tag == 'n' or tag == 'a':
                        pos_tokens = pos_tokens + word + ' '
            if len(pos_tokens) > 0:
                na_token.append(pos_tokens)
        all_na_tokens.append(na_token)
    return all_na_tokens

def model_train(all_na_tokens):
    # 使用sklearn中的tf,TF-IDF向量化方法对该数据集中1000个句子建立文档词向量矩阵。
    all_theme = []
    for na_tokens in all_na_tokens:
        t0 = time()
        n_features = 1000
        myvectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=n_features,)
        vectors = myvectorizer.fit_transform(na_tokens)
        matrixs = vectors.toarray()
        # print(matrixs)
        data = np.array(matrixs)
        # print(data)
        print("向量化所花的时间为：%0.3fs." % (time() - t0))

        # 使用LDA模型对文本进行主题建模
        print("Fitting LDA models...")
        n_components = 10
        lda = LatentDirichletAllocation(n_components=n_components, max_iter=5,
                                            learning_method='online',
                                            learning_offset=50.,
                                            random_state=0)
        t0 = time()
        lda.fit(data)
        print("LDA建模时间为： %0.3fs." % (time() - t0))
        # return myvectorizer, lda

# def result(self, na_tokens):
        # 打印所抽取出的主题的主题词
        print("\nTopics in LDA model:")
        theme = []
        # myvectorizer, lda = self.model_train(na_tokens)
        feature_names = myvectorizer.get_feature_names()
        n_top_words = 20
        for topic_idx, topic in enumerate(lda.components_):
            message = ""
            message += " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]])
            theme.append(message)
        all_theme.append(theme)
    return all_theme
