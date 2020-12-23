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
    sum_of_rates=models.IntegerField(default=0)
    num_of_rates=models.IntegerField(default=0)
    def __str__(self):
        return f"This is Dr(a) {self.Last_Name} from the clinic {self.Clinic}"
    
    def promedio(self,New_rate):
        if self.num_of_rates==0:
            pass
        self.sum_of_rates=self.sum_of_rates+New_rate
        self.num_of_rates=self.num_of_rates+1
        self.rate=self.sum_of_rates/self.num_of_rates

class Normal_User(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    First_Name=models.CharField(max_length=300)
    Last_Name=models.CharField(max_length=300)
    age=models.IntegerField()

    def __str__(self):
        return f"This is User {self.First_Name} {self.Last_Name} "

class Medic_Article(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    medic=models.ForeignKey(Medic,on_delete=models.CASCADE)
    title=models.CharField(max_length=60)
    content=models.CharField(max_length=2000)

    def __str__(self):
        return f"this is Article from {self.medic}"

class Article_comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    article=models.ForeignKey(Medic_Article,on_delete=models.CASCADE)
    comment=models.CharField(max_length=300)
    Date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"This is from {self.user} and article {self.article}"