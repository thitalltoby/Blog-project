from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),
    path('post_detail/', views.post_detail, name="blog-post_detail")
]