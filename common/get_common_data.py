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
    for x in range(len(comments)):
        comments[x] = comments[x].decode()
    return comments

# 返回好评
def all_pos_com(mask_name):
    pos_comments = r.lrange(pinyin(mask_name).lower() + "_pos_comments", 0, -1)
    for x in range(len(pos_comments)):
        pos_comments[x] = pos_comments[x].decode()
    return pos_comments

# 返回差评
def all_nav_com(mask_name):
    nav_comments = r.lrange(pinyin(mask_name).lower() + "_nav_comments", 0, -1)
    for x in range(len(nav_comments)):
        nav_comments[x] = nav_comments[x].decode()
    return nav_comments

# 返回词频
def all_word_tfs(mask_name):
    words = r.hkeys(pinyin(mask_name).lower() + "_word_tf")
    tfs = r.hvals(pinyin(mask_name).lower() + "_word_tf")
    word_tf = []
    for x in range(len(words)):
        words[x].decode()
        tfs[x].decode()
        word_tf.append((words[x], tfs[x]))
    return word_tf

# 返回主题词
def all_topics(mask_name):
    topics = r.lrange(pinyin(mask_name).lower() + "_theme", 0, -1)
    for x in range(len(topics)):
        topics[x] = topics[x].decode()
    return topics

# 返回二元组
def all_bigrams(mask_name):
    pair_words = r.lrange(pinyin(mask_name).lower() + "_bigram", 0, 20)
    for x in range(len(pair_words)):
        pair_words[x] = pair_words[x].decode()
    return pair_words


# 返回词云
def all_wc(mask_name):
    wc_name = r.lrange(pinyin(mask_name).lower() + "wc", 0, -1)
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

