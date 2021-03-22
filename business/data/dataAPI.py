from common import redis_con
from business.data import getAllData
from common import get_common_data
from recommend.business import get_train_data

# 连接数据库
r = redis_con.Redis()

# 用户
def insert_user():
    # r.hset("user", "sukki", "123456")
    r.hset("user", "leeyona", "12345678")

# 面膜
goods_name = ['yunifang', 'yiyezi', 'zirantang', 'queling', 'dijiating', 'olaiya', 'meidihuier', 'chunyu', 'fuerjia', 'jm',
              'keyanshi', 'gelai', 'fuleishi', 'swisse', 'lanzhi']
# 备选面膜
can_mask_name = ['sk2', 'hanshu', 'mg', 'panshi', 'wanzixx', 'xiaobding', 'youtlan', 'bolaiya', 'farmacy', 'niuxzmi']

# 商品所有信息
all_data = getAllData.getAll()
# 商品评论
def insert_all_coms():
    for x in range(len(all_data.get_all_comments())):
        for com in all_data.get_all_comments()[x]:
            r.rpush(goods_name[x]+"_comments", com)

# 商品好评
pos_com, nav_com = all_data.get_all_pos_nav()
def insert_pos_com():
    for x in range(len(pos_com)):
        for com in pos_com[x]:
            r.rpush(goods_name[x]+"_pos_comments", com)

# 商品差评
def insert_nav_com():
    for x in range(len(nav_com)):
        for com in nav_com[x]:
            r.rpush(goods_name[x]+"_nav_comments", com)

# 商品词频入库
def insert_words_tf():
    for x in range(len(all_data.get_all_tfs())):
        for tf in all_data.get_all_tfs()[x]:
            r.hset(goods_name[x]+"_word_tf", tf[0], tf[1])

# 商品形容词
def insert_adj_word():
    for x in range(len(all_data.get_all_adj_words())):
        for word in all_data.get_all_adj_words()[x]:
            r.rpush(goods_name[x]+"_adj_words", word)

# 商品关键词
def insert_keyword():
    for x in range(len(all_data.get_all_keywords())):
        for word in all_data.get_all_keywords()[x]:
            r.hset(goods_name[x]+"_keywords", word[0], word[1])

# 商品主题
def insert_theme():
    for x in range(len(all_data.get_all_topics())):
        for theme in all_data.get_all_topics()[x]:
            r.rpush(goods_name[x]+"_theme", theme)

# 商品二元组
def insert_bigram():
    for x in range(len(all_data.get_all_bigram())):
        for pairs in all_data.get_all_bigram()[x]:
            r.rpush(goods_name[x] + "_bigram", pairs)

# 词云图片
def insert_wc_name():
    all_data.get_all_wc()
    for x in range(len(goods_name)):
        r.rpush(goods_name[x] + "_wc", goods_name[x] + "wordCloud" + str(x) + ".png")

# 备选面膜集天猫商城url
def insert_urls():
    can_mask_name = ['sk2', 'hanshu', 'mg', 'panshi', 'wanzixx', 'xiaobding', 'youtlan', 'bolaiya', 'farmacy', 'niuxzmi']
    all_urls = all_data.get_all_urls()
    for x in range(len(can_mask_name)):
        r.hset("mask_urls", can_mask_name[x], all_urls[x])

# 用户搜索面膜次数
def insert_click_num():
    username = get_common_data.all_username()
    mask_names = all_data.get_all_mask_name()
    for name in username:
        for mask in mask_names:
            r.zadd("click_num_" + name, {mask: 0})

# 备选面膜主题词01列表
def insert_can_mask():
    all_can_topic_01 = get_train_data.createMaskProfile()
    for x in range(len(all_can_topic_01)):
        r.hset("can_mask_01", can_mask_name[x], str(all_can_topic_01[x]))