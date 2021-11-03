from django.urls import path
from . import views

urlpatterns = [
    path('upload_img', views.upload_img, name="upload_img"),
    path('upload_excel', views.upload_excel, name="upload_excel"),
    path('logout',views.logout, name="logout"),
    path('index',views.index, name="index")
]