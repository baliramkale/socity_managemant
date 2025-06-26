from django.db import models

# Create your models here.

from django.db import models

class tenant(models.Model):
    roomno=models.IntegerField()
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    adharno=models.IntegerField()
    rent=models.IntegerField()
    mobile=models.IntegerField()
    
    def __str__(self):
        return self.name
        


class personaldata(models.Model):
    name=models.CharField(max_length=60)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=60)
    
    def __str__(self):
        return self.name


class MeterRecord(models.Model):
    meter_no = models.CharField(max_length=20)
    month = models.IntegerField()
    year = models.IntegerField()
    units_consumed = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.meter_no
    
    
class Submeter(models.Model):
    roomno = models.CharField(max_length=20)
    p=models.IntegerField()
    c=models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    
    

class Tanker(models.Model):
    
    month = models.IntegerField()
    year = models.IntegerField()
    totaltanker= models.IntegerField()
    amounttanker= models.IntegerField()
    maintenance= models.IntegerField()
    tenantno= models.IntegerField()
    
    def __str__(self):
        return self.totaltanker