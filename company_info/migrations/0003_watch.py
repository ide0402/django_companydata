# Generated by Django 3.1.2 on 2021-06-30 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_info', '0002_auto_20210629_0458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255, verbose_name='企業名')),
                ('company_code', models.CharField(max_length=255, verbose_name='企業名コード')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'ウォッチリスト',
            },
        ),
    ]
