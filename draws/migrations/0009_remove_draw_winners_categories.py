# Generated by Django 3.0.7 on 2020-06-30 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('draws', '0008_draw_predicted_jackpot_probability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='draw',
            name='winners_categories',
        ),
    ]