# Generated by Django 3.2.7 on 2021-12-30 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20211217_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='demo_link',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Link demo'),
        ),
        migrations.AlterField(
            model_name='project',
            name='source_link',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Source code'),
        ),
    ]
