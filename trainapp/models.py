from django.db import models

class trainticket(models.Model):
    Name=models.CharField(max_length=20)
    from1= models.CharField(max_length=20, default="CityA")
    to1= models.CharField(max_length=20, default="CityA")
    train_no=models.IntegerField(default=12345,null=True)


# Create your models here.
