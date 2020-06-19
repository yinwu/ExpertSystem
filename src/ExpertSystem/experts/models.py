from django.db import models

# Create your models here.

from program.models import Program


class Expert(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    desp = models.CharField(max_length=500)
    selected_program_list = models.ManyToManyField(Program, related_name="selected")
    excluded_program_list = models.ManyToManyField(Program, related_name="excluded")



class Comments(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    author = models.ForeignKey(Expert, on_delete=models.CASCADE)
    content = models.CharField(max_length=10000)
    input_date = models.DateField()