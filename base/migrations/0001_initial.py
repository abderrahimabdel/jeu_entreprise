# Generated by Django 4.0.6 on 2022-09-29 12:55

import datetime
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choix', models.CharField(max_length=150, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=200, null=True, unique=True)),
                ('Adresse', models.CharField(max_length=200, null=True)),
                ('cp', models.CharField(max_length=200, null=True)),
                ('ville', models.CharField(max_length=200, null=True)),
                ('remise', models.CharField(max_length=200, null=True)),
                ('divers', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=200, null=True, unique=True)),
                ('Adresse', models.CharField(max_length=200, null=True)),
                ('cp', models.CharField(max_length=200, null=True)),
                ('ville', models.CharField(max_length=200, null=True)),
                ('remise', models.CharField(max_length=200, null=True)),
                ('divers', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200, null=True, unique=True)),
                ('type', models.CharField(max_length=200, null=True)),
                ('temps_en_secondes', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GestioncM',
            fields=[
                ('mission_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.mission')),
                ('enonce', models.TextField()),
                ('nbre_ref', models.IntegerField(default=0, null=True)),
                ('min_qte', models.IntegerField(default=0, null=True)),
                ('max_qte', models.IntegerField(default=0, null=True)),
                ('points', models.IntegerField(default=0, null=True)),
            ],
            bases=('base.mission',),
        ),
        migrations.CreateModel(
            name='VEntrepriseM',
            fields=[
                ('mission_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.mission')),
                ('intitule', models.CharField(max_length=200, null=True)),
                ('pointsA', models.IntegerField(default=0, null=True)),
                ('pointsR', models.IntegerField(default=0, null=True)),
            ],
            bases=('base.mission',),
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=200, null=True, unique=True)),
                ('prix_achatHT', models.CharField(max_length=200, null=True)),
                ('prix_venteHT', models.CharField(max_length=200, null=True)),
                ('prix_venteTTC', models.CharField(max_length=200, null=True)),
                ('TVA', models.CharField(max_length=200, null=True)),
                ('stock', models.CharField(max_length=200, null=True)),
                ('fournisseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.fournisseur')),
            ],
        ),
        migrations.CreateModel(
            name='Mission_Joueur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temps_restant', models.IntegerField(null=True)),
                ('enonce', models.TextField(default='', null=True)),
                ('reponse', models.CharField(default='', max_length=80, null=True)),
                ('debut', models.DateTimeField(default=datetime.datetime(2022, 9, 29, 12, 55, 47, 233139, tzinfo=utc))),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.mission')),
            ],
        ),
        migrations.CreateModel(
            name='Joueur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=200, null=True, unique=True)),
                ('password1', models.CharField(max_length=80, null=True)),
                ('password2', models.CharField(max_length=80, null=True)),
                ('points', models.IntegerField(null=True)),
                ('points_depart', models.IntegerField(null=True)),
                ('nombre_de_missions', models.IntegerField(default=0, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('mission_courante', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.mission_joueur')),
                ('missions_passe', models.ManyToManyField(default='', related_name='missions_passe', to='base.mission_joueur')),
                ('type_de_missions', models.ManyToManyField(related_name='type_de_missions', to='base.choix')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='QuizzM',
            fields=[
                ('mission_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.mission')),
                ('question', models.CharField(max_length=200, null=True)),
                ('op1', models.CharField(max_length=200, null=True)),
                ('op2', models.CharField(max_length=200, null=True)),
                ('op3', models.CharField(max_length=200, null=True)),
                ('op4', models.CharField(max_length=200, null=True)),
                ('rep', models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], default='a', max_length=6)),
                ('points', models.IntegerField(null=True)),
                ('type_de_quizz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.choix')),
            ],
            bases=('base.mission',),
        ),
    ]
