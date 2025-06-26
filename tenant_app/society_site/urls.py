from .import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    
    path('',views.login),
    path('addtenant',views.addtenant),
    path('demo',views.demo),
    
    path('addingtenants',views.addingtenants),
    
    path('tenantdata',views.tenantdata),
    
    path('deletetenant',views.deletetenant),
    
    path('profileupdate',views.profileupdate),
    
    path('edit',views.edit),
    
    path('registered',views.registered),
    
    path('logined',views.logined),
    
    path('register',views.register),
    
    path('index',views.index),
    
    path('search',views.search),
    
    path('mainmeter',views.mainmeter),
    
    path('mainmeterentry',views.mainmeterentry),
    
    path('submeter',views.submeter),
    
    path('submeterentry',views.submeterentry),
    
    path('tanker',views.tanker),
    
    path('addtanker',views.addtanker),
    
    path('gallary',views.gallary),
    
    path('addcookie',views.addcookie),
    
    path('logout',views.logout),
]
