from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

import logging
# importer les models et les forms
from .models import Etudiant,EtudiantInscription
from .models import Enseignant,EnseignantRecrutement
from .models import Option
from .models import Module
from .models import Cours
from .models import Salle
from .models import Absence
from .models import Horaire
from .models import NoteEtudiant
from .models import Secretaire
from .models import Ad
from .models import log
from .models import login_user

# from .models import User
from .forms import EnseignantForm,EnseignantA,EnseignantA1
from .forms import EtudiantForm,EtudiantA,EtudiantA1
from .forms import OptionA,UserForm
# from .forms import UserForm




# Create your views here.

# les pages
def index(request):
    return render(request, 'Gestion_Ecole/index.html')





# Admin 

# utilisateurs 
def Etudiants(request, CNE):
    try:
        etudiant = Etudiant.objects.get(CNE=CNE)
        return render(request, 'Gestion_Ecole/Etudiants.html', {'et': etudiant,'CNE': CNE})
    except Etudiant.DoesNotExist:
        return render(request, 'Gestion_Ecole/Etudiants.html', {'message': 'Etudiant non trouvé'})

def Enseignants(request, CIN):
    try:
        enseignant = Enseignant.objects.get(CIN=CIN)
        return render(request, 'Gestion_Ecole/Enseignants.html', {'e': enseignant, 'CIN': CIN})
    except Enseignant.DoesNotExist:
        return render(request, 'Gestion_Ecole/Enseignants.html', {'message': 'Enseignant non trouvé'})
    
def Adm(request):
    return render(request,'Gestion_Ecole/Adm.html', {'etudiants': Etudiant.objects.all()})
def Secretaires(request):
    return render(request, 'Gestion_Ecole/Secretaires.html')
# Etudiant


     # Tous les etudiants

def Etud(request):
    return render(request, 'Gestion_Ecole/Etud.html', {'etudiant': Etudiant.objects.all()})



    # Un seul etudiant 
def Etud_info(request):
     # Récupérer la valeur de l'attribut à partir du formulaire
    return render(request, 'Gestion_Ecole/Etud_info.html', {'et': Etudiant.objects.get(CNE="AA70")})   
    # Ajout un etudiant INSCRIPTION
def Ajout_Etud(request):
    if request.method == 'POST':
       dataform = EtudiantForm(request.POST)
       # Verifier la validite des donnees entrees
       if dataform.is_valid():
          # Enregistrer données
           dataform.save()   

    return render(request, 'Gestion_Ecole/Ajout_Etud.html',{'etf':EtudiantForm})

    # Ajout un etudiant par admin
def Ajout_Etud_admin(request):
    if request.method == 'POST':
       dataform = EtudiantA(request.POST)
       # Verifier la validite des donnees entrees
       if dataform.is_valid():
          # Enregistrer données
          dataform.save()
    return render(request, 'Gestion_Ecole/Ajout_Etud_admin.html',{'etf':EtudiantA})

    # Acceptation etudiant

def etudiant_inscription_list(request):
    etudiant_inscriptions = EtudiantInscription.objects.all()
    context = {'etudiant_inscriptions': etudiant_inscriptions}
    return render(request, 'Gestion_Ecole/etudiant_inscription_list.html', context)

def Acceptation_etudiant(request):
    if request.method == 'POST':
        cne = request.POST.get('cne')
        etudiant = Etudiant()
        etudiant_inscription = get_object_or_404(EtudiantInscription, CNE=cne)

        # Create a new instance of Etudiant and copy the fields
        etudiant = Etudiant.objects.create(
            CNE=etudiant_inscription.CNE,
            nom=etudiant_inscription.nom,
            prenom=etudiant_inscription.prenom,
            sexe=etudiant_inscription.sexe,
            tel=etudiant_inscription.tel,
            email=etudiant_inscription.email,
            adresse=etudiant_inscription.adresse,
            annee_Bac=etudiant_inscription.annee_Bac,
            parcours=etudiant_inscription.parcours,
            code_Option=etudiant_inscription.code_Option
        )

        # Delete the transferred instance from EtudiantInscription
        etudiant_inscription.delete()

    return redirect('etudiant_inscription_list')  # Redirect to the original list view

    # Suppression d un etudiant
