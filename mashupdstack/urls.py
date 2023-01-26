"""mashupdstack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from medicine import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    
    path("login/",LoginView.as_view(), name="login"),
    path("",views.base , name="base.html"),
    path("index/",views.index ,name="home"),
    path("index/edit/<int:id>",views.edit , name="edit"),
    path("index/delete/<int:id>",views.delete, name="delete"),
    path("add/",views.add, name="add"),
    path("search",views.search, name="search.html"),
    path("register",views.register,name ="register"),
    path("accounts/profile/",views.profile,name ="profile"),

    path('logout/',LogoutView.as_view(),name="logout"),
    path('catalog/', include('catalog.urls')),
  


]
