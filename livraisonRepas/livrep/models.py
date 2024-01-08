from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.
'''
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    ADMIN = 'admin'
    CLIENT = 'client'
    ROLE_CHOICES = [
        (ADMIN, 'admin'),
        (CLIENT, 'client'),
    ]

    objects = CustomUserManager()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=CLIENT)
    username = None
    ville = models.CharField(max_length=100)
    telephone = models.IntegerField(unique=True)
    adresse = models.CharField(max_length=250)
    is_active = None
    is_staff = None
    is_superuser = None
    last_login = None
    date_joined = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [first_name, last_name]
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='livrep_user_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='livrep_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )'''



class Categorie(models.Model):
    name = models.CharField(max_length=100)

class Plat(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    prix = models.FloatField()
    ingredients = models.CharField(max_length=500)
    url = models.CharField(max_length=250, null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

class Commande(models.Model):
    status = models.CharField(max_length=200)
    dateCommande = models.DateField()
    plat = models.ForeignKey(Plat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Commentaire(models.Model):
    comment = models.CharField(max_length=250)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    plat = models.ForeignKey(Plat, on_delete=models.CASCADE)

class Ranking(models.Model):
    rank = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plat = models.ForeignKey(Plat, on_delete=models.CASCADE)

class Historique(models.Model):
    user = models.ForeignKey(User, related_name='historique_user', on_delete=models.CASCADE)
    commande = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=250)







