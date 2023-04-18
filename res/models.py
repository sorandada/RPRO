from django.db import models

class Shop(models.Model):
    #店舗ID
    id = models.CharField(primary_key=True, max_length=10)



