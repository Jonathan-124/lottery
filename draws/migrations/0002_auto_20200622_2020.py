# Generated by Django 3.0.7 on 2020-06-23 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
        ('draws', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draw',
            name='game',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='draws', to='games.Game'),
        ),
    ]
