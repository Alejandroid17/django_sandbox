from django.db import models
from dynamic.fields import DynamicField


# Create your models here.

class ModelA(models.Model):
    filename = models.CharField(max_length=30, blank=True)
    binary = DynamicField(blank=True)
    model_b = models.ForeignKey('ModelB', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.filename


class ModelB(models.Model):
    label = models.CharField(max_length=30, blank=True)
    binary = models.FileField(upload_to='uploads/', blank=True)

    def __str__(self):
        return self.label


