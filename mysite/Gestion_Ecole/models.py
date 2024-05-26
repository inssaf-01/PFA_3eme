from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError




    
class Enseignant(models.Model):
    CIN = models.CharField(max_length=40, primary_key=True, null=False)
    nom = models.CharField(max_length=60)
    prenom = models.CharField(max_length=60)
    titre_prof = models.CharField(max_length=60, null=True, blank=True)
    tel = models.CharField(max_length=20)
    email = models.EmailField()
    salaire = models.DecimalField(max_digits=8, decimal_places=2)
    cv = models.FileField(upload_to="cv", default=None)

    
    def __str__(self):
        return f"Enseignant CIN: {self.CIN} - Nom : {self.nom}"

    class Meta:
        ordering = ['nom']


class EnseignantRecrutement(models.Model):
    CIN = models.CharField(max_length=40, primary_key=True, null=False)
    nom = models.CharField(max_length=60)
    prenom = models.CharField(max_length=60)
    titre_prof = models.CharField(max_length=60, null=True, blank=True)
    tel = models.CharField(max_length=20)
    email = models.EmailField()
    salaire = models.DecimalField(max_digits=8, decimal_places=2)
    cv = models.FileField(upload_to="cv", default=None)

    # comment ca s'affiche sur le la liste d'admin
    def __str__(self):
        return f"Enseignant CIN: {self.CIN} - Nom : {self.nom}"

    class Meta:
        ordering = ['nom']
    


class Option(models.Model):
    num_Option = models.BigAutoField(primary_key=True)
    nom_Option = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return str(self.nom_Option)

    class Meta:
        ordering = ['nom_Option']




class Module(models.Model):
    num_Module =models.BigAutoField(primary_key=True)
    nom_Module = models.CharField(max_length=60)
    code_Option = models.ForeignKey(Option, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_Module

    class Meta:
        ordering = ['nom_Module']



class Etudiant(models.Model):
    x = [('H', 'Homme'), ('F', 'Femme')]
    p = [('Bac +2', 'Bac +2'), ('Bac +3', 'Bac +3'), ('Bac +5', 'Bac +5')]
    CNE = models.CharField(max_length=40, primary_key=True)
    nom = models.CharField(max_length=60)
    prenom = models.CharField(max_length=60)
    sexe = models.CharField(max_length=20, choices=x)
    tel = models.CharField(max_length=20)
    email = models.CharField(max_length=80)
    adresse = models.CharField(max_length=100)
    annee_Bac = models.IntegerField()
    parcours = models.CharField(max_length=20, choices=p)
    code_Option = models.ForeignKey(Option, on_delete=models.CASCADE)
  
    
    def delete(self):
        super(Etudiant, self).delete()

    def __str__(self):
        return self.CNE

    class Meta:
        ordering = ['CNE']



class EtudiantInscription(models.Model):
    x = [('H', 'Homme'), ('F', 'Femme')]
    p = [('2', 'Bac +2'), ('3', 'Bac +3'), ('5', 'Bac +5')]
    CNE = models.CharField(max_length=40, primary_key=True, null=False)
    nom = models.CharField(max_length=60)
    prenom = models.CharField(max_length=60)
    sexe = models.CharField(max_length=20, choices=x)
    tel = models.CharField(max_length=20)
    email = models.CharField(max_length=80)
    adresse = models.CharField(max_length=100)
    annee_Bac = models.IntegerField()
    parcours = models.CharField(max_length=20, choices=p)
    code_Option = models.ForeignKey(Option, on_delete=models.CASCADE)

    
    def __str__(self):
        option_str = str(self.code_Option) if self.code_Option else ''
        return f"{self.CNE} - {self.nom} {self.prenom} ({option_str})"


class NoteEtudiant(models.Model):
    r = [('R', 'Rattrapage'), ('V', 'validé'), ('X', 'échec')]
    id_Note = models.BigAutoField(primary_key=True)
    CNE = models.ForeignKey(Etudiant, on_delete=models.CASCADE, null=False)
    num_Module = models.ForeignKey(Module, on_delete=models.CASCADE, null=False)
    note_Module = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(20)])
    resultat = models.CharField(max_length=1, choices=r)

    class Meta:
        ordering = ['CNE']

    def __str__(self):
        return f"Note ID: {self.id_Note} - Étudiant: {self.CNE}"
    
    def save(self, *args, **kwargs):
        if self.note_Module >= 10:
            self.resultat = 'V'  # Validé
        elif 5 <= self.note_Module < 10:
            self.resultat = 'R'  # Rattrapage
        else:
            self.resultat = 'X'  # Échec
        super(NoteEtudiant, self).save(*args, **kwargs)


class Cours(models.Model):
    num_Cours = models.BigAutoField(primary_key=True)
    nom_Cours = models.CharField(max_length=60)
    masse_horaire = models.PositiveIntegerField()
    num_Enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    num_Module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_Cours

    class Meta: # changer le nom dans la liste chez l admin
        ordering = ['nom_Cours']

class Salle(models.Model):
    nom_Salle = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.nom_Salle

    class Meta:
        ordering = ['nom_Salle']


