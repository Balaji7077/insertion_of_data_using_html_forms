from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def topic(request):
    if request.method=='POST':

        tn=request.POST['tn']

        TO=Topic.objects.get_or_create(topic_name=tn)[0]

        TO.save()
        QLTO=Topic.objects.all()
        d={'topics':QLTO}
        return render(request,'display_topic.html',d)
    
    return render(request,'topic.html')


def webpage(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':

        tn=request.POST['tn']
        n=request.POST['n']
        u=request.POST['u']
        e=request.POST['e']

        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
        WO.save()
        QLWO=Webpage.objects.all()
        d1={'webpages':QLWO}
        return render(request,'display_webpage.html',d1)
    
    return render(request,'webpage.html')

def accessrecord(request):
    QLWO=Webpage.objects.all()
    d1={'webpages':QLWO}
    if request.method=='POST':

        n=request.POST['n']
        d=request.POST['d']
        a=request.POST['a']

        WO=Webpage.objects.get(name=n)
        AO=AccessRecord.objects.get_or_create(name=WO,date_of_birth=d,author=a)[0]

        AO.save()
        QLAO=AccessRecord.objects.all()
        d2={'accessrecods': QLAO}
        return render(request,'display_access.html',d2)
    
    return render(request,'accessrecord.html')

def select_multiple_web(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}

    if request.method=='POST':
        topiclist=request.POST.getlist('tn')
        QLWO=Webpage.objects.none()
        for i in topiclist:
            QLWO=QLWO|Webpage.objects.filter(topic_name=i)
        d1={'webpages': QLWO}
        return render(request,'display_webpage.html',d1)

    return render(request,'select_multiple_web.html',d)
def select_multiple_access(request):
    QLWO=Webpage.objects.all()
    d={'webpages': QLWO}

    if request.method=='POST':
        weblist=request.POST.getlist('n')
        print(weblist)
        QLAO=AccessRecord.objects.none()
        for x in weblist:
            print(x)
            w=Webpage.objects.get(pk=int(x))
            QLAO=QLAO|AccessRecord.objects.filter(name=w)
        d1={'accessrecords': QLAO}
        return render(request,'display_access.html',d1)
    return render(request,'select_multiple_access.html',d)

def checkbox_web(request):
    QLTO=Webpage.objects.all()
    d={'topics': QLTO}
    return render(request,'checkbox_web.html',d)