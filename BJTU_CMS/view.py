import time,datetime,json,uuid,requests
from sqlalchemy import and_,extract
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.core import serializers
import BJTU_CMS.models as models
from BJTU_CMS.orm import sqlConn
localtime = time.localtime(time.time())

'''
栏目列表
'''
def category_list(request):
    LIST = models.sqlConn.getqueryAll(models.Category)
    jsonList= ','.join([str(x) for x in LIST])
    return HttpResponse('['+jsonList+']')
'''
主页跳转
'''
def home(request):
    LIST = models.sqlConn.getqueryAll(models.Category)
    #user=request.session.get('cms_user')
    return render(request, 'home.html', {'categoryList': LIST})

'''
获取item列表
'''
def categroydetail(request):
    cid = request.GET.get("cid")
    curPage = int(request.GET.get("curPage"))#当前页
    pageSize = int(request.GET.get("pageSize"))#每页条数
    #总条数
    totalSize=sqlConn.executeFetchall("select count(*) from cms_item WHERE category_id='{}'".format(cid))[0][0]
    itemList=sqlConn.Session_class().query(models.Item).filter(models.Item.category_id == cid).limit(pageSize).offset((curPage-1)*pageSize)
    totalPageSize=int((totalSize+pageSize-1)/pageSize) #总页数
    itemjoin= ','.join([str(x) for x in itemList])
    jsonstr={'data':'['+itemjoin+']','totalSize':totalSize,'curPage':curPage,'totalPageSize':totalPageSize}
    return HttpResponse(json.dumps(jsonstr))
'''
item详情
'''
def getItemById(request):
    id = request.POST.get("id")
    item=sqlConn.getqueryById(models.Item,id)
    return HttpResponse(item )
'''
跳转管理页面
'''
def gotoManagerPage(request):
    #user=request.session.get('cms_user','')
    return render(request, 'manager/manager.html')
'''
跳转到用户列表
'''
def toUserGride(request):
    return render(request, 'manager/userGrid.html')
'''
获取用户列表
'''
def getUser(request):
    userList=sqlConn.getqueryAll(models.User)
    userjoin = ','.join([str(x) for x in userList])
    return HttpResponse('['+userjoin+']')
'''
跳转到信息列表
'''
def toItemGride(request):
    return render(request, 'manager/itemList.html')
'''
获取信息列表
'''
def getItem(request):
    curPage = int(request.GET.get("curPage"))  # 当前页
    pageSize = int(request.GET.get("pageSize"))  # 每页条数
    title=request.GET.get("title")
    ctime=request.GET.get("ctime")
    category_id=request.GET.get("category_id")
    param={}
    if title!=None:
        where="where title='{}'".format(title)
        param={'title':title}
    elif ctime:
        where = 'WHERE DATE_FORMAT(c_time,\'%Y-%m-%d\')=\'{}\''.format(ctime)
    elif category_id:
        where = 'where category_id=\'{}\''.format(category_id)
        param = {'category_id':category_id}
    else:
        where=""

    # 总条数
    totalSize = sqlConn.executeFetchall("select count(*) from cms_item "+where)[0][0]
    totalPageSize = int((totalSize + pageSize - 1) / pageSize)  # 总页数
    if ctime:
        dtime=datetime.datetime.strptime(ctime,'%Y-%m-%d')
        itemList = sqlConn.Session_class().query(models.Item).filter(
            extract('year',models.Item.ctime)==dtime.year,
            extract('month', models.Item.ctime) == dtime.month,
            extract('day', models.Item.ctime) == dtime.day,
        ).limit(pageSize).offset( (curPage - 1) * pageSize)
    else:
        itemList = sqlConn.getObjBywhere(models.Item,param).limit(pageSize).offset( (curPage - 1) * pageSize)
    itemjoin ='['+ ','.join([str(x) for x in itemList])+']'
    jsonstr = {'data': itemjoin , 'totalSize': totalSize, 'curPage': curPage, 'totalPageSize': totalPageSize}
    return HttpResponse(json.dumps(jsonstr))

'''
跳转到类别列表
'''
def toCategoryGride(request):
    return render(request, 'manager/categoryList.html')
'''
获取类别列表
'''
def getCategory(request):
    categoryList=sqlConn.getqueryAll(models.Category)
    cjoin = ','.join([str(x) for x in categoryList])
    return HttpResponse('['+cjoin+']')
'''
文章详情
'''
def getItemByIdPage(request):
    id = request.GET.get("id")
    item=sqlConn.getqueryById(models.Item,id)[0]
    return render(request, 'itemDtail.html',{'item':item})
