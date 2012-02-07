from django.db import models

class Alumno(models.Model):
    dni = models.CharField(max_length=9, unique=True)
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    usuarioUJI = models.CharField(max_length=8)
    
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    usuarioUJI = models.CharField(max_length=8)
    email = models.EmailField()
    ROL_CHOICES = (
                    ('P', 'Professorado'),
                    ('T', 'Tutorizacion'),
                    ('C', 'Coordinadinacion')
                    )
    rol = models.CharField(max_length=1, choices=ROL_CHOICES)
    
    def __str__(self):
        return self.rol

class Curso(models.Model):
    curso = models.CharField(max_length=15)
    
    def __str__(self):
        return self.curso

class Proyecto(models.Model):
    alumno = models.ForeignKey(Alumno, null=True)
    tutor = models.ForeignKey(Usuario)
    supervisor = models.CharField(max_length=50)
    curso = models.ForeignKey(Curso, null=True)
    
    empresa= models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    
    titulo = models.CharField(max_length=100, null=True)
    
    inicio = models.DateField()
    dedicacionSemanal = models.FloatField(null=True)
    
    otrosDatos = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        unique_together = [("alumno", "curso")]
    
    
        
    