from rest_framework import serializers
from .models import *

class LivrableSerializers(serializers.ModelSerializer):
    class Meta:
        model=Livrable
        fields="__all__"

class ProfilSerializers(serializers.ModelSerializer):
    class Meta:
        model=Profil
        fields="__all__"

class PhaseSerializers(serializers.ModelSerializer):
    class Meta:
        model=Phase
        fields="__all__"
        
class ProjetSerializers(serializers.ModelSerializer):
    class Meta:
        model=Projet
        fields="__all__"              
class OrganismeSerializers(serializers.ModelSerializer):
    class Meta:
        model=Organisme
        fields="__all__"       
class EmployerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Employer
        fields="__all__"