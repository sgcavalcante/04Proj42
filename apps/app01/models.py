from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.



class Dados(models.Model):
    nome = models.CharField(
        max_length=120,
        null = False,
        blank=False
    )

    telefone = models.CharField(
        max_length=120,
        null=False,
        blank=False
    )

    email = models.CharField(
        max_length=120,
        null=False,
        blank=False
    )

    cidade = models.CharField(
        max_length=120,
        null=False,
        blank=False
    )

    subestacao = models.CharField(
        max_length=120,
        null=False,
        blank=False
    )

    nivel_tensao_AT = models.CharField(
        max_length=120,
        null=False,
        blank=False
    )

    nivel_tensao_BT = models.CharField(
        max_length=120,
        null=False,
        blank=False
    )



