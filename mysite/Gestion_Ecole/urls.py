from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

# url /
urlpatterns = [
    path('', views.index, name='index'),
    # General  
    path('logg', views.logg, name='logg'),
    path('Enreg', views.Enreg, name='Enreg'),
    # admin
    path('Adm', views.Adm, name='Adm'),
    # etudiant
    path('Etud', views.Etud, name='Etud'),
    path('Etudiants/', views.Etudiants, name='Etudiants'),
    path('Etud_info', views.Etud_info, name='Etud_info'),
    path('Ajout_Etud', views.Ajout_Etud, name='Ajout_Etud'),
    path('Ajout_Etud_admin', views.Ajout_Etud_admin, name='Ajout_Etud_admin'),
    path('Modif_Etud', views.Modif_Etud, name='Modif_Etud'),
    path('modifetud3/<str:myid>', views.modifetud3, name='modifetud3'),
    path('Supp_Etud', views.Supp_Etud, name='Supp_Etud'),
    path('Acceptation_etudiant', views.Acceptation_etudiant, name='Acceptation_etudiant'),
    path('etudiant_inscription_list/', views.etudiant_inscription_list, name='etudiant_inscription_list'),
    path('Etudiants/<str:CNE>/Note_Etud/', views.Note_Etud, name='Note_Etud'),
    path('Etudiants/<str:CNE>/Etud_cours_m/', views.Etud_cours_m, name='Etud_cours_m'),


    # enseignant
    path('Ens', views.Ens, name='Ens'),
    path('Ens_info/<str:myid>', views.Ens_info, name='Ens_info'),
    path('Ens_infos', views.Ens_infos, name='Ens_infos'),
    path('Ens_private', views.Ens_private, name='Ens_private'),
    path('Ajout_Ens', views.Ajout_Ens, name='Ajout_Ens'),
    path('Modif_Ens', views.Modif_Ens, name='Modif_Ens'),
    path('modifens3/<str:myid>', views.modifens3, name='modifens3'),
    path('Supp_Ens', views.Supp_Ens, name='Supp_Ens'),
    path('Acceptation_enseignant', views.Acceptation_enseignant, name='Acceptation_enseignant'),
    path('enseignant_recrutement_list/', views.enseignant_recrutement_list, name='enseignant_recrutement_list'),
    path('Aff_etud_admin', views.Aff_etud_admin, name='Aff_etud_admin'),
    path('Aff_ens_admin', views.Aff_ens_admin, name='Aff_ens_admin'),
    path('Enseignants/<str:CIN>/', views.Enseignants, name='Enseignants'),
    # secretaire
    path('Secretaires', views.Secretaires, name='Secretaires'),
    path('Aff_etud_sec', views.Aff_etud_sec, name='Aff_etud_sec'),
    path('Aff_ens_sec/', views.Aff_ens_sec, name='Aff_ens_sec'),
    path('Horaire_T', views.Horaire_T, name='Horaire_T'),
    # Filiere
    path('Ajout_Filiere', views.Ajout_Filiere, name='Ajout_Filiere'),
    #General
    path('Horaire_T', views.Horaire_T, name='Horaire_T'),

    
]
