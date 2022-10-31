from django.db import models

# modelos de solicitud de servicios.

class clientes(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=80)
    telefono = models.CharField(max_length=20)
    

    def __str__(self):
        return self.nombre

class servicios(models.Model):
    id=models.AutoField(primary_key=True)
    servicio = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.IntegerField()

    def __str__(self):
        return self.servicio

class solicitud(models.Model):
    id=models.AutoField(primary_key=True)
    cliente = models.ForeignKey(clientes, on_delete=models.CASCADE)
    servicio = models.ForeignKey(servicios, on_delete=models.CASCADE)
    sfechahora = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)

    def __str__(self):
        return self.cliente.nombre

class cobros(models.Model):
    id=models.AutoField(primary_key=True)
    solicitud = models.ForeignKey(solicitud, on_delete=models.CASCADE)
    cfechahora = models.DateTimeField(auto_now_add=True)
    valorcobrado = models.IntegerField()

    def __str__(self):
        return self.valor
    