# Generated by Django 4.2.1 on 2023-07-04 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_Ecole', '0003_alter_login_user_cin_alter_login_user_cne_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login_user',
            name='CIN',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Gestion_Ecole.enseignant'),
        ),
        migrations.AlterField(
            model_name='login_user',
            name='CNE',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Gestion_Ecole.etudiant'),
        ),
        migrations.AlterField(
            model_name='login_user',
            name='id_A',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Gestion_Ecole.ad'),
        ),
        migrations.AlterField(
            model_name='login_user',
            name='id_S',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Gestion_Ecole.secretaire'),
        ),
    ]
