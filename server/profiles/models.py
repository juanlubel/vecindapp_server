from django.db import models

# Create your models here.


class Propietario(models.Model):
    user = models.OneToOneField(
        'authentication.Profile', on_delete=models.CASCADE
    )
    bankAccount = models.TextField(blank=True)
    isAdmin = models.BooleanField('Administrador', default=False)
    isPresident = models.BooleanField('Presidente', default=False)

    def __str__(self):
        return self.user.first_name


class Inquilino(models.Model):
    user = models.OneToOneField(
        'authentication.Profile', on_delete=models.CASCADE
    )
    bankAccount = models.TextField(blank=True)
    canPublish = models.BooleanField('Puede publicar', default=False)

    def __str__(self):
        return self.user.first_name


class Servicio(models.Model):
    user = models.OneToOneField(
        'authentication.Profile', on_delete=models.CASCADE
    )
    company = models.TextField()
    typeOf = models.TextField()

    def __str__(self):
        return self.user.first_name
