"""BJTU_CMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import view
urlpatterns = [
    url(r'^cms/', view.home),
    url(r'^categroydetail$', view.categroydetail),
    url(r'^getItemById$', view.getItemById),
    url(r'^gotoManagerPage/$', view.gotoManagerPage),
    url(r'^getUser$', view.getUser),
    url(r'toUserGride$', view.toUserGride),
    url(r'^getItem$', view.getItem),
    url(r'toItemGride', view.toItemGride),
    url(r'^getCategory', view.getCategory),
    url(r'toCategoryGride', view.toCategoryGride),
    url(r'getItemByIdPage', view.getItemByIdPage),
    url(r'saveItem', view.saveItem),
    url(r'toEditItem/', view.toEditItem),
    url(r'category_list', view.category_list),
    url(r'deleteItemBykey', view.deleteItemBykey),
    url(r'toEditCategory', view.toEditCategory),
    url(r'saveCategory', view.saveCategory),
    url(r'deleteCategoryBykey', view.deleteCategoryBykey),
    url(r'login', view.login),
    url(r'saveUser', view.saveUser),
    url(r'deleteUser', view.deleteUser),
    url('editUserPage', view.editUserPage),
    url('getUserbyName', view.getUserbyName),
]
