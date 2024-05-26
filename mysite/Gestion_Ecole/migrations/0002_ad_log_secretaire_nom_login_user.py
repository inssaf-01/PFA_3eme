# Generated by Django 4.2.1 on 2023-07-04 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_Ecole', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id_A', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='log',
            fields=[
                ('username', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='secretaire',
            name='nom',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='login_user',
            fields=[
                ('id_log', models.BigAutoField(primary_key=True, serialize=False)),
                ('is_adm', models.BooleanField(default=False)),
                ('is_etud', models.BooleanField(default=True)),
                ('is_ens', models.BooleanField(default=False)),
                ('is_secr', models.BooleanField(default=False)),
                ('CIN', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Gestion_Ecole.enseignant')),
                ('CNE', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Gestion_Ecole.etudiant')),
                ('id_A', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Gestion_Ecole.ad')),
                ('id_S', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Gestion_Ecole.secretaire')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Gestion_Ecole.log')),
            ],
        ),
    ]