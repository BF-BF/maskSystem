from django.http import JsonResponse
from recommend.business import get_train_data

can_mask_name = ['sk2', 'hanshu', 'mg', 'panshi', 'wanzixx', 'xiaobding', 'youtlan', 'bolaiya', 'farmacy', 'niuxzmi']

# 商品推荐
def recommend():
    # username = request.GET["username"]
    user_profile = get_train_data.createUserProfile("sukki")
    all_can_mask_profile = get_train_data.createMaskProfile()

    can_cos = []
    for x in range(len(get_train_data.get_all_topic())):
        can_cos.append(get_train_data.cos_sim(user_profile, all_can_mask_profile[x]))

    mask_cos = dict()
    for x in range(len(can_mask_name)):
        mask_cos[can_cos] = can_mask_name[x]

    score = mask_cos.keys()
    score.sort(reversed=True)
    recommend_mask_name = []
    for key in mask_cos.keys():
        if key in score[:3]:
            recommend_mask_name.append(mask_cos[key])
    print(recommend_mask_name)

    # return JsonResponse(recommend_mask_name)

recommend()