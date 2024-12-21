from django.db import models
class intradata(models.Model):
    companyName = models.CharField(max_length=100)
    marketCap=models.CharField(null=True , max_length=100)
    initialPrice = models.DecimalField(max_digits=10,decimal_places=2)
    maximaOfGap=models.DecimalField(max_digits=10, decimal_places=2)
    minimaOfGap=models.DecimalField(max_digits=10, decimal_places=2)
    gap=models.DecimalField(max_digits=10, decimal_places=2)
    finalPrice  = models.DecimalField(max_digits=10, decimal_places=2)
    finalGain=models.DecimalField(max_digits=10, decimal_places=2)
    dayHigh = models.DecimalField(max_digits=10, decimal_places=2)
    dayLow = models.DecimalField(max_digits=10, decimal_places=2)
    maximaOfGap1=models.DecimalField(null=True,max_digits=10, decimal_places=2)
    minimaOfGap1=models.DecimalField(null=True,max_digits=10, decimal_places=2)
    gap1=models.DecimalField(null=True,max_digits=10, decimal_places=2)
    finalPrice1  = models.DecimalField(null=True,max_digits=10, decimal_places=2)
    finalGain1 = models.DecimalField(null=True,max_digits=10, decimal_places=2)
    dayHigh1 = models.DecimalField(null=True,max_digits=10, decimal_places=2)
    dayLow1 = models.DecimalField(null=True,max_digits=10, decimal_places=2)
    maximaOfGap2=models.DecimalField(null=True,max_digits=10, decimal_places=2)
    minimaOfGap2=models.DecimalField(null=True,max_digits=10, decimal_places=2)
    gap2=models.DecimalField(null=True,max_digits=10, decimal_places=2)
    finalPrice2  = models.DecimalField(null=True,max_digits=10, decimal_places=2)
    finalGain2 = models.DecimalField(null=True,max_digits=10, decimal_places=2)
    dayHigh2 = models.DecimalField(null=True,max_digits=10, decimal_places=2)
    dayLow2 = models.DecimalField(null=True,max_digits=10, decimal_places=2)
    Date=models.DateField(null=True)

    
    

# Create your models here.
