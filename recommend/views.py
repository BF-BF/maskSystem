from django.http import JsonResponse
from recommend.business import get_train_data
from common import get_common_data
import numpy as np

# can_mask_name = ['sk2', 'hanshu', 'mg', 'panshi', 'wanzixx', 'xiaobding', 'youtlan', 'bolaiya', 'farmacy', 'niuxzmi']

# 商品推荐
def recommend(request):
    # 获取备选面膜的url
    com_urls = "https://detail.tmall.com/item.htm?"
    name_urls = get_common_data.all_urls()
    recommend_name_urls = dict()

    username = request.GET["username"]
    # username = 'sukki'
    if len(get_train_data.user_saw_mask(username)):
        # 用户画像
        user_profile = get_train_data.createUserProfile(username)
        # print(user_profile)
        # 备选面膜画像
        mask_01_dict = get_common_data.all_can_mask_01()
        can_mask_name = list(mask_01_dict.keys())
        all_can_mask = list(mask_01_dict.values())
        # print(can_mask_name)
        # print(all_can_mask)
        all_can_mask_profile = []
        for can_mask in all_can_mask:
            all_can_mask_profile.append(can_mask)
        all_can_mask_profile = np.array(all_can_mask_profile)
        # print(all_can_mask_profile)
        # all_can_mask_profile = get_train_data.createMaskProfile()

        # 计算备选面膜画像和用户画像的余弦相似度
        can_cos = []
        for x in range(len(can_mask_name)):
            can_cos.append(get_train_data.cos_sim(user_profile, all_can_mask_profile[x]))

        mask_cos = dict()
        for x in range(len(can_mask_name)):
            mask_cos[can_mask_name[x]] = can_cos[x]
        # print(mask_cos)

        score = list(mask_cos.values())
        score.sort(reverse=True)
        # print(score[:3])
        # print(list(mask_cos.keys()))

        # 推荐相似度排名前三的面膜给用户
        recommend_mask_name = []
        for value in list(mask_cos.values()):
            if value in score[:3]:
                recommend_mask_name.append(list(mask_cos.keys())[list(mask_cos.values()).index(value)])
        # print(recommend_mask_name)

        for mask in recommend_mask_name:
            recommend_name_urls[mask] = com_urls + name_urls[mask]
        # print(recommend_name_urls)

        return JsonResponse(recommend_name_urls)
    else:
        default_recommend = dict()
        default_recommend['sk2'] = com_urls + name_urls['sk2']
        default_recommend['bolaiya'] = com_urls + name_urls['bolaiya']
        default_recommend['hanshu'] = com_urls + name_urls['hanshu']

        # print(default_recommend)
        return JsonResponse(default_recommend)

# recommend()
