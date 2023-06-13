from django.db import models

# Create your models here.


class Sexo(models.Model):
    id_genero = models.AutoField(db_column="idGenero", primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)


class Mascota(models.Model):
    id_mascota = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_genero = models.ForeignKey(
        "Sexo", on_delete=models.CASCADE, db_column="idGenero"
    )

    def __str__(self):
        return str(self.nombre) + " " + str(self.apellido)
