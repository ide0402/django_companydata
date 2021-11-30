from django.db import models

# Create your models here.
class companyList(models.Model):
    cik = models.CharField(max_length=255, verbose_name='CIKコード')
    company_name = models.CharField(max_length=255, verbose_name='企業名')
    company_code = models.CharField(max_length=255, verbose_name='企業名コード')
    exchange = models.CharField(max_length=255, verbose_name='取引市場', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = '上場企業リスト'


class Watch(models.Model):
    cik = models.CharField(max_length=255, verbose_name='CIKコード')
    company_name = models.CharField(max_length=255, verbose_name='企業名')
    company_code = models.CharField(max_length=255, verbose_name='企業名コード')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'ウォッチリスト'


class Accounting(models.Model):
    company_name = models.CharField(max_length=255, verbose_name='企業名')
    cik = models.CharField(max_length=255, verbose_name='CIKコード')
    # finaicial_year = models.CharField(max_length=255, verbose_name='会計年度', default="-")
    fiscal_period = models.CharField(max_length=255, verbose_name='会計期間', default="-")
    accounting_type = models.CharField(max_length=255, verbose_name='決算種類')
    revenue = models.BigIntegerField(verbose_name='売上', null=True)
    operating_income = models.BigIntegerField(verbose_name='営業利益', null=True)
    net_income = models.BigIntegerField(verbose_name='純利益', null=True)
    earnings_per_share = models.FloatField(verbose_name='EPS', null=True)
    period = models.CharField(max_length=255, verbose_name='決算期間')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = '決算数値'



