
## ◆実装サンプル  
[sample](https://user-images.githubusercontent.com/69793509/145155804-90f0a99d-b0db-4662-8a1a-5e35a6d6eb5d.mov)  


## ◆機能

上場会社に係る指標の取得・整形

①株価関連

②業績

③金利等の経済指標との相関チェック(今後実装予定)

## ◆フロントエンド(React)

[https://github.com/ide0402/companydata_front](https://github.com/ide0402/companydata_front)

## ◆ディレクトリ構成

　django

　├── companydata (バックエンド)

　└── companydata_front (フロントエンド)

## ◆環境



* Python 3.7.2
* django 3.1.2
* SQLite 3.28.0

## ◆インストール

　- pip install django-cors-headers

　- pip install djangorestframework

　- pip install django-import_export

　- pip install requests

　- pip install MonthDelta

　- pip install beautifulsoup4

　- pip install pandas

　- pip install pandas_datareader

　- pip install matplotlib

## ◆手順

- git clone https://github.com/ide0402/django_companydata.git

- フォルダ名の変更　「django_companydata」 → 「company_data」

- cp company_data/local_settings.example.py company_data/local_settings.py

- → edit ALPHA_VANTAGE_API_KEY         // 個々で設定

       取得元：https://www.alphavantage.co/

- python3 manage.py runserver

## ◆今後の実装予定

①株価関連



* 株価以外の指標の追加：PER等
* カレンダーのUI調整

	

②業績関連



* 桁数の調整
* 指標の追加(前年度比などの比率追加)
* グラフ機能の追加

③金利等の経済指標との相関チェック(今後実装予定)