'''
文章编辑页
'''
def toEditItem(request):
    id=request.GET.get('id')
    item=None
    if(id!=None):
        item = sqlConn.getqueryById(models.Item, id)[0]
    return render(request, 'manager/editItem.html',{'item':item})
'''
文章保存
'''
def saveItem(request):
    if request.POST.get('id')=='' or request.POST.get('id')==None:
        item=models.Item(id=uuid.uuid1().__str__().replace('-',''),
                         title=request.POST.get('title'),
                         content=request.POST.get('content'),
                         category_id=request.POST.get('category_id'),
                         status=request.POST.get('status'),
                         ctime=localtime)
        sqlConn.save(item)
        return HttpResponse(json.dumps({'status':'OK','msg':'保存成功'}))
    else:
        updateItem(request)
        return HttpResponse(json.dumps({'status':'OK','msg':'更新成功'}))
'''
更新ITEM
'''
def updateItem(request):
    sqlConn.updateById(models.Item,request.POST.get('id'),
                       { 'title' : request.POST.get('title'),
                         'content' : request.POST.get('content'),
                         'category_id' : request.POST.get('category_id'),
                         'status' : request.POST.get('status'),
                         'utime' : localtime})
'''
删除item
'''
def deleteItemBykey(request):
    sqlConn.delete(models.Item,request.GET.get('id'))
    return HttpResponse(json.dumps({'status': 'OK', 'msg': '删除成功'}))
'''
跳转栏目编辑页
'''
def toEditCategory(request):
    id = request.GET.get('id')
    category = None
    if (id != None):
        category = sqlConn.getqueryById(models.Category, id)[0]
    return render(request, 'manager/editCategroy.html', {'category': category})
'''
保存栏目
'''
def saveCategory(request):
    id=request.POST.get('id')
    if request.POST.get('id')=='':
        LIST = models.sqlConn.getqueryAll(models.Category)
        Category=models.Category(id=str(LIST.__len__()+1),
                             type=request.POST.get('type'),
                             type_name=request.POST.get('type_name'),
                             ctime=localtime)
        sqlConn.save(Category)
        return HttpResponse(json.dumps({'status':'OK','msg':'保存成功'}))
    else:
        updateCategory(request)
        return HttpResponse(json.dumps({'status':'OK','msg':'更新成功'}))
'''
更新栏目
'''
def updateCategory(request):
    sqlConn.updateById(models.Category,request.POST.get('id'),
                       { 'type' : request.POST.get('type'),
                         'type_name' : request.POST.get('type_name'),
                         })
'''
删除栏目
'''
def deleteCategoryBykey(request):
    sqlConn.delete(models.Category,request.GET.get('id'))
    return HttpResponse(json.dumps({'status': 'OK', 'msg': '删除成功'}))
'''
登录
'''
def login(request):
    name=request.POST.get('name')
    pwd=request.POST.get('pwd')
    param={'name':name,'pwd':pwd}
    user=sqlConn.getObjBywhere(models.User,param).scalar()
    if user!=None:
        response=HttpResponse(json.dumps({'status': 'OK', 'msg': '登录成功', 'data': user.name}))
        #response.set_cookie('user', user.name)
        return response
    else:
        return HttpResponse(json.dumps({'status': 'error', 'msg': '登录失败'}))
'''
保存用户
'''
def saveUser(request):

    uname=request.POST.get('name')
    user=None
    if uname!=None:
       user=sqlConn.getObjBywhere(models.User,{'name':uname}).scalar()
    if user==None:
        user=models.User(id=uuid.uuid1().__str__().replace('-',''),
                         name=uname,
                         pwd=request.POST.get('pwd'),
                         role=request.POST.get('role'),
                         ctime=localtime)
        sqlConn.save(user)
        return HttpResponse(json.dumps({'status':'OK','msg':'保存成功'}))
    else:
        return HttpResponse(json.dumps({'status': 'error', 'msg': '已经存在的用户'}))
'''
删除用户
'''
def deleteUser(request):
    sqlConn.delete(models.User,request.GET.get('id'))
    return HttpResponse(json.dumps({'status': 'OK', 'msg': '删除成功'}))
'''
跳转到用户编辑页
'''
def editUserPage(request):
    return render(request, 'manager/editUser.html')
'''
根据用户姓名查询用户
'''
def getUserbyName(request):
    uname = request.POST.get('name')
    user = sqlConn.getObjBywhere(models.User, {'name': uname}).scalar()
    if user.role=='管理员':
        return HttpResponse(json.dumps({'status': 'OK', 'msg': ''}))
    else:
        return HttpResponse(json.dumps({'status': 'error', 'msg': ''}))

