from django.db import models
from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class medicine(models.Model):
    name =models.CharField(max_length=50)
    cost =models.DecimalField(max_digits=10,decimal_places=2,null=True)
    shop =models.CharField(max_length=50)
    adress =models.CharField(max_length=50)


    def __str__(self):
        return self.name
    
