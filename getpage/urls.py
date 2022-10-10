from argparse import Namespace
from django.urls import path 
from . import views
urlpatterns=[
    path('',views.test1,name='base') ,   #基础测试
    path('test1',views.test1,name='test1'),
    path('test2',views.test2,name='test2'),
]
   
