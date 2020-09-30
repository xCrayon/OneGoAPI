from django.db import models
from common import OGBaseModel


# Create your models here.
class Category(OGBaseModel):
    code = models.CharField(max_length=20,
                            verbose_name='编码',
                            unique=True)
    name = models.CharField(max_length=20,
                            verbose_name='名称')
    grade = models.IntegerField(default=1,
                                verbose_name='等级')
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True,
                               verbose_name='父类')
    picture_url = models.CharField(max_length=200,
                                   blank=True,
                                   null=True,
                                   verbose_name='图片路径')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_category'
        verbose_name = verbose_name_plural = '分类表'
