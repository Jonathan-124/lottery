# Generated by Django 3.0.7 on 2020-06-23 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draws', '0003_auto_20200623_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draw',
            name='drawn',
            field=models.BooleanField(default=False),
        ),
    ]
