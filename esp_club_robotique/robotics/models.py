from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Member(models.Model):
    first_login = models.BooleanField(default=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Mot de passe non haché

    def __str__(self):
        return self.email

# Modèle pour les médias (photos, vidéos, tutoriels PDF)
class Media(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('pdf', 'PDF'),  # Pour les tutoriels en PDF
    ]
    title = models.CharField(max_length=100)  # Titre du média
    file = models.FileField(upload_to='media/')  # Chemin de stockage des fichiers
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)  # Type de média
    description = models.TextField(blank=True, null=True)  # Description optionnelle
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Date d'ajout

    def __str__(self):
        return f"{self.title} ({self.media_type})"