def Supp_Etud(request):
    if request.method == 'POST':
        id = request.POST.get('cne')  # Récupérer la valeur de l'attribut à partir du formulaire
        try:
            etudiant = Etudiant.objects.get(CNE=id)  # Rechercher l'étudiant correspondant à l'attribut
        except:  
            return render(request, 'Gestion_Ecole/Supp_Etud.html', { 'message':'Aucun Etudiant trouvé'})

        if etudiant is not None :
            etudiant.delete()
    
            return render(request, 'Gestion_Ecole/Supp_Etud.html', {'etudiant': etudiant , 'message':'Supprimé avec succès'})
        
    return render(request, 'Gestion_Ecole/Supp_Etud.html')

    # Modification d'un etudiant
def Modif_Etud(request):
        # if request.method == 'POST':
        #     id = request.POST.get('cne')
        #     et = Etudiant.objects.get(CNE=id)
        #     form = EtudiantA(instance = et)
        #     opt=Option.objects.all()
        #     x = [('H', 'Homme'), ('F', 'Femme')]
        #     
        #       # on pré-remplir le formulaire avec un groupe existant
        #     return render(request,'Gestion_Ecole/Modif_Etud2.html',{'form1': et,'form':EtudiantA1,'opt':opt,'p':par,'se':x})
            
        # return render(request,'Gestion_Ecole/Modif_Etud.html',{'form': EtudiantA})     
        if request.method == 'POST':
            id = request.POST.get('cne')
            try:
                et = Etudiant.objects.get(CNE=id)
            except:
            
                return render(request, 'Gestion_Ecole/Modif_Etud.html', { 'message':'Aucun Etudiant trouve'})

            if et is not None :
               et = Etudiant.objects.get(CNE=id)
               form = EtudiantA(instance = et)
               opt=Option.objects.all()
               x = [('H', 'Homme'), ('F', 'Femme')]
               se = x
               par =[('Bac +2', 'Bac +2'), ('Bac +3', 'Bac +3'), ('Bac +5', 'Bac +5')]
               p= par
    
            return render(request, 'Gestion_Ecole/Modif_Etud2.html',{'form1': et,'form':EtudiantA1,'opt':opt,'p':par,'se':x ,'message':'Modifie avec succes'})
        
            
    # Si la méthode HTTP n'est pas POST, cela signifie que la page vient d'être chargée, donc pas de suppression
        return render(request, 'Gestion_Ecole/Modif_Etud.html')   




def modifetud3(request, myid):
    etud = Etudiant.objects.get(CNE=myid)
    opt=Option.objects.all()
    if request.method == 'POST':
        etud.nom = request.POST.get('n')
        etud.prenom = request.POST.get('pre')
        etud.sexe = request.POST.get('s')
        etud.tel = request.POST.get('t')
        etud.email = request.POST.get('e')
        etud.adresse = request.POST.get('ad')
        etud.annee_Bac = request.POST.get('anb')
        etud.parcours = request.POST.get('p')
        #etud.code_Option = request.POST.get('cd')
        #option_instance = request.POST(Option, value=request.POST.get('cd'))
        #etud.code_Option = option_instance
        # option_id = request.POST.get('code_Option')
        # option_instance = Option.objects.get(num_Option=option_id)
        # etud.code_Option = option_instance
        selected_option_value = request.POST.get('cd')

    
        option_instance = get_object_or_404(Option, nom_Option=selected_option_value)
        etud.code_Option = option_instance
        etud.save()
        
        # Redirect to a success page or perform further actions
        #return redirect('success-page')
        
        return redirect(Modif_Etud)
    else:
        form = EtudiantA(instance=etud)
    
    return render(request, 'Gestion_Ecole/Modif_Etud.html', {'form': form,'opt':opt})



    
