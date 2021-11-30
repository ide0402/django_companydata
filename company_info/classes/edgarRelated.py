# scraping
import urllib.request,urllib.error
from bs4 import BeautifulSoup
from monthdelta import monthmod
import datetime
import json
import logging
import requests

# debug
import pdb
import pprint


class EdgarAPI:
    column_list = {
        'revenue': (
            'RevenueFromContractWithCustomerExcludingAssessedTax', 'Revenues',
        ),
        'operating_income': (
            'OperatingIncomeLoss',
        ),
        'net_income': (
            'NetIncomeLoss',
        ),
        'earnings_per_share': (
            'EarningsPerShareBasic', 'EarningsPerShareDiluted',
        )
    }


    def getCompanyCode(self):
        url = 'https://www.sec.gov/files/company_tickers_exchange.json'
        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req) as res:
                body = res.read()
                company_meta_data = BeautifulSoup(body, "html.parser")
                company_meta_data = json.loads(str(company_meta_data))
        except:
            logging.exception("Error happens when getCompanyCode.")
        return company_meta_data


    def checkScrapingResourceColumns(self, company_meta_data):
        field_columns = ['cik','name','ticker','exchange']
        if company_meta_data['fields'] == field_columns:
            return True
        else:
            return False


    def getAllAccountingData(self,cik_code):
        USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
        headers = {
            'user-agent': USER_AGENT,
        }
        url = "https://data.sec.gov/api/xbrl/companyfacts/CIK" + cik_code + ".json"
        accounting_all_data = {}
        try:
            api_response = requests.get(url,headers=headers)
            accounting_all_data = api_response.json()
        except:
            logging.exception("Error happens when getAllAccountingData.")
            print('error')

        return accounting_all_data


    def getAccountingDataByIndex(self, accounting_data, index):
        index_list = self.column_list
        target_index = index_list[index]
        for target_api_tag_name in target_index:
            try:
                accounting_data_by_index = self.extractShapedAccountingData(accounting_data['facts']['us-gaap'][target_api_tag_name]['units'])
                break
            except KeyError:
                continue
        return accounting_data_by_index


    def extractShapedAccountingData(self, accounting_data):
        shaped_data = []
        for key in accounting_data.keys():
            for data in accounting_data[key]:
                start_date = datetime.datetime.strptime(data['start'], '%Y-%m-%d')
                end_date = datetime.datetime.strptime(data['end'], '%Y-%m-%d')
                filed_date = datetime.datetime.strptime(data['filed'], '%Y-%m-%d')
                if (data['form'] == '10-K' and 
                        11 <= monthmod(start_date,end_date)[0].months <= 13):
                    data['fiscal_period'] = 'Q4'
                    data['accounting_type'] = 'total'
                    shaped_data.append(data)
                elif data['form'] == '10-Q' and data['fp'] == 'Q1':
                    data['fiscal_period'] = data['fp']
                    data['accounting_type'] = 'quarter/total'
                    shaped_data.append(data)
                elif (data['form'] == '10-Q' and 
                        2 <= monthmod(start_date,end_date)[0].months <= 4 and
                        monthmod(end_date, filed_date)[0].months <= 2):
                    data['fiscal_period'] = data['fp']
                    data['accounting_type'] = 'quarter'
                    shaped_data.append(data)
                elif (data['form'] == '10-Q' and
                        3 < monthmod(start_date,end_date)[0].months and
                        monthmod(end_date, filed_date)[0].months <= 2):
                    data['fiscal_period'] = data['fp']
                    data['accounting_type'] = 'total'
                    shaped_data.append(data)
                elif (data['form'] == '10-Q' and 
                        2 <= monthmod(start_date,end_date)[0].months <= 4 and
                        12 <= monthmod(end_date, filed_date)[0].months <= 14):
                    data['fiscal_period'] = data['fp']
                    data['accounting_type'] = 'quarter'
                    shaped_data.append(data)
                elif (data['form'] == '10-Q' and
                        3 < monthmod(start_date,end_date)[0].months and
                        12 <= monthmod(end_date, filed_date)[0].months <= 14):
                    data['fiscal_period'] = data['fp']
                    data['accounting_type'] = 'total'
                    shaped_data.append(data)

        shaped_data = self.addQuarterFourData(shaped_data)
        return shaped_data


    def addQuarterFourData(self, shaped_data):
        add_quarter4_data = shaped_data
        for data in shaped_data:
            if data['fiscal_period'] == 'Q3' and data['accounting_type'] == 'total':
                for for_Q4_data in shaped_data:
                    if for_Q4_data['fiscal_period'] == 'Q4' and for_Q4_data['start'] == data['start']:
                        new_data = {}
                        new_data['start'] = (datetime.datetime.strptime(data['end'], '%Y-%m-%d') + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
                        new_data['end'] = for_Q4_data['end']
                        new_data['fiscal_period'] = for_Q4_data['fiscal_period']
                        new_data['accounting_type'] = 'quarter'
                        new_data['val'] = int(for_Q4_data['val']) - int(data['val'])
                        add_quarter4_data.append(new_data)
                        break
        return add_quarter4_data