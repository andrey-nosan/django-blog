from django.urls import path
from blog.views.post import *


urlpatterns = [
    path('post/', index, name='post_index'),
    path('post/<str:slug>/', show, name='post_show')
]