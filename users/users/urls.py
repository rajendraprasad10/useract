"""users URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

# urls for the whole project here
from django.contrib import admin
from django.urls import path,include
from usersapp.views import index
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('userset', views.Userview) # api url creation
router.register('activitytimeset', views.Useract) # api url creation
router.register('alluseractivitics', views.Userdata) # api url creation
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('api/', include(router.urls))
]
