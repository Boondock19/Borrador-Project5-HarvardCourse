from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

class Medic(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    First_Name=models.CharField(max_length=300)
    Last_Name=models.CharField(max_length=300)
    Clinic=models.CharField(max_length=300)
    age=models.IntegerField()
    rate=models.FloatField(blank=True)
    def __str__(self):
        return f"This is Dr(a) {self.Last_Name} from the clinic {self.Clinic}"

class Normal_User(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    First_Name=models.CharField(max_length=300)
    Last_Name=models.CharField(max_length=300)
    age=models.IntegerField()

    def __str__(self):
        return f"This is User {self.First_Name} {self.Last_Name} "
