from django.shortcuts import render
from rest_framework import generics
from xml.dom import ValidationErr
from .models import *
from .serializer import *
# Create your views here.
class LivrableCreateAPIView(generics.ListCreateAPIView):
    queryset=Livrable.objects.all()
    serializer_class=LivrableSerializers
    
    def perform_create(self, serializer):
        if not serializer.validated_data:
            raise  ValidationErr("Please fill up all fields")
        else:
            serializer.save()
livrable_create_view=LivrableCreateAPIView.as_view()

class LivrableDetail(generics.RetrieveAPIView):
    queryset=Livrable.objects.all()
    serializer_class=LivrableSerializers
    lookup_field='pk'

livrable_detail_view=LivrableDetail.as_view()    

class LivrableUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset=Livrable.objects.all()
    serializer_class=LivrableSerializers
    lookup_field='pk'
    
livrable_update_view=LivrableUpdateAPIView.as_view()    

class LivrableDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset=Livrable.objects.all()
    serializer_class=LivrableSerializers
    lookup_field='pk'
    
livrable_destroy_view=LivrableDestroyAPIView.as_view()  


class ProfilCreateAPIView(generics.ListCreateAPIView):
    queryset=Profil.objects.all()
    serializer_class=ProfilSerializers

profil_create_view=ProfilCreateAPIView.as_view()

class ProfilDetailAPIView(generics.RetrieveAPIView):
    queryset=Profil.objects.all()
    serializer_class=ProfilSerializers
    lookup_field='pk'
profil_detail_view=ProfilDetailAPIView.as_view()      

class ProfilUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset=Profil.objects.all()
    serializer_class=ProfilSerializers
    lookup_field='pk'
profil_update_view=ProfilUpdateAPIView.as_view() 

class ProfilDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset=Profil.objects.all()
    serializer_class=ProfilSerializers
    lookup_field='pk'
profil_destroy_view=ProfilDestroyAPIView.as_view() 

class PhaseCreateAPIView(generics.ListCreateAPIView):
    queryset=Phase.objects.all()
    serializer_class=PhaseSerializers

phase_create_view=PhaseCreateAPIView.as_view() 

class PhaseDetailAPIView(generics.RetrieveAPIView):
    queryset=Phase.objects.all()
    serializer_class=PhaseSerializers
    lookup_field='pk'

phase_detail_view=PhaseDetailAPIView.as_view() 

class PhaseUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset=Phase.objects.all()
    serializer_class=PhaseSerializers
    lookup_field='pk'

phase_update_view=PhaseUpdateAPIView.as_view() 

class PhaseDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset=Phase.objects.all()
    serializer_class=PhaseSerializers
    lookup_field='pk'

phase_destroy_view=PhaseDestroyAPIView.as_view() 

class ProjetCreateAPIView(generics.ListCreateAPIView):
    queryset=Projet.objects.all()
    serializer_class=ProjetSerializers
   

projet_create_view=ProjetCreateAPIView.as_view() 

class ProjetDetailAPIView(generics.RetrieveAPIView):
    queryset=Projet.objects.all()
    serializer_class=ProjetSerializers
    lookup_field='pk'

projet_detail_view=ProjetDetailAPIView.as_view() 

class ProjetUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset=Projet.objects.all()
    serializer_class=ProjetSerializers
    lookup_field='pk'

projet_update_view=ProjetUpdateAPIView.as_view() 

class ProjetDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset=Projet.objects.all()
    serializer_class=ProjetSerializers
    lookup_field='pk'

projet_destroy_view=ProjetDestroyAPIView.as_view() 

class OrganismeCreateAPIView(generics.ListCreateAPIView):
    queryset=Organisme.objects.all()
    serializer_class=OrganismeSerializers


organisme_create_view=OrganismeCreateAPIView.as_view() 

class OrganismeDetailAPIView(generics.RetrieveAPIView):
    queryset=Organisme.objects.all()
    serializer_class=OrganismeSerializers
    lookup_field='pk'

organisme_detail_view=OrganismeDetailAPIView.as_view() 

class OrganismeUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset=Organisme.objects.all()
    serializer_class=OrganismeSerializers
    lookup_field='pk'

organisme_update_view=OrganismeUpdateAPIView.as_view() 

class OrganismeDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset=Organisme.objects.all()
    serializer_class=OrganismeSerializers
    lookup_field='pk'

organisme_destroy_view=OrganismeDestroyAPIView.as_view() 
   
    
class EmployerCreateAPIView(generics.ListCreateAPIView):
    queryset=Employer.objects.all()
    serializer_class=EmployerSerializers
    
employer_create_view=EmployerCreateAPIView.as_view() 

class EmployerDetailAPIView(generics.RetrieveAPIView):
    queryset=Employer.objects.all()
    serializer_class=EmployerSerializers
    lookup_field='pk'

employer_detail_view=EmployerDetailAPIView.as_view() 

class EmployerUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset=Employer.objects.all()
    serializer_class=EmployerSerializers
    lookup_field='pk'

employer_update_view=EmployerUpdateAPIView.as_view() 

class EmployerDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset=Employer.objects.all()
    serializer_class=EmployerSerializers
    lookup_field='pk'

employer_destroy_view=EmployerDestroyAPIView.as_view()  