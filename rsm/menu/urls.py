from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu),
    path('update', views.updateMenu),
    path('additem', views.additem),
    path('updateitem/<uid>', views.updateitem),
    path('deleteitem/<did>', views.deleteitem),
    path('changeavailable/<cid>', views.changeavailable)
]