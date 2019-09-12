from django.db import models

class Debtors(models.Model):
    name = models.CharField(max_length=20)
    individual_id = models.CharField(max_length=20)
    gender=models.CharField(max_length=8, default='Male')
    age=models.IntegerField(default=0)
    phone = models.IntegerField()
    email=models.EmailField()
    Address = models.TextField()
    debt_amount=models.IntegerField()
    photo=models.ImageField(default='default.jpeg')
    case_details=models.TextField()
    document=models.FileField(blank=True)

    def __str__(self):
        return self.name

class Creditors(models.Model):
    name = models.CharField(max_length=20)
    individual_id = models.CharField(max_length=20)
    gender=models.CharField(max_length=8, default='Male')
    age=models.IntegerField(default=0)
    phone = models.IntegerField()
    email=models.EmailField()
    Address = models.TextField()
    photo=models.ImageField(default='default.jpeg')