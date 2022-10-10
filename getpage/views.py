from django.shortcuts import render,HttpResponse
# Create your views here.
from  urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import re
import requests
#creat my function to html page
def test1(request):
    method=request.method
    if method =='GET':
        return render(request,'base.html')
    elif method =='POST':
        url=request.POST.get('url')
        tag=request.POST.get('tag')
        if url:
                head={'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
                Req=Request(url,method='GET',headers=head)
                resp=urlopen(Req)
                html=BeautifulSoup(resp,'html.parser')
                tagtext=' '
                taglist=html.find_all(tag)
                for text in taglist:
                    tagtext=tagtext+text.get_text()
                tagtext=[i for i in tagtext.split(' ') if len(i)>=2]
                contents={'url':url,'tag':tag,'tagtext':tagtext}
                return render(request,'response.html',contents)
        else:
            contents={'url':url,'tag':tag,'tagtext':'没有找到'}
            return render(request,'response.html',contents)
def test2(request):
    method=request.method
    if method =='GET':
        return render(request,'base.html')
    elif method =='POST':
        url=request.POST.get('url')
        tag=request.POST.get('tag')
        cookie=request.POST.get('cookie')
        if url:
                head={'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
                head['Cookie']=cookie
                try:
                    Req=Request(url,method='GET',headers=head)
                    resp=urlopen(Req)
                except:
                    resp=requests.post(url,headers=head)
                html=BeautifulSoup(resp,'html.parser')
                tagtext=' '
                taglist=html.find_all(tag)
                for text in taglist:
                    tagtext=tagtext+text.get_text()
                tagtext=[i for i in tagtext.split(' ') if len(i)>=2]
                contents={'url':url,'tag':tag,'tagtext':tagtext}
                return render(request,'response.html',contents)
        else:
            contents={'url':url,'tag':tag,'tagtext':'没有找到'}
            return render(request,'response.html',contents)

    

            


