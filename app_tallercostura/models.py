
from django.db import models



# ==========================================

# MODELO: ALUMNO

# ==========================================

class Alumno(models.Model):

    nombre = models.CharField(max_length=100)

    apellido = models.CharField(max_length=100)

    correo = models.EmailField(unique=True)

    telefono = models.CharField(max_length=15)

    direccion = models.CharField(max_length=200)

    fecha_nacimiento = models.DateField()

    fecha_registro = models.DateField(auto_now_add=True)



    clases = models.ManyToManyField('Clase', through='Inscripcion', related_name='alumnos')



    def __str__(self):

        return f"{self.nombre} {self.apellido}"





# ==========================================

# MODELO: CLASE

# ==========================================

class Clase(models.Model):

    nombre = models.CharField(max_length=100)

    descripcion = models.TextField()

    nivel = models.CharField(max_length=50, choices=[

        ('Básico', 'Básico'),

        ('Intermedio', 'Intermedio'),

        ('Avanzado', 'Avanzado'),

    ])

    fecha_inicio = models.DateField()

    fecha_fin = models.DateField()

    duracion_horas = models.PositiveIntegerField()

    cupo_maximo = models.PositiveIntegerField()



    def __str__(self):

        return f"{self.nombre} ({self.nivel})"





# ==========================================

# MODELO: INSCRIPCION

# ==========================================

class Inscripcion(models.Model):

    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)

    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)

    fecha_inscripcion = models.DateField(auto_now_add=True)

    metodo_pago = models.CharField(max_length=50, choices=[

        ('Efectivo', 'Efectivo'),

        ('Tarjeta', 'Tarjeta'),

        ('Transferencia', 'Transferencia'),

    ])

    monto_pagado = models.DecimalField(max_digits=8, decimal_places=2)

    estado = models.CharField(max_length=50, choices=[

        ('Activa', 'Activa'),

        ('Cancelada', 'Cancelada'),

        ('Finalizada', 'Finalizada'),

    ])

    observaciones = models.TextField(blank=True, null=True)



    def __str__(self):

        return f"{self.alumno} → {self.clase}"
