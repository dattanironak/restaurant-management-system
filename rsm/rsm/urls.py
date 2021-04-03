"""rsm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import views, settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('feedback/', include('feedback.urls')),
    path('login/', include('user.urls')),
    path('menu/', include('menu.urls')),
    path('bill/', include('Bill.urls'))
<<<<<<< HEAD
] + staticfiles_urlpatterns()
=======
]
>>>>>>> 673f329fd7fcf909a38534e4fb7b8022537e44f1
