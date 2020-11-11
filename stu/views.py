from django.shortcuts import render,HttpResponse
import json

# 打开登录页面
def login(request):
    return render(request,"login.html")

# 判断登录是否成功
def islogin(request):
    u = "1804"
    p = "123456"
    # 获取页面传来的数据
    username = request.POST.get("username")
    password = request.POST.get("password")
    # code:-1,用户名不存在，0：密码正确，1，密码错误
    data = {"code":-1,"msg":"用户名不存在"}
    if u == username:
        if p == password:
            # 密码正确
            data["code"] = 0
            data["msg"] = "密码正确"
        else:
            # 密码错误
            data["code"] = 1
            data["msg"] = "密码错误"

    return HttpResponse(json.dumps(data))

# 打开主页面
def index(request):
    return render(request,"index.html")