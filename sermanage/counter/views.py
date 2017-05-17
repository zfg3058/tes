# coding: utf8
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def readFileData(path):
    dat = []
    for line in open(path):
        s = line.strip()
        dat.append(s)
    return dat

def index(request):
    #     return HttpResponse('welcome!')
    return render(request, 'test.html')

def login(request):
    return render_to_response('../templates/counter/login.html')

@csrf_exempt
def logins(request):
    if request.method=='GET':
        print 'method==get'
        return render_to_response('counter/login.html')
    if request.method == 'POST':
        print 'method====post'
        name = request.POST.get('name')
        pasw = request.POST.get('password')
        if name=='admin' and pasw =='admin':
            return itemlist()
        else:
            return HttpResponse('账号密码错误')
        # return render_to_response('index.html',RequestContext(request, {'form':''}))
    
def itemlist():
    itemls =['状态','服务器IP','CPU','内存','硬盘','类型','客户','起始日期','结束日期','提交工单']
    return render_to_response('index.html', {'items':itemls,'dic':dicd})

def tab(request):
    # assetpath = '../static/datafile/asset.dat'
    # assetlist = readFileData(assetpath)
    assetitem =['编号','状态','服务器IP','CPU','内存','硬盘','类型','备注','起始日期','结束日期']
    return render_to_response('tab.html', {'assetitem':assetitem,'assetd':assetd})

def book(request):
    return render_to_response('book.html')

@csrf_exempt
def submit(request):
    return render_to_response('test.html',request,{})
    # return HttpResponse('提交成功！')

@csrf_exempt
def adduser(request):
    return render(request,'test.html')

def info(request):
    return render_to_response('info.html')

def add(request):
    return render_to_response('add.html')

def adv(request):
    return render_to_response('adv.html')

def cate(request):
    return render_to_response('cate.html')

def cateedit(request):
    return render_to_response('cateedit.html')

def column(request):
    return render_to_response('column.html')

def list(request):
    return render_to_response('list.html',{'liuyan':liuyand})

def page(request):
    return render_to_response('page.html')

def passwd(request):
    return render_to_response('pass.html')

def tips(request):
    return render_to_response('tips.html')

def adduser(request):
    return render_to_response('adduser.html')

def users(request):
    # userspath = '../static/datafile/users.dat'
    # userlist = readFileData(userspath)
    return render_to_response('users.html',{'user':usersd})

def usergroup(request):
    # usergpath = '../static/datafile/usergroup.dat'
    # grouplist = readFileData(usergpath)
    return render_to_response('usergroup.html', {'group':usergroupd})


liuyand = ['这是一套MUI后台精美管理系统，我的支持','这是一套MUI后台精美管理系统，您的支持','这是一套MUI后台精美管理系统，感谢您的支持',
          '这是一套MUI后台精美管理系统，她的支持','这是一套MUI后台精美管理系统，感谢支持','这是一套MUI后台精美管理系统，请多支持',
          '这是一套MUI后台精美管理系统，她的支持','这是一套MUI后台精美管理系统，她的支持','这是一套MUI后台精美管理系统，她的支持',
          '这是一套MUI后台精美管理系统，她的支持','这是一套MUI后台精美管理系统，她的支持','这是一套MUI后台精美管理系统，她的支持',
          '这是一套MUI后台精美管理系统，她的支持','这是一套MUI后台精美管理系统，她的支持','这是一套MUI后台精美管理系统，她的支持']

usergroupd = [{'jibie':'一级用户','num':'100','beizhu':'此级别可以看到二级用户','time':'2016-12-12 12:30:20'},
            {'jibie':'二级用户','num':'500','beizhu':'此级别可以看到三级用户','time':'2016-12-12 12:30:20'},
            {'jibie':'三级用户','num':'2000','beizhu':'此级别可以看到四级用户','time':'2016-12-12 12:30:20'},
            {'jibie':'四级用户','num':'10000','beizhu':'此级别只能看到自己','time':'2016-12-12 12:30:20'}]

