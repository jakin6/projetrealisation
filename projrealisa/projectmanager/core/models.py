from django.db import models

# Create your models here.



# Project Status
# Active: The project is currently being worked on by the project team.
#  Completed: Work on the project has finished, and 
#all deliverables/tasks have been completed. Cancelled: The project has not finished, and work on the project will not continue

# Comprendre les différents statuts d'une facture fournisseur
# Facture reçue - statut partagé ...
# Facture intégrée – statut partagé ...
# Facture Bon à payer – statut partagé ...
# Facture en attente de paiement – statut non partagé...
# Facture payée - statut non partagé...
# Facture clôturée – statut non partagé


#Type paiement:
# En attente
# Il s'agit d'un paiement qui a commencé, mais qui n'est pas terminé. Un exemple de ceci est quelqu'un qui a rempli le formulaire de paiement et s'est ensuite rendu sur PayPal pour le paiement. Nous avons le dossier de vente, mais ils n'ont pas encore effectué leur paiement.

# Complet
# Il s'agit d'un paiement qui a été payé et le produit livré au client.

# Remboursé
# Il s'agit d'un paiement où l'argent a été retransféré au client et le client n'a plus accès au produit.

#Les paiements révoqués restreignent l'accès au produit sans remboursement.

# Pré-approuvé
# Un paiement pré-approuvé est un paiement pour lequel le client a approuvé le paiement, mais il n'a pas encore été traité. Il sera traité ultérieurement.
class Livrable(models.Model):
    libelle=models.CharField(max_length=500)
    description=models.TextField()
    createdAt=models.DateField(auto_now_add=True)

    def  __str__(self):
        return self.libelle
    
class Profil(models.Model):
    nom=models.CharField(max_length=200)
    createdAt=models.DateField(auto_now_add=True)
    def  __str__(self):
        return self.nom

class Phase(models.Model):
    livrable=models.ForeignKey(Livrable,related_name="livrable_phase",on_delete=models.CASCADE)
    libelle=models.CharField(max_length=500)
    description=models.TextField()
    date_debut=models.DateField(auto_now_add=True)
    date_fin=models.DateField(auto_now=True,null=True,blank=True)
    nbreEmploye=models.IntegerField(default=0)
    montant=models.DecimalField(max_digits=20,decimal_places=2)
    etat_projetType=[('En_cours',"En  Cours"),('comp','Complet'),('canceled','Cancelled'),('tout_Comp','Tout Complet')]
    etat_projet=models.CharField(max_length=9,choices=etat_projetType)
    etat_facturationType=[("rec","reçue"),("integr","intégrée"),("bonAPayer","Bon à payer"),("EnAttente","En attente de paiement "),("paid","payée"),("cloturer","clôturée")]
    etat_facturation=models.CharField(max_length=9,choices=etat_facturationType)
    etat_paiementType=[("En_attente","En attente"),("Complet","Complet")]
    etat_paiement=models.CharField(max_length=10,choices=etat_paiementType)
    createdAt=models.DateField(auto_now_add=True)

    def  __str__(self):
        return self.libelle


class Projet(models.Model):
    projet=models.ForeignKey(Phase,related_name="projet_phase",on_delete=models.CASCADE)
    nom=models.CharField(max_length=200)
    description=models.TextField(max_length=5000)
    organismeClient=models.CharField(max_length=200)
    date_debut=models.DateField(auto_now_add=True)
    date_fin=models.DateField(auto_now=True,null=True,blank=True)
    montant=models.DecimalField(max_digits=20,decimal_places=2)
    document_tech=models.FileField(upload_to='documents/')
    createdAt=models.DateField(auto_now_add=True)

    def  __str__(self):
        return self.nom

class Organisme(models.Model):
    nom=models.CharField(max_length=200)
    projet=models.ForeignKey(Projet,related_name="organisme_projet",on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    telephone=models.IntegerField(default=1,null=True,blank=True)
    nom_contact=models.CharField(max_length=200)
    email=models.EmailField(unique=True,null=True)
    address_web=models.CharField(max_length=200)
    createdAt=models.DateField(auto_now_add=True)

    def  __str__(self):
        return self.nom

class Employer(models.Model):
    nom=models.CharField(max_length=200)
    organisme=models.ForeignKey(Organisme,related_name="employer_organisme",on_delete=models.CASCADE)
    profil=models.ForeignKey(Profil,related_name="employer_profil",on_delete=models.CASCADE)
    prenom=models.CharField(max_length=200)
    telephone=models.IntegerField(default=0,null=True,blank=True)
    email=models.EmailField(unique=True,null=True)
    password=models.CharField(max_length=200)
    createdAt=models.DateField(auto_now_add=True)
    def  __str__(self):
        return self.nom



    


