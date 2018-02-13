#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from django.urls import re_path
from . import views

app_name = 'user'

urlpatterns = [

    # 登录 ==============================================================
    path('login/', views.login),       # 登录验证
    path('register/', views.register),  # 注册



    # path('home/', views.home),         # 后台管理
    # path('user_info/', views.user_info),  # 用户信息
    # path('user_group/', views.user_group),  # 用户管理
    # re_path('user_detail-(\d+)/', views.user_detail),  # 用户详情
    # re_path('user_delete-(\d+)/', views.user_delete),  # 用户删除
    # re_path('user_change-(\d+)/', views.user_change),  # 用户编辑
    # path('user_ajax/', views.user_ajax),    # 用户创建验证
    # path('user_page/', views.user_page),    # 分页加载
    # path('user_exit/', views.user_exit),    # 注销
    # path('caches/', views.suCaches),        # 缓存
    # path('form/', views.su_form),           # form验证
    # path('modeform/', views.su_mode_form),  # modeform验证
    # path('img_show/', views.img_show),  # modeform验证
    # # path('picture/', views.su_picture),     # 图像识别
    #
    # # CBV view 类 ===========================================================
    # path('CBV/', views.CBV.as_view()), # CBV类
    #
    # # 正则 ===================================================================
    # path('urlIndex/', views.suIndex),  # url主页
    # re_path('urlDetails-(\d)/', views.suDetail),                   # 正则匹配
    # re_path('urlArgs-(\d)-(\d)/', views.suGroup),                  # 元组正则
    # re_path('urlKwargs-(?P<nid>\d)-(?P<sid>\d)/', views.suGroup),  # 字典正则
    # # url(r'^urlDetails-(\d)/', views.suDetail), # url版本正则匹配
    #
    # # 路由命名 ===============================================================
    # path('nameURL/', views.urlName,name="urlName"),
    # re_path('nameURL/(\d+)/', views.urlName,name="urlName"),
    #
    # # 数据库 =================================================================






]


