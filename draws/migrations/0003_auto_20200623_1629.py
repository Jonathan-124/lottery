# Generated by Django 3.0.7 on 2020-06-23 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draws', '0002_auto_20200622_2020'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='draw',
            options={'ordering': ['-draw_date']},
        ),
        migrations.AddField(
            model_name='draw',
            name='drawn',
            field=models.BooleanField(default=True),
        ),
    ]
