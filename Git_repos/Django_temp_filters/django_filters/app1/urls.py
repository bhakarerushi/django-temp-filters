from django.contrib import admin
from django.urls import path
from .views import testview

urlpatterns = [
    path('test/',testview, name ='test'),

]
