# Generated by Django 3.1.2 on 2021-06-29 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='companyList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255, verbose_name='企業名')),
                ('company_code', models.CharField(max_length=255, verbose_name='企業名コード')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '上場企業リスト',
            },
        ),
        migrations.RenameModel(
            old_name='Company',
            new_name='companyInfo',
        ),
    ]