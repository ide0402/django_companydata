from django.core.management.base import BaseCommand
from company_info.models import Watch,companyList,Accounting
import company_info.views

class Command(BaseCommand):
    def handle(self, *args, **options):
        watch_list = Watch.objects.all()
        for watch in watch_list:
            getAndStoreAccountingData(watch.cik, watch.company_name)
