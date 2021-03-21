from django.http import JsonResponse
from common import redis_con

# 连接数据库
r = redis_con.Redis()

users = r.hkeys("user")
# 登陆
def signin(request):
    username = request.GET['username']
    password = request.GET['password']
    if bytes(username, encoding='utf8') in users:
        if password == r.hget("user", username):
            return JsonResponse({"rCode": 0, "msg": "登录成功"})
        else:
            return JsonResponse({"rCode": 1, "msg": "密码不正确"})
    else:
        return JsonResponse({"rCode": 2, "msg": "用户不存在"})

# 注册
def register(request):
    username = request.POST['username']
    password = request.POST['password']
    if bytes(username, encoding='utf8') in users:
        return JsonResponse({"rCode": 1, "msg": "用户名已存在"})
    else:
        r.hset("user", username, password)
        return JsonResponse({"rCode": 0, "msg": "注册成功"})
