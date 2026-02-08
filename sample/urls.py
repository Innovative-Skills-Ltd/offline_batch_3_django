"""
URL configuration for sample project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path

from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.sample_view), #root URL
    path('sum/', views.sum),
    path('demo_html/',views.demo_template),
    path('insert_login/',views.demo_insert,name='insert'),
    path('user_list/',views.user_list,name='show_user'),
    path('edit/<int:uid>',views.editUser,name='edit_user'),
    path('update/',views.update_user,name='update'),
]
