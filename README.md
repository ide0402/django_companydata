# description
上場会社に係る指標
①株価
②実績（今後実装予定）
③金利などの経済指標との相関チェック(今後実装予定)

# image
<!-- <img src="./image.gif" width="500px"> -->

# 環境
- python 3.7.2
- django 3.1.2

# start
- git clone https://github.com/ide0402/django_stockdata.git

- python manage.py migrate
- cp company_data/local_settings.example.py company_data/local_settings.py
- -> edit ALPHA_VANTAGE_API_KEY         // 個々で設定
       取得元：https://www.alphavantage.co/
