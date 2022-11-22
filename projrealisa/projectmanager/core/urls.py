from django.urls import path
from .import views

urlpatterns=[
    path("livrable/",views.livrable_create_view,name="livrable-list"),
    path("livrable/<int:pk>/",views.livrable_detail_view,name="livrable-detail"),
    path("livrable/<int:pk>/update",views.livrable_update_view,name="livrable-update"),
    path("livrable/<int:pk>/delete",views.livrable_destroy_view,name="livrable-delete"),
    #profil
    path("profil/",views.profil_create_view,name="profil-list"),
    path("profil/<int:pk>/",views.profil_detail_view,name="profil-detail"),
    path("profil/<int:pk>/update",views.profil_update_view,name="profil-update"),
    path("profil/<int:pk>/delete",views.profil_destroy_view,name="profil-delete"),
    #phase
    path("phase/",views.phase_create_view,name="phase-list"),
    path("phase/<int:pk>/",views.phase_detail_view,name="phase-detail"),
    path("phase/<int:pk>/update",views.phase_update_view,name="phase-update"),
    path("phase/<int:pk>/delete",views.phase_destroy_view,name="phase-delete"),
    #projet
    path("projet/",views.projet_create_view,name="projet-list"),
    path("projet/<int:pk>/",views.projet_detail_view,name="projet-detail"),
    path("projet/<int:pk>/update",views.projet_update_view,name="projet-update"),
    path("projet/<int:pk>/delete",views.projet_destroy_view,name="projet-delete"),
    #projet
    path("organisme/",views.organisme_create_view,name="organisme-list"),
    path("organisme/<int:pk>/",views.organisme_detail_view,name="organisme-detail"),
    path("organisme/<int:pk>/update",views.organisme_update_view,name="organisme-update"),
    path("organisme/<int:pk>/delete",views.organisme_destroy_view,name="organisme-delete"),
    #employer
    path("employer/",views.employer_create_view,name="employer-list"),
    path("employer/<int:pk>/",views.employer_detail_view,name="employer-detail"),
    path("employer/<int:pk>/update",views.employer_update_view,name="employer-update"),
    path("employer/<int:pk>/delete",views.employer_destroy_view,name="employer-delete"),
]