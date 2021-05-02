from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.ForeignKey(User, verbose_name='User', blank=True, on_delete = models.CASCADE)
    name = models.CharField(verbose_name='Name', max_length=50)
    points = models.IntegerField(verbose_name='Points')

    def __str__ (self):
        return f'{self.id} {self.name} {self.points}'

class Operations(models.Model):
    client = models.ForeignKey(Client, verbose_name='Client', on_delete = models.CASCADE)
    descript = models.CharField(verbose_name='Descript', max_length=100, null=True)
    act = models.BooleanField(verbose_name='Act') # True = add point, False = subtract points
    points = models.IntegerField(verbose_name='Points')
    date = models.DateTimeField(verbose_name='Date', auto_now_add=True)