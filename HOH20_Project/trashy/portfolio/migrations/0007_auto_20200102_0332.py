# Generated by Django 3.0.1 on 2020-01-02 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20200102_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(verbose_name='date published'),
        ),
    ]
