# Generated by Django 3.0 on 2020-07-04 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experts', '0003_auto_20200704_0627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expert',
            name='excluded_program_list',
        ),
    ]
