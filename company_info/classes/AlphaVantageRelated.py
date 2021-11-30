# panda_reader関連
from django.conf import settings
import pandas as pd
import pandas_datareader.data as web

# debug
import pdb
import pprint

class AlphaVantageAPI:
    def getStockPrice(self, symbol, start_date, end_date):
        api_data = web.DataReader(symbol, 'av-daily', start_date, end_date, api_key = settings.ALPHA_VANTAGE_API_KEY)
        api_data = api_data.to_json()
        return api_data
