from django.db import models

# Create your models here.

#from experts.models import Expert


class Program(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    responser = models.CharField(max_length=100)
    desp = models.CharField(max_length=1000)
    #excluded_experts = models.ManyToManyField(Expert)


class Comments(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    author = models.ForeignKey(Expert, on_delete=models.CASCADE)
    content = models.CharField(max_length=10000)
    input_date = models.DateField()