# Enseigant
def Ens_info(request, myid):
    return render(request, 'Gestion_Ecole/Ens_info.html', {'e': Enseignant.objects.get(CIN=myid)})    

def Ens_infos(request):
    return render(request, 'Gestion_Ecole/Ens_infos.html', {'ens': Enseignant.objects.all()})  
    
def Ens(request):
    if request.method == 'POST':
       data = EnseignantForm(request.POST, request.FILES)
       logger = logging.getLogger("mylogger")
       logger.info(data)
       if data.is_valid():
          data.save()
    return render(request, 'Gestion_Ecole/Ens.html',{'en':EnseignantForm})

def Ajout_Ens(request):
    if request.method == 'POST':
       data = EnseignantA(request.POST, request.FILES)
       if data.is_valid():
            data.save()
    return render(request, 'Gestion_Ecole/Ajout_Ens.html', {'en':EnseignantA})



def Supp_Ens(request):
    if request.method == 'POST':
        id = request.POST.get('cin')  # Récupérer la valeur de l'attribut à partir du formulaire
        enseignant = Enseignant.objects.get(CIN=id)  # Rechercher l'étudiant correspondant à l'attribut
        enseignant.delete()  # Supprimer l'étudiant de la base de données
    return render(request, 'Gestion_Ecole/Supp_Ens.html')


# def Supp_Ens(request):
#     if request.method == 'POST':
#         id = request.POST.get('cin')
#         enseignant = Enseignant.objects.get(CIN=id)
#         enseignant.delete() 
#         return render(request, 'Gestion_Ecole/Supp_Ens.html', {'enseignant': enseignant})
    
#     # Si la méthode HTTP n'est pas POST, cela signifie que la page vient d'être chargée, donc pas de suppression
#     return render(request, 'Gestion_Ecole/Supp_Ens.html')

def Supp_Ens(request):
    if request.method == 'POST':
        id = request.POST.get('cin')
        try:
            enseignant = Enseignant.objects.get(CIN=id)
        except:
            
            return render(request, 'Gestion_Ecole/Supp_Ens.html', { 'message':'Aucun Enseignant trouve'})

        if enseignant is not None :
            enseignant.delete()
    
            return render(request, 'Gestion_Ecole/Supp_Ens.html', {'enseignant': enseignant , 'message':'Supprime avec succes'})
        
            
    # Si la méthode HTTP n'est pas POST, cela signifie que la page vient d'être chargée, donc pas de suppression
    return render(request, 'Gestion_Ecole/Supp_Ens.html')

    # Modification d'un enseignant
       
        

def Modif_Ens(request):
        if request.method == 'POST':
            id = request.POST.get('cin')
            en = Enseignant.objects.get(CIN=id)
            form = EnseignantA(instance = en)
            # on pré-remplir le formulaire avec un groupe existant
            return render(request,'Gestion_Ecole/Modif_Ens2.html',{'form1': en,'form':EnseignantA1})
            
        return render(request,'Gestion_Ecole/Modif_Ens.html',{'form': EnseignantA})        



def modifens3(request, myid):
    ens = Enseignant.objects.get(CIN=myid)
    if request.method == 'POST':
        ens.nom = request.POST.get('n')
        ens.prenom = request.POST.get('pre')
        ens.titre_prof = request.POST.get('ti')
        ens.tel = request.POST.get('te')
        ens.email = request.POST.get('e')
        ens.salaire = request.POST.get('s')
        if 'cv' in request.FILES:
            new_cv = request.FILES['cv']
            # Supprimer l'ancien fichier si nécessaire
            if ens.cv:
                ens.cv.delete()
            ens.cv = new_cv
        ens.save()
        # Redirect to a success page or perform further actions
        #return redirect('success-page')
        
        return redirect('Modif_Ens')
    else:
        form = EnseignantA(instance=ens)
    
    return render(request, 'Gestion_Ecole/Modif_Ens.html', {'form': form})

