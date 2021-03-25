# coding:utf8
from django.http import JsonResponse
from common import redis_con
from common import get_common_data

# 连接数据库
r = redis_con.Redis()

users = r.hkeys("user")
# 登陆
def signin(request):
    username = request.GET['username']
    password = request.GET['password']
    if bytes(username, encoding='utf8') in users:
        if password == r.hget("user", username).decode():
            return JsonResponse({"rCode": 0, "msg": "login success"})
        else:
            return JsonResponse({"rCode": 1, "msg": "password error"})
    else:
        return JsonResponse({"rCode": 2, "msg": "username does not exist"})

# 注册
def register(request):
    username = request.GET['username']
    password = request.GET['password']
    if bytes(username, encoding='utf8') in users:
        return JsonResponse({"rCode": 1, "msg": "username had exist"})
    else:
        r.hset("user", username, password)
        # 为用户创建搜索面膜次数表
        mask_names = get_common_data.get_all_mask_name()
        for mask in mask_names:
            r.zadd("click_num_" + username, {mask: 0})

        return JsonResponse({"rCode": 0, "msg": "register success"})