class Absence(models.Model):
    a = [('E', 'Excusé(e)'), ('J', 'justifiée'), ('N', 'Non justifié')]
    num_Abs = models.BigAutoField(primary_key=True)
    etat_abs = models.CharField(max_length=1, choices=a)
    date_abs = models.DateTimeField()
    num_Cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    CNE = models.ForeignKey(Etudiant, on_delete=models.CASCADE)

    def __str__(self):
        return self.date_abs

    class Meta:
        ordering = ['date_abs']

class Horaire(models.Model):
    id_Horaire = models.BigAutoField(primary_key=True)
    num_Salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    CIN = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    num_Cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    date_Debut_C = models.DateTimeField()
    date_Fin_C = models.DateTimeField()

    class Meta:
        ordering = ['date_Debut_C']
    
    def __str__(self):
        return f"{self.date_Debut_C.date()} - {self.num_Cours} - {self.CIN}"
    def get_queryset(self):
    # Obtenez la date et l'heure actuelles
       current_date = timezone.now().date()

    # Filtrer les horaires à partir d'aujourd'hui
       queryset = Horaire.objects.filter(date_Debut_C__gte=current_date)
       return queryset

    def clean(self):
        # Vérifier si un autre horaire existe déjà avec le même enseignant et une date de chevauchement
        horaires_existantes = Horaire.objects.filter(CIN=self.CIN, date_Debut_C__lt=self.date_Fin_C, date_Fin_C__gt=self.date_Debut_C)
        if horaires_existantes.exists():
            raise ValidationError('Cet enseignant a déjà un cours planifié à cette heure.')
        
        # Vérifier si la date de début est supérieure ou égale à la date actuelle
        current_date = timezone.now()
        if self.date_Debut_C < current_date:
            raise ValidationError('La date du début de cours est déjà passée.')
        
        # Vérifier si la salle est déjà occupée par un autre cours
        horaires_salle = Horaire.objects.filter(num_Salle=self.num_Salle, date_Debut_C__lt=self.date_Fin_C, date_Fin_C__gt=self.date_Debut_C)
        if horaires_salle.exists():
            raise ValidationError('La salle est déjà occupée pendant cette période.')
        
        # Vérifier si la date de début et de fin sont dans le même jour
        if self.date_Debut_C.date() != self.date_Fin_C.date():
            raise ValidationError('La date de début et de fin doivent être dans le même jour.')
        
        # Vérifier si la date de début est antérieure à la date de fin
        if self.date_Debut_C >= self.date_Fin_C:
            raise ValidationError('La date de début de cours doit être antérieure à la date de fin de cours.')
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    
@receiver(pre_save, sender=Horaire)
def check_horaire_dates(sender, instance, **kwargs):
    current_date = timezone.now().date()
    if instance.date_Debut_C.date() < current_date:
        raise ValidationError('La date du début de cours est déjà passée.')

class Secretaire(models.Model):
    id_S = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=60)

    def __str__(self):
        return str(self.id_S)
    
class Ad(models.Model):
    id_A = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=60)

    def __str__(self):
        return str(self.id_A)

class log(models.Model):
    username = models.CharField(max_length=40, primary_key=True)
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.username
 

class login_user(models.Model):
    id_log = models.BigAutoField(primary_key=True)
    username = models.OneToOneField(log, on_delete=models.CASCADE)
    CNE = models.ForeignKey(Etudiant, on_delete=models.CASCADE, null=True, blank=True)
    CIN = models.ForeignKey(Enseignant, on_delete=models.CASCADE, null=True, blank=True)
    id_S = models.ForeignKey(Secretaire, on_delete=models.CASCADE, null=True, blank=True)
    id_A = models.ForeignKey(Ad, on_delete=models.CASCADE, null=True, blank=True)
    is_adm = models.BooleanField(default=False)
    is_etud = models.BooleanField(default=True)
    is_ens = models.BooleanField(default=False)
    is_secr = models.BooleanField(default=False)
    def __str__(self):
        return str(self.username)

@receiver(pre_save, sender=login_user)
def update_user_attributes(sender, instance, **kwargs):
    if instance.CNE:
        instance.CIN = None
        instance.id_A = None
        instance.id_S = None
        instance.is_adm = False
        instance.is_ens = False
        instance.is_secr = False
        instance.is_etud = True
    elif instance.CIN:
        instance.CNE = None
        instance.id_A = None
        instance.id_S = None
        instance.is_adm = False
        instance.is_ens = True
        instance.is_secr = False
        instance.is_etud = False
    elif instance.id_A:
        instance.CNE = None
        instance.CIN = None
        instance.id_S = None
        instance.is_adm = True
        instance.is_ens = False
        instance.is_secr = False
        instance.is_etud = False
    elif instance.id_S:
        instance.CNE = None
        instance.CIN = None
        instance.id_A = None
        instance.is_adm = False
        instance.is_ens = False
        instance.is_secr = True
        instance.is_etud = False
    else:
        instance.is_adm = False
        instance.is_ens = False
        instance.is_secr = False
        instance.is_etud = False



    
    



    

    