from django.db import models
class Employeemodel(models.Model):
    Name=models.CharField(max_length=30)
    Age=models.IntegerField()
    Contact=models.IntegerField()
    Email=models.EmailField()
    Username=models.CharField(unique=True,max_length=50)
    Password=models.CharField(max_length=10)
    gender=models.CharField(max_length=20)