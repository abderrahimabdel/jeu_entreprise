# Generated by Django 4.0.6 on 2022-09-18 20:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_mission_joueur_debut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission_joueur',
            name='debut',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 18, 22, 34, 59, 642776)),
        ),
        migrations.AlterField(
            model_name='quizzm',
            name='type_de_quizz',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='base.choix'),
        ),
    ]