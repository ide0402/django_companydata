from rest_framework import viewsets, routers, pagination
from company_info.models import Watch, companyList, Accounting
from .serializers import WatchSerializer, CompanyListSerializer, AccountingSerializer
from django.db.models import Q

import pdb

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 100
    

class WatchViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = WatchSerializer
    queryset = Watch.objects.all()



class CompanyListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyListSerializer
    queryset = companyList.objects.all()
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = companyList.objects.all()
        q_word = self.request.query_params.get('query')
 
        if q_word:
            # pdb.set_trace()
            queryset = queryset.filter(
                Q(company_name__icontains=q_word) | Q(company_code__icontains=q_word))
        else:
            queryset = companyList.objects.all()
        return queryset

class AccountingViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AccountingSerializer
    queryset = Accounting.objects.all()

    def get_queryset(self):
        queryset = Accounting.objects.all()
        cik_code = self.request.query_params.get('cik')
        queryset = queryset.filter(cik=cik_code)
        return queryset

    

router = routers.DefaultRouter()
router.register(r'watchlist', WatchViewSet)
router.register(r'companylist', CompanyListViewSet)
router.register(r'accounting', AccountingViewSet)