from django.db import models

# Create your models here.


class ModelA(models.Model):
    name = models.CharField(max_length=20)
    size = models.PositiveIntegerField()


class ModelB(models.Model):
    model = models.ForeignKey('ModelA', on_delete=models.CASCADE)
    value = models.CharField(max_length=10, null=True)
