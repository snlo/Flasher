from django.db import models

class goods(models.Model):
    category = models.IntegerField('分类',default=0)
    goods_id = models.CharField('商品ID',max_length=10)
    goods_name = models.CharField('商品名',max_length=100,default='')
    goods_price = models.DecimalField('商品价格',max_digits=10,decimal_places=2)
    goods_Stock = models.IntegerField('商品库存',default=100)
    sales_Volume = models.IntegerField('销量',default=0)
    goods_introduce = models.CharField('商品简介',max_length=250,default='')
    def __str__(self):
        return self.goods_name