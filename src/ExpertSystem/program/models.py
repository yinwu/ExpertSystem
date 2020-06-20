from django.db import models

# Create your models here.


class Program(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    responser = models.CharField(max_length=100)
    desp = models.CharField(max_length=1000)
    #excluded_experts = models.ManyToManyField(Expert)
