"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('Gestion_Ecole.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from Gestion_Ecole.views import home, Enreg, Etud,Ens, Secretaires, Adm
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Gestion_Ecole.urls')),
    path('logg', include('Gestion_Ecole.urls')),
    path('Enreg', include('Gestion_Ecole.urls')), 
    path('Adm', include('Gestion_Ecole.urls')), 
    path('Etud', include('Gestion_Ecole.urls')), 
    path('Etud_info', include('Gestion_Ecole.urls')),
    path('Ajout_Etud', include('Gestion_Ecole.urls')),
    path('Ajout_Etud_admin', include('Gestion_Ecole.urls')),
    path('Modif_Etud', include('Gestion_Ecole.urls')),
    path('modifetud3/<str:myid>', include('Gestion_Ecole.urls')),
    path('Supp_Etud', include('Gestion_Ecole.urls')),
    path('Acceptation_etudiant', include('Gestion_Ecole.urls')),
    path('etudiant_inscription_list/', include('Gestion_Ecole.urls')),
    path('Etudiants/<str:CNE>/',include('Gestion_Ecole.urls')),
    path('Ens', include('Gestion_Ecole.urls')),
    path('Ens_info/<str:myid>', include('Gestion_Ecole.urls')),
    path('Ens_infos', include('Gestion_Ecole.urls')),
    path('Ens_private', include('Gestion_Ecole.urls')),
    path('Ajout_Ens', include('Gestion_Ecole.urls')),
    path('Modif_Ens', include('Gestion_Ecole.urls')),
    path('modifens3/<str:myid>', include('Gestion_Ecole.urls')),
    path('Supp_Ens', include('Gestion_Ecole.urls')),
    path('Acceptation_enseignant', include('Gestion_Ecole.urls')),
    path('enseignant_recrutement_list/', include('Gestion_Ecole.urls')),
    path('Secretaires', include('Gestion_Ecole.urls')),
    path('Ajout_Filiere', include('Gestion_Ecole.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG :
       urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)