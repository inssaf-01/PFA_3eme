from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import EtudiantInscription
from .models import EnseignantRecrutement
from .models import Etudiant
from .models import Enseignant
from .models import Option
from .models import log






class EtudiantForm(forms.ModelForm):
    class Meta:
        model = EtudiantInscription 
        fields = '__all__'
        widget= {
            'email':forms.EmailInput(attrs={'class':"form-control"}),
            'nom':forms.TextInput(attrs={'class':"form-control"}),
            'prenom':forms.TextInput(attrs={'class':"form-control"}),
            'adresse':forms.TextInput(attrs={'class':"form-control"}),
        }
class EtudiantA(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = '__all__'
        widget= {
            'email':forms.EmailInput(attrs={'class':"form-control"}),
            'nom':forms.TextInput(attrs={'class':"form-control"}),
            'prenom':forms.TextInput(attrs={'class':"form-control"}),
            'adresse':forms.TextInput(attrs={'class':"form-control"}),
        }
        widgets = {
            #'code_Option': forms.Select(choices=Option.objects.values_list('id', 'nom_Option'))
        }       

class EtudiantA1(forms.ModelForm):
    class Meta:
        model = Etudiant
      
        fields = ['nom','prenom','annee_Bac']
        
            
               

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = EnseignantRecrutement 
        fields = '__all__'       

class EnseignantA(forms.ModelForm):
    class Meta:
        model = Enseignant 
        fields = '__all__'  
    
class EnseignantA1(forms.ModelForm):
    class Meta:
        model = Enseignant 
        fields = '__all__'  


class OptionA(forms.ModelForm):
    class Meta:
        model = Option
        exclude = ["num_Option"] 

class UserForm(forms.ModelForm):
    class Meta:
        model = log
        fields = '__all__' 