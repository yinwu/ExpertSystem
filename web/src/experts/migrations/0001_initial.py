# Generated by Django 3.0 on 2020-07-05 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('program', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=10000, verbose_name='评审意见')),
                ('input_date', models.DateField(auto_now=True, verbose_name='评审日期')),
                ('status', models.CharField(choices=[('ok', '已确认'), ('nok', '已排除'), ('unknow', '待确认')], default='unknow', max_length=20, verbose_name='评审状态')),
            ],
            options={
                'verbose_name': '专家评审意见',
                'verbose_name_plural': '专家评审意见',
            },
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('visible', models.BooleanField(default=True, null=True)),
                ('name', models.CharField(max_length=100, verbose_name='专家姓名')),
                ('phone', models.CharField(max_length=100, verbose_name='联系方式')),
                ('email', models.CharField(max_length=100, null=True, verbose_name='电子邮箱')),
                ('address', models.CharField(max_length=100, null=True, verbose_name='联系地址')),
                ('unit', models.CharField(max_length=100, verbose_name='工作单位')),
                ('degree', models.CharField(max_length=500, null=True, verbose_name='学历')),
                ('level', models.CharField(max_length=500, null=True, verbose_name='职务等级')),
                ('program_type', models.CharField(max_length=500, null=True, verbose_name='专业类型')),
                ('selected_program_list', models.ManyToManyField(related_name='selected', through='experts.Comments', to='program.Program')),
            ],
            options={
                'verbose_name': '专家',
                'verbose_name_plural': '专家',
            },
        ),
        migrations.AddField(
            model_name='comments',
            name='expert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experts.Expert', verbose_name='评审专家'),
        ),
        migrations.AddField(
            model_name='comments',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.Program', verbose_name='项目名称'),
        ),
    ]
