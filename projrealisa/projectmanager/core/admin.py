from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Livrable)
admin.site.register(Profil)
admin.site.register(Phase)
admin.site.register(Projet)
admin.site.register(Organisme)
admin.site.register(Employer)

admin.site.site_header = "Gestion des Projets"
admin.site.site_title = "Gestion des Projets Admin Portal"
admin.site.index_title = "Bienvenue sur le portail de Gestion des Projets "