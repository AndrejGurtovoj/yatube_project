<<<<<<< HEAD
# posts/urls.py
=======
>>>>>>> 98b8eadd3bfa24a547381b81a4bf0b81313271c0
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index),
<<<<<<< HEAD
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
]
=======
    path('group/<slug:slug>/', views.group_posts, name='group_list')
]
>>>>>>> 98b8eadd3bfa24a547381b81a4bf0b81313271c0