# def Horaire_ens(request, cin):
#     return render(request,'Gestion_Ecole/Horaire_T.html', {'horaires': Horaire.objects.get(CIN=cin)})

    # Recrutement Enseignant 
def enseignant_recrutement_list(request):
    enseignant_recrutements = EnseignantRecrutement.objects.all()
    context = {'enseignant_recrutements': enseignant_recrutements}
    return render(request, 'Gestion_Ecole/enseignant_recrutement_list.html', context)

def Acceptation_enseignant(request):
    if request.method == 'POST':
        cin = request.POST.get('cin')
        enseignant_recrutement = EnseignantRecrutement.objects.get(CIN=cin)

        # Create a new instance of Etudiant and copy the fields
        enseignant = Enseignant()
        enseignant.CIN = enseignant_recrutement.CIN
        enseignant.nom = enseignant_recrutement.nom
        enseignant.prenom = enseignant_recrutement.prenom
        enseignant.titre_prof = enseignant_recrutement.titre_prof
        enseignant.tel = enseignant_recrutement.tel
        enseignant.email = enseignant_recrutement.email
        enseignant.salaire = enseignant_recrutement.salaire
        if 'cv' in request.FILES:
            enseignant.cv = request.FILES['cv']
           
        enseignant.save()

        # Delete the transferred instance from EtudiantInscription
        enseignant_recrutement.delete()

    return redirect('enseignant_recrutement_list')  # Redirect to the original list view

def Ens_private(request):
    return render(request, 'Gestion_Ecole/Ens_private.html', {'ens': Enseignant.objects.all()})

# Option 
def Ajout_Filiere(request):
    if request.method == 'POST':
       data = OptionA(request.POST)
       if data.is_valid():
            data.save()
    return render(request, 'Gestion_Ecole/Ajout_Filiere.html',{'opt':OptionA})




def logg(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        passw = request.POST.get('password')
        pers = get_object_or_404(login_user, username=user)
        us = get_object_or_404(log, username=user)
        
        if us.password == passw:
            if pers.is_adm:
                return redirect('Adm')
            elif pers.is_etud:
                return redirect('Etudiants', CNE=pers.CNE)
            elif pers.is_secr:
                return redirect('Secretaires')
            elif pers.is_ens:
                return redirect('Enseignants',CIN=pers.CIN)
            
        else:
            return render(request, 'Gestion_Ecole/logg.html', {'message': 'Mot de passe incorrect'})
    
    return render(request, 'Gestion_Ecole/logg.html')

def Enreg(request):  
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('logg')
    return render(request, 'Gestion_Ecole/Enreg.html', {'form': form })

def Aff_etud_sec(request):   
    return render(request,'Gestion_Ecole/Aff_etud_sec.html', {'etudiant': Etudiant.objects.all()})    
            
def Aff_etud_admin(request):  
    return render(request,'Gestion_Ecole/Aff_etud_sec.html', {'etudiant': Etudiant.objects.all()})

def Aff_ens_sec(request):
    return render(request,'Gestion_Ecole/Aff_ens_sec.html', {'ens': Enseignant.objects.all()})

def Aff_ens_admin(request):
    return render(request,'Gestion_Ecole/Aff_ens_admin.html', {'ens': Enseignant.objects.all()})

def Horaire_T(request):
    return render(request,'Gestion_Ecole/Horaire_T.html', {'horaires': Horaire.objects.all()})

def Note_Etud(request, CNE):
    notes = NoteEtudiant.objects.filter(CNE=CNE)
    return render(request, 'Gestion_Ecole/Note_Etud.html', {'notes': notes,'CNE': CNE})

def Etud_cours_m(request, CNE):
    etudiant = Etudiant.objects.get(CNE=CNE)
    modules = Module.objects.filter(code_Option=etudiant.code_Option)
    return render(request, 'Gestion_Ecole/Etud_cours_m.html', {'etudiant': etudiant, 'modules': modules,'CNE': CNE})


