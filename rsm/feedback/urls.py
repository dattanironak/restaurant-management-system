from django.urls import path

from feedback import views

urlpatterns=[
    path('display', views.displayfeedback),
    path('', views.newfeedback),
]