from django.db import models


# Create your models here.

class Recursive1(models.Model):
    label = models.CharField(max_length=30, blank=True)
    recursive = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.label


class Recursive2(models.Model):
    label = models.CharField(max_length=30, blank=True)
    recursive = models.ManyToManyField('self', through='Recursive2Throught', symmetrical=False)

    def __str__(self):
        return self.label


class Recursive2Throught(models.Model):
    label = models.CharField(max_length=30, blank=True)
