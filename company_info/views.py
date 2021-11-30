# model
from .models import companyList, Watch, Accounting 

#other
from django.shortcuts import render,redirect
from django.views.generic import ListView
import requests
from django.views import generic
from django.db.models import Q
from django.conf import settings
import json
from django.http import HttpResponse
from monthdelta import monthmod
import logging

# scraping
import urllib.request,urllib.error
from bs4 import BeautifulSoup

# panda_reader関連
import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# debug
import pdb
import pprint

#drf
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status

from django.http import JsonResponse

#class
from company_info.classes.edgarRelated import EdgarAPI
from company_info.classes.AlphaVantageRelated import AlphaVantageAPI


def index(request, watch_list_id = ''):
    return render(request, 'company_info/index.html')


# ----------------------------------------------------------------
#    WatchList(Top) Page related method
# ----------------------------------------------------------------
def deleteWatchList(request, watch_list_id):
    watch_list = Watch.objects.get(id = watch_list_id)
    watch_list.delete()
    return HttpResponse('')


# ----------------------------------------------------------------
#    Search Page related method
# ----------------------------------------------------------------
def storeListedCompanyList(request):
    edgarAPI = EdgarAPI()
    company_meta_data = edgarAPI.getCompanyCode()
    if edgarAPI.checkScrapingResourceColumns(company_meta_data):
        try:
            companyList.objects.all().delete()
            for one_company_meta_data in company_meta_data['data']:
                companyList.objects.create(
                    cik = str(one_company_meta_data[0]).zfill(10),
                    company_name = one_company_meta_data[1],
                    company_code = one_company_meta_data[2],
                    exchange = one_company_meta_data[3],
                )
            companyList.objects.filter(exchange='').delete()
        except:
            logging.exception("Error happens when storeListedComapanyList.")
    return HttpResponse('')


def storeWatchList(request, company_list_id):
    company_list = companyList.objects.get(pk = company_list_id)
    new_watch_company = Watch(company_name=company_list.company_name, company_code=company_list.company_code, cik=company_list.cik)
    new_watch_company.save()
    return HttpResponse('')


# ----------------------------------------------------------------
#    WatchListDetail Page related method
# ----------------------------------------------------------------
def getStockPriceByCalendarDate(request):
    alphaVantageAPI = AlphaVantageAPI()
    request_from_react_calendar = json.loads(request.body)
    watch_list = Watch.objects.get(id = request_from_react_calendar['watchlist_id'])
    symbol = watch_list.company_code
    stock_data = alphaVantageAPI.getStockPrice(symbol, request_from_react_calendar['startDate'], request_from_react_calendar['endDate'])
    return JsonResponse(stock_data, safe = False)


def processAccountingRequestFromReact(request, watch_list_id):
    watch_list = Watch.objects.get(id = watch_list_id) 
    cik_code = watch_list.cik
    company_name = watch_list.company_name
    # if not Accounting.objects.filter(cik = cik_code).exists():
    getAndStoreAccountingData(cik_code, company_name)
    response_data = {
        'cik':cik_code,
        'company_name':company_name,
    }
    return JsonResponse(response_data, safe = False)


def getAndStoreAccountingData(cik_code, company_name):
    edgarAPI = EdgarAPI()
    index_list = edgarAPI.column_list
    all_accounting_data = edgarAPI.getAllAccountingData(cik_code)
    for target_index in index_list:
        accounting_data_by_index = edgarAPI.getAccountingDataByIndex(all_accounting_data, target_index)
        if not accounting_data_by_index is None:
            storeAccountingData(accounting_data_by_index, target_index, company_name, cik_code)            


def storeAccountingData(accounting_data_by_index, accounting_index, company_name, cik_code):
    for data in accounting_data_by_index:
        period = data['start'] + ' ~ ' + data['end']
        Accounting.objects.update_or_create(
            cik = cik_code,
            accounting_type = data['accounting_type'],
            fiscal_period = data['fiscal_period'],
            period = period,
            defaults = {
                "company_name": company_name,
                "cik": cik_code, 
                "accounting_type": data['accounting_type'],
                "fiscal_period": data['fiscal_period'],
                **{accounting_index: data['val']},
                "period": period
            }
        )


class ObjectLike(dict):
    __getattr__ = dict.get