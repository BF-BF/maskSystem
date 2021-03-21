from common import get_common_data
import numpy as np
from business.data import getAllData
from business.analyze import dataAnalyse
from common import redis_con

r = redis_con.Redis()

# 建立用户画像：用户搜索过的面膜所对应的主题词的次数
def createUserProfile(username):
    # user_saw_mask: [("yiyezi", 8),("yunifang", 6),...]
    user_saw_masks = []
    mask_name = get_common_data.get_all_mask_name()
    for mask in mask_name:
        if r.zscore("click_num_"+username, mask):
            user_saw_masks.append((mask, r.zscore("click_num_"+username, mask)))

    all_topics = []
    for mask in mask_name:
        all_topics += get_common_data.all_topics(mask)
    # all_topics: ["补水", "服帖", "保湿", ...]
    all_topics = list(set(all_topics))

    # all_topic_score: [[8, 0, 8, ...],[2, 2, ...],[], ...]
    all_topic_score = []
    for x in range(len(user_saw_masks)):
        topic_score = []
        for j in range(len(all_topics)):
            if all_topics[j] in get_common_data.all_topics(user_saw_masks[x][0]):
                topic_score.append(user_saw_masks[x][1])
            else:
                topic_score.append(0)
        all_topic_score.append(topic_score)

    score_array = np.array(all_topic_score)
    topic_score_sum = np.sum(score_array, axis=0)

    average_score = []
    for score in topic_score_sum:
        average_score.append(score/len(user_saw_masks))

    aver_score_array = np.array(average_score)

    return aver_score_array

def get_all_can_mask_com():
    filename = ['E:\\backend\\recommend\\data\\comments\\sk2',
                'E:\\backend\\recommend\\data\\comments\\hanshu',
                'E:\\backend\\recommend\\data\\comments\\mg',
                'E:\\backend\\recommend\\data\\comments\\pangshi',
                'E:\\backend\\recommend\\data\\comments\\wanzixx',
                'E:\\backend\\recommend\\data\\comments\\xiaobding',
                'E:\\backend\\recommend\\data\\comments\\youtlan',
                'E:\\backend\\recommend\\data\\comments\\bolaiya',
                'E:\\backend\\recommend\\data\\comments\\farmacy',
                'E:\\backend\\recommend\\data\\comments\\niuxzmi',
                ]
    all_commments = []
    for x in range(len(filename)):
        with open(filename[x], 'r', encoding='utf8') as f:
            comments = f.readlines()
        all_commments.append(comments)
    return all_commments

def get_candidate_mask_topic():
    all_data = getAllData.getAll()
    stopwords = all_data.get_stopwords()

    all_na_tokens = dataAnalyse.pos_tag(get_all_can_mask_com(), stopwords)
    all_candidate_topic = dataAnalyse.model_train(all_na_tokens)

    all_mask_candidate_topic = []
    for topic in all_candidate_topic:
        split_topic = []
        for text in topic:
            split_topic += text.split()
        all_mask_candidate_topic.append(split_topic)

    return all_mask_candidate_topic

def get_all_topic():
    mask_names = get_common_data.get_all_mask_name()

    all_topics = []
    for mask in mask_names:
        all_topics += get_common_data.all_topics(mask)
    all_topics = list(set(all_topics))
    return all_topics

def createMaskProfile():
    all_topics = get_all_topic()
    all_mask_candidate_topic = get_candidate_mask_topic()

    all_can_topic_01 = []
    for can_topic in all_mask_candidate_topic:
        can_topic_01 = []
        for x in range(len(can_topic)):
            if can_topic[x] in all_topics:
                can_topic_01[x] = 1
            else:
                can_topic_01 = 0
        all_can_topic_01.append(can_topic_01)
    all_can_topic_01 = np.array(all_can_topic_01)

    return all_can_topic_01

def cos_sim(user, can_topic_01):
    user_norm = np.linalg.norm(user)
    can_topic_01_norm = np.linalg.norm(can_topic_01)
    if (user_norm * can_topic_01_norm):
        cos = np.dot(user, can_topic_01)/(user_norm * can_topic_01_norm)
    else:
        cos = 0.0
    return cos








