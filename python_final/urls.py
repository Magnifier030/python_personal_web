"""
URL configuration for python_final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from mysite import views

urlpatterns = [
    path('news/', views.nkustnews),
    path('phonelist/', views.phonelist),  # 列出所有新款手機
    path('phonelist/maker/<int:id>/', views.phonelist),  # 列出指定廠牌的所有手機
    path('phonelist/country/<str:country>/', views.phonelist),  # 列出指定國家的所有手機
    path('stock300list/', views.stock300list), # 列出所有股價超過300元的公司
    path('chart/', views.chart), 
    path('all/', views.all_data),         # 顯示所有的站
    path("filter/", views.filtered_data), # 顯示超過10台可用自行車的站
    path('', views.index ),  # 如果有人來瀏覽首頁的話，請交給views.py裡面的index()函式處理
    path('admin/', admin.site.urls),
]
