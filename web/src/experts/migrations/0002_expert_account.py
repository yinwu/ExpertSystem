# Generated by Django 3.0 on 2020-07-10 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import experts.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('experts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert',
            name='account',
            field=models.ForeignKey(default=experts.models.get_default_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='账户'),
        ),
    ]