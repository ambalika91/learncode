'''
URLS for the website
'''

from django.conf.urls import url
from django.contrib import admin
from website.views import index

urlpatterns = [
    url(r'index.html', index.as_view(),name="index")
    
]