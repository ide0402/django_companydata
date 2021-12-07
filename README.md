# description
上場会社に係る指標  
①株価  
②実績（今後実装予定）  
③金利などの経済指標との相関チェック(今後実装予定)

# フロントエンド(React)
https://github.com/ide0402/companydata_front

# ディレクトリ構成

django  
 ├── companydata (バックエンド)  
 └── companydata_front (フロントエンド)

# 環境
- python  3.7.2
- django  3.1.2
- SQLite3 3.28.0
- 

# インストール
- pip install django-cors-headers
- pip install djangorestframework
- pip install django-import_export
- pip install requests
- pip install MonthDelta
- pip install beautifulsoup4
- pip install pandas
- pip install pandas_datareader
- pip install matplotlib


# start
- git clone https://github.com/ide0402/django_companydata.git
- フォルダ名の変更　「django_companydata」 → 「company_data」
- cp company_data/local_settings.example.py company_data/local_settings.py
- -> edit ALPHA_VANTAGE_API_KEY         // 個々で設定
       取得元：https://www.alphavantage.co/
- python3 manage.py runserver
