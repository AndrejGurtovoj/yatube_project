<<<<<<< HEAD
# posts/urls.py
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
=======
# posts/urls.py
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
>>>>>>> 69556b8a0716293534e47006d9c147481746765e
]