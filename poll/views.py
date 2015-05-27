from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.
namelist = []
numlist = []
def getlist():
    global namelist
    global numlist
    votelist = Vote.objects.all()
    for item in votelist:
        namelist.append(item.studentname)
        numlist.append(item.studentnumber)

def login(req):
    if req.session.get('username',''):
        return HttpResponseRedirect('/index/')
    if req.POST:
        password = req.POST.get('password')
        if password == "jxnuacs" :
            req.session['username'] = 'kdwycz'
            return HttpResponseRedirect('/index/')
        else:
            return HttpResponse("密码错误")
    return render(req, 'login.html', {})

def index(req):
    print('4')
    if req.session.get('username', '') == '':
        return HttpResponseRedirect('/')
    if req.POST:
        post = req.POST
        name = post.get('name')
        num = post.get('number')
        sz = Shirt.objects.get(sid = post.get('z'))
        sf = Shirt.objects.get(sid = post.get('f'))
        getlist()
        if name and num and (name in namelist or num in numlist):
            return HttpResponse("不能重复投票")
        Vote.objects.create(studentname = name, studentnumber = num, shirt = sz)
        Vote.objects.create(studentname = name, studentnumber = num, shirt = sf)
        sz.votenum += 1
        sf.votenum += 1
        sz.save()
        sf.save()
        return HttpResponseRedirect('/logout/')
    return render(req, 'index.html', {})

def logout(req):
    req.session['username'] = ''
    shirt = Shirt.objects.all()
    content = {'shirt': shirt}
    return render(req, 'logout.html', content)
