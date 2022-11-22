# Generated by Django 4.1.3 on 2022-11-22 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livrable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('createdAt', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('date_debut', models.DateField(auto_now_add=True)),
                ('date_fin', models.DateField(auto_now=True, null=True)),
                ('nbreEmploye', models.IntegerField(default=0)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=20)),
                ('etat_projet', models.CharField(choices=[('En_cours', 'En  Cours'), ('comp', 'Complet'), ('canceled', 'Cancelled'), ('tout_Comp', 'Tout Complet')], max_length=9)),
                ('etat_facturation', models.CharField(choices=[('rec', 'reçue'), ('integr', 'intégrée'), ('bonAPayer', 'Bon à payer'), ('EnAttente', 'En attente de paiement '), ('paid', 'payée'), ('cloturer', 'clôturée')], max_length=9)),
                ('etat_paiement', models.CharField(choices=[('En_attente', 'En attente'), ('Complet', 'Complet')], max_length=10)),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('livrable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livrable_phase', to='core.livrable')),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('createdAt', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=5000)),
                ('organismeClient', models.CharField(max_length=200)),
                ('date_debut', models.DateField(auto_now_add=True)),
                ('date_fin', models.DateField(auto_now=True, null=True)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=20)),
                ('document_tech', models.FileField(upload_to='documents/')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projet_phase', to='core.phase')),
            ],
        ),
        migrations.CreateModel(
            name='Organisme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('telephone', models.IntegerField(blank=True, default=1, null=True)),
                ('nom_contact', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('address_web', models.CharField(max_length=200)),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organisme_projet', to='core.projet')),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('telephone', models.IntegerField(blank=True, default=0, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('organisme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employer_organisme', to='core.organisme')),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employer_profil', to='core.profil')),
            ],
        ),
    ]