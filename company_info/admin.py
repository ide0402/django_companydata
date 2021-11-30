from django.contrib import admin
from import_export.resources import ModelResource
from import_export.admin import ImportMixin
from import_export.formats import base_formats
from import_export import fields
from .models import companyList

class companyListResource(ModelResource):
    name = fields.Field(attribute='company_name', column_name='Name')
    code = fields.Field(attribute='company_code', column_name='Symbol')

    class Meta:
        model = companyList
        skip_unchanged = True
        import_id_fields = ['code']

@admin.register(companyList)
class companyListAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ('company_name', 'company_code','cik','exchange')
    resource_class = companyListResource
    formats = [base_formats.CSV]



