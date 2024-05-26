from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .models import Etudiant
from .models import Enseignant
from .models import Option
from .models import Module
from .models import Cours
from .models import Salle
from .models import Absence
from .models import Horaire
from .models import NoteEtudiant
from .models import EtudiantInscription
from .models import EnseignantRecrutement
from .models import Secretaire
from .models import Ad
from .models import log
from .models import login_user
# from .models import User

# Enregistrer les classes
admin.site.register(Etudiant)
admin.site.register(EtudiantInscription)
admin.site.register(Enseignant)
admin.site.register(EnseignantRecrutement)
admin.site.register(Secretaire)
admin.site.register(Option)
admin.site.register(Module)
admin.site.register(Cours)
admin.site.register(Salle)
admin.site.register(Absence)
admin.site.register(Horaire)
admin.site.register(NoteEtudiant)
admin.site.register(Ad)
admin.site.register(log)
admin.site.register(login_user)

# admin.site.register(User)