dicd = [{'statu':'正常','ip':'192.168.0.121','cpu':'I6500U*2','ram':'16G','YP':'2T','TYPE':'租用主机','kehu':'游讯','bgtime':'2016-11-11','edtime':'2016-12-12','tjgd':'提交工单'},
       {'statu':'正常','ip':'192.168.0.122','cpu':'I6500U*2','ram':'16G','YP':'2T','TYPE':'租用主机','kehu':'游讯','bgtime':'2016-11-11','edtime':'2016-12-12','tjgd':'提交工单'},
       {'statu':'正常','ip':'192.168.0.123','cpu':'I6500U*2','ram':'16G','YP':'2T','TYPE':'租用主机','kehu':'游讯','bgtime':'2016-11-11','edtime':'2016-12-12','tjgd':'提交工单'},
       {'statu':'正常','ip':'192.168.0.124','cpu':'I6500U*2','ram':'16G','YP':'2T','TYPE':'租用主机','kehu':'游讯','bgtime':'2016-11-11','edtime':'2016-12-12','tjgd':'提交工单'},
       {'statu':'正常','ip':'192.168.0.125','cpu':'I6500U*2','ram':'16G','YP':'2T','TYPE':'租用主机','kehu':'游讯','bgtime':'2016-11-11','edtime':'2016-12-12','tjgd':'提交工单'}]


assetd = [{'id':'1','asId':'x1001','statu':'闲置','ip':'192.168.0.121','cpu':'I6500U*2','ram':'16G*2','YP':'2T*2','TYPE':'租用主机','remark':'游讯','bgtime':'2016-11-11','edtime':'2016-12-12'},
        {'id':'2','asId':'x1002','statu':'闲置','ip':'192.168.0.122','cpu':'I6500U*2','ram':'16G','YP':'2T','TYPE':'租用主机','remark':'游讯','bgtime':'2016-11-11','edtime':'2016-12-12'},
        {'id':'3','asId':'x1003','statu':'闲置','ip':'192.168.0.123','cpu':'I6500U*2','ram':'16G*4','YP':'1T*3','TYPE':'租用主机','remark':'游讯','bgtime':'2016-11-11','edtime':'2016-12-12'},
        {'id':'4','asId':'x1004','statu':'闲置','ip':'192.168.0.123','cpu':'I6500U*2','ram':'16G*4','YP':'1T*3','TYPE':'租用主机','remark':'游讯','bgtime':'2016-11-11','edtime':'2016-12-12'},
        {'id':'5','asId':'x1005','statu':'闲置','ip':'192.168.0.123','cpu':'I6500U*2','ram':'16G*4','YP':'1T*3','TYPE':'租用主机','remark':'游讯','bgtime':'2016-11-11','edtime':'2016-12-12'},
        {'id':'6','asId':'x1006','statu':'闲置','ip':'192.168.0.123','cpu':'I6500U*2','ram':'16G*4','YP':'1T*3','TYPE':'租用主机','remark':'游讯','bgtime':'2016-11-11','edtime':'2016-12-12'},
        {'id':'7','asId':'x1007','statu':'闲置','ip':'192.168.0.123','cpu':'I6500U*2','ram':'16G*4','YP':'1T*3','TYPE':'租用主机','remark':'游讯','bgtime':'2016-11-11','edtime':'2016-12-12'},
        {'id':'8','asId':'x1008','statu':'闲置','ip':'192.168.0.123','cpu':'I6500U*2','ram':'16G*4','YP':'1T*3','TYPE':'租用主机','remark':'游讯','bgtime':'2016-11-11','edtime':'2016-12-12'},
        {'id':'9','asId':'x1009','statu':'闲置','ip':'192.168.0.123','cpu':'I6500U*2','ram':'16G*4','YP':'1T*3','TYPE':'租用主机','remark':'游讯','bgtime':'2016-11-11','edtime':'2016-12-12'},
        {'id':'10','asId':'x1010','statu':'闲置','ip':'192.168.0.123','cpu':'I6500U*2','ram':'16G*4','YP':'1T*3','TYPE':'租用主机','remark':'游讯','bgtime':'2016-11-11','edtime':'2016-12-12'},
        {'id':'11','asId':'x1011','statu':'闲置','ip':'192.168.0.123','cpu':'I6500U*2','ram':'16G*4','YP':'1T*3','TYPE':'租用主机','remark':'游讯','bgtime':'2016-11-11','edtime':'2016-12-12'},
        {'id':'12','asId':'x1012','statu':'闲置','ip':'192.168.0.123','cpu':'I6500U*2','ram':'16G*4','YP':'1T*3','TYPE':'租用主机','remark':'游讯','bgtime':'2016-11-11','edtime':'2016-12-12'},
        {'id':'13','asId':'x1013','statu':'闲置','ip':'192.168.0.123','cpu':'I6500U*2','ram':'16G*4','YP':'1T*3','TYPE':'租用主机','remark':'游讯','bgtime':'2016-11-11','edtime':'2016-12-12'},
        {'id':'14','asId':'x1014','statu':'1001','ip':'192.168.0.124','cpu':'I6500U*2','ram':'8G*4','YP':'2T','TYPE':'租用主机','remark':'游讯','bgtime':'2016-11-11','edtime':'2016-12-12'},
        {'id':'15','asId':'x1015','statu':'报废','ip':'192.168.0.125','cpu':'I6500U*2','ram':'16G','YP':'2T','TYPE':'租用主机','remark':'游讯','bgtime':'2016-11-11','edtime':'2016-12-12'},
        {'id':'16','asId':'x1016','statu':'报废','ip':'192.168.0.125','cpu':'I6500U*2','ram':'16G','YP':'2T','TYPE':'租用主机','remark':'游讯','bgtime':'2016-11-11','edtime':'2016-12-12'}]



