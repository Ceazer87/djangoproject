from django.urls import path


from . import views

urlpatterns=[
    path('', views.index),
    path('upload_movie/', views.upload),
    path('test_list/',views.test_list),
    path('video.compared/', views.video_compared),
]