from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from user import models # 引入模块数据库类
import json #返回json


# 注册 - 检测用户 =================================================================
def register_verify(request):

    verify_json = {"verify": True, "error": None, "data": None}

    if request.method == "POST":

        user_name = request.POST.get("user_name", None)
        # su_name = models.userInfo.objects.filter(user_name=user_name).first()
        if user_name:

            verify_json["verify"] = False
            verify_json["error"] = "账号已存在!"
        else:

            verify_json["verify"] = True
            verify_json["error"] = "可以进行注册!"
        return HttpResponse(json.dumps(verify_json))


def register(request):

    if request.method == "POST":
        # 获取按钮
        submit = request.POST.get("submit")

        if submit == "提交":
            city = request.POST.getlist("city", None)
            gender = request.POST.get("gender", None)
            hobby = request.POST.getlist("hobby", None)

        elif submit == "图片提交":
            # 获取图片
            img = request.FILES.get("img_upload")
            print(img)

            # 设置保存路径
            import  os
            img_path = os.path.join("PICTURE",img.name)
            # 读取图片
            file = open(img_path,mode="wb")
            for i in img.chunks():
                file.write(i)
            file.close()

    return HttpResponse("哈哈哈")

# def _set_token(self, request, response):
#     if settings.CSRF_USE_SESSIONS:
#         request.session[CSRF_SESSION_KEY] = request.META[‘CSRF_COOKIE‘]
#         else:
#         response.set_cookie(
#             settings.CSRF_COOKIE_NAME,
#             request.META[‘CSRF_COOKIE‘],
#         max_age = settings.CSRF_COOKIE_AGE,
#                   domain = settings.CSRF_COOKIE_DOMAIN,
#                            path = settings.CSRF_COOKIE_PATH,
#                                   secure = settings.CSRF_COOKIE_SECURE,
#                                            httponly = settings.CSRF_COOKIE_HTTPONLY,
#         )
#         # Set the Vary header since content varies with the CSRF cookie.
#         patch_vary_headers(response, (‘Cookie‘, ))

def login(request):
    # if not getattr(request, "csrf_cookie_needs_reset", False):
    #     if getattr(response, "csrf_cookie_set", False):
    #         return response
    #
    # if not request.META.get("CSRF_COOKIE_USED", False):
    #     return response
    #
    # # Set the CSRF cookie even if it‘s already set, so we renew
    # # the expiry timer.
    # self._set_token(request)
    # response.csrf_cookie_set = True
    # return HttpResponse("哈哈哈")

    return HttpResponse(request.META['CSRF_COOKIE'])
    # return HttpResponse(request.session.CSRF_SESSION_KEY)