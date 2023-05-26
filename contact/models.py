from django.db import models

class Contact(models.Model):
    ism = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    raqam = models.CharField(max_length=70,blank=True,null=True)
    xabar = models.TextField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return self.ism
    


class ChooseModel(models.Model):
    mashina = models.CharField(max_length=100)
    rasm = models.ImageField(upload_to='image/')
    narxi = models.CharField(max_length=50)
    soat = models.PositiveBigIntegerField()


    def __str__(self):
        return self.mashina
    
class InfoModel(models.Model):
    mashina = models.CharField(max_length=100)
    rasm = models.ImageField(upload_to='image/')
    narxi = models.CharField(max_length=50)
    tanlash = models.ForeignKey(ChooseModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.mashina
    
class BuyurtmaBerishModel(models.Model):
    mashina = models.CharField(max_length=50)
    manzildan = models.CharField(max_length=300)
    manzilga = models.CharField(max_length=300)
    email1 = models.EmailField()
    raqam1 = models.CharField(max_length=70)

    def __str__(self):
        return self.email1