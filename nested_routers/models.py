from django.db import models


# Create your models here.

class Domain(models.Model):
    host = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.host


class Nameservers(models.Model):
    label = models.CharField(max_length=30, blank=True)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.label

