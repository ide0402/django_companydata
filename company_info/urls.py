"""company_data URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from company_info import views
from . import views

from django.conf.urls import url
from django.views.generic import RedirectView

from rest_framework import routers


app_name = 'company_info'
urlpatterns = [
    # root URL processed by front-end
    path('', views.index),
    path('search', views.index),
    path('watchlist/<int:watch_list_id>', views.index),

    # Request URL 
    path('search/<int:company_list_id>/store/', views.storeWatchList, name='add'),
    path('<int:company_list_id>/store/', views.storeWatchList, name='add'),
    path('<int:watch_list_id>/delete/', views.deleteWatchList, name='delete'),
    path('test/', views.getStockPriceByCalendarDate, name='selectCalendar'),
    # path('search/newlist/', views.getCompanyCodeFromEdgarAPI),
    path('watchlist/<int:watch_list_id>/api/', views.processAccountingRequestFromReact),
    # path('edgar_test/', views.getAllAccountingDataFromEdgarAPI),

    #new
    path('search/newlist/', views.storeListedCompanyList),

]

    # path('', views.showWatchList, name='watchlist'),
    # path('watchlist/', views.showCompanyInfo, name='info'),
    # path('search/', views.addWatchCompanyList.as_view(), name='search'),
    # path('watchlist/<int:watch_list_id>/', views.showCompanyStockInfo, name='show'),