usersd = [{'ID':'1001','name':'zhaofenggang','level':'一级用户','assets':'1,2,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'1002','name':'zhaofenggang','level':'一级用户','assets':'4,5,9','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'1003','name':'zhaofenggang','level':'一级用户','assets':'7,8,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'1004','name':'zhaofenggang','level':'一级用户','assets':'1,2,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'1005','name':'zhaofenggang','level':'一级用户','assets':'1,2,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'2001','name':'zhaofenggang','level':'二级用户','assets':'1,2,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'2002','name':'zhaofenggang','level':'二级用户','assets':'1,2,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'2003','name':'zhaofenggang','level':'二级用户','assets':'1,2,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'2004','name':'zhaofenggang','level':'二级用户','assets':'1,2,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'2005','name':'zhaofenggang','level':'二级用户','assets':'1,2,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'3001','name':'zhaofenggang','level':'三级用户','assets':'1,2,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'3002','name':'zhaofenggang','level':'三级用户','assets':'1,2,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'3003','name':'zhaofenggang','level':'三级用户','assets':'1,2,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'3004','name':'zhaofenggang','level':'三级用户','assets':'1,2,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'3005','name':'zhaofenggang','level':'三级用户','assets':'1,2,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'4001','name':'zhaofenggang','level':'四级用户','assets':'1,2,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'4002','name':'zhaofenggang','level':'四级用户','assets':'1,2,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'4003','name':'zhaofenggang','level':'四级用户','assets':'1,2,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'4004','name':'zhaofenggang','level':'四级用户','assets':'1,2,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'4005','name':'zhaofenggang','level':'四级用户','assets':'1,2,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'4006','name':'zhaofenggang','level':'四级用户','assets':'1,2,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'4007','name':'zhaofenggang','level':'四级用户','assets':'1,2,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'4008','name':'zhaofenggang','level':'四级用户','assets':'1,2,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'4009','name':'zhaofenggang','level':'四级用户','assets':'1,2,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'4010','name':'zhaofenggang','level':'四级用户','assets':'1,2,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'},
        {'ID':'4011','name':'zhaofenggang','level':'四级用户','assets':'1,2,3','remark':'最高级别','rgtime':'2016-12-01 12:12:30'}]
