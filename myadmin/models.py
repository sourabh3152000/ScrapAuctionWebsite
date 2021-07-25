from django.db import models



class Category(models.Model):
    catid=models.AutoField(primary_key=True)
    catnm=models.CharField(max_length=100)
    caticonnm=models.CharField(max_length=100)
    
class SubCategory(models.Model):
    subcatid=models.AutoField(primary_key=True)
    catid=models.IntegerField()
    subcatnm=models.CharField(max_length=100)
    subcaticonnm=models.CharField(max_length=100)
    
class Product(models.Model):
    pid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    catid=models.IntegerField()
    subcatid=models.IntegerField()
    pdescription=models.CharField(max_length=100)
    bprice=models.IntegerField()
    piconnm=models.CharField(max_length=100)
    info=models.CharField(max_length=100)
   
