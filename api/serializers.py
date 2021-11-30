from rest_framework import serializers
from company_info.models import Watch, companyList, Accounting


class WatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watch
        fields = ('id','company_name', 'company_code')

class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = companyList
        fields = ('id','company_name', 'company_code')

class AccountingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounting
        fields = "__all__"