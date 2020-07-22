from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100, null=False, blank=True, verbose_name='Title')
    status = models.CharField(max_length=100, default='New', blank=True, verbose_name='Status')
    date_perform = models.DateField(default='', verbose_name='Data')

