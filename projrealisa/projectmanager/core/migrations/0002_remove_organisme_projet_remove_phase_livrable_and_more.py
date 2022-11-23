# Generated by Django 4.1.3 on 2022-11-23 12:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisme',
            name='projet',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='livrable',
        ),
        migrations.RemoveField(
            model_name='projet',
            name='organismeClient',
        ),
        migrations.RemoveField(
            model_name='projet',
            name='projet',
        ),
        migrations.AddField(
            model_name='livrable',
            name='phase',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='livrable_phase', to='core.phase'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phase',
            name='projet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='projet_phase', to='core.projet'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projet',
            name='organisme_Client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='projet_phase', to='core.organisme'),
            preserve_default=False,
        ),
    ]