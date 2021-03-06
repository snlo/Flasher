# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-27 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(default=0, verbose_name='分类')),
                ('goods_id', models.CharField(max_length=10, verbose_name='商品ID')),
                ('goods_name', models.CharField(default='', max_length=100, verbose_name='商品名')),
                ('goods_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='商品价格')),
                ('goods_Stock', models.IntegerField(default=100, verbose_name='商品库存')),
                ('sales_Volume', models.IntegerField(default=0, verbose_name='销量')),
                ('goods_introduce', models.CharField(default='', max_length=250, verbose_name='商品简介')),
            ],
        ),
    ]
