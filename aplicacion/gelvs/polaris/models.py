from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

class Ciudad(models.Model):
    id_ciudad = models.IntegerField(primary_key=True)
    id_provincia = models.ForeignKey('Provincia', db_column='id_provincia')
    nombre = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.nombre.econde(encoding='UTF-8')

    class Meta:
        managed = False
        db_table = 'ciudad'


class Cliente(models.Model):
    id_cliente = models.CharField(primary_key=True, max_length=13)
    id_contacto = models.ForeignKey('Contacto', db_column='id_contacto', blank=True, null=True)
    id_ciudad = models.ForeignKey(Ciudad, db_column='id_ciudad', blank=True, null=True)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=600)
    telefono = models.CharField(max_length=15)
    fax = models.CharField(max_length=15, blank=True)
    mail = models.CharField(max_length=100, blank=True)
    notas = models.TextField(blank=True)
    registro = models.DateTimeField()

    def __unicode__(self):
        return self.nombre.econde(encoding='UTF-8')

    class Meta:
        managed = False
        db_table = 'cliente'

class Compra(models.Model):
    id_compra = models.IntegerField(primary_key=True)
    id_inventario = models.ForeignKey('Inventario', db_column='id_inventario')
    id_proveedor = models.ForeignKey('Proveedor', db_column='id_proveedor')
    id_tecnico = models.ForeignKey('Tecnico', db_column='id_tecnico')
    nro_factura = models.CharField(max_length=12)
    fecha = models.DateField()
    cantidad = models.IntegerField()
    costo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    notas = models.TextField(blank=True)
    registro = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'compra'

class Contacto(models.Model):
    id_contacto = models.IntegerField(primary_key=True)
    id_ciudad = models.ForeignKey(Ciudad, db_column='id_ciudad', blank=True, null=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15, blank=True)
    celular = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=100, blank=True)
    notas = models.TextField(blank=True)
    registro = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'contacto'

class Factura(models.Model):
    id_factura = models.IntegerField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, db_column='id_cliente')
    id_contacto = models.ForeignKey(Contacto, db_column='id_contacto', blank=True, null=True)
    fecha = models.DateField()
    fecha_envio = models.DateField()
    guia_envio = models.CharField(max_length=50, blank=True)
    servicio_envio = models.CharField(max_length=80)
    estado = models.CharField(max_length=50)
    archivo = models.CharField(max_length=200, blank=True)
    notas = models.TextField(blank=True)
    registro = models.DateTimeField()

    def __unicode__(self):
        return str(self.id_factura)

    class Meta:
        managed = False
        db_table = 'factura'

class FacturaDetalle(models.Model):
    id_factura_detalle = models.IntegerField(unique=True)
    id_factura = models.ForeignKey(Factura, db_column='id_factura')
    id_mantenimiento = models.IntegerField()
    id_reparacion = models.IntegerField()
    registro = models.DateTimeField()

    def __unicode__(self):
        return str(self.id_factura)

    class Meta:
        managed = False
        db_table = 'factura_detalle'

class GastosViaje(models.Model):
    id_gasto_viaje = models.IntegerField(unique=True)
    id_viaje = models.ForeignKey('Viaje', db_column='id_viaje')
    nro_factura = models.CharField(max_length=20)
    fecha = models.DateField()
    detalle = models.CharField(max_length=300)
    valor = models.DecimalField(max_digits=4, decimal_places=2)
    tipo = models.CharField(max_length=45, blank=True)
    registro = models.DateTimeField()
    
    def __unicode__(self):
        return str(self.id_viaje)

    class Meta:
        managed = False
        db_table = 'gastos_viaje'

class Inspeccion(models.Model):
    id_inspeccion = models.IntegerField(primary_key=True)
    id_vehiculo = models.ForeignKey('Vehiculo', db_column='id_vehiculo')
    id_tecnico = models.ForeignKey('Tecnico', db_column='id_tecnico')
    id_contacto = models.ForeignKey(Contacto, db_column='id_contacto')
    id_ciudad = models.ForeignKey(Ciudad, db_column='id_ciudad', blank=True, null=True)
    periodo = models.IntegerField()
    fecha = models.DateField()
    notas = models.TextField(blank=True)
    registro = models.DateTimeField()
    def __unicode__(self):
        cadena = "Inspeccion:%s Cliente %s"%(self.id_inspeccion, self.id_vehiculo)
        return str(cadena)


    class Meta:
        managed = False
        db_table = 'inspeccion'

class Inventario(models.Model):
    id_inventario = models.IntegerField(primary_key=True)
    fecha = models.DateTimeField()
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    unidad = models.CharField(max_length=25)
    stok_min = models.IntegerField()
    marca = models.CharField(max_length=45, blank=True)
    ubicacion = models.CharField(max_length=100)
    notas = models.TextField(blank=True)
    registro = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'inventario'

class Mantenimiento(models.Model):
    id_mantenimiento = models.IntegerField(primary_key=True)
    id_viaje = models.ForeignKey('Viaje', db_column='id_viaje')
    id_vehiculo = models.ForeignKey('Vehiculo', db_column='id_vehiculo')
    id_ciudad = models.ForeignKey(Ciudad, db_column='id_ciudad', blank=True, null=True)
    periodo = models.IntegerField()
    fecha = models.DateField()
    kilometros = models.CharField(max_length=10)
    notas = models.TextField(blank=True)
    registro = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'mantenimiento'

class MantenimientoDetalle(models.Model):
    id_mantenimiento_detalle = models.IntegerField(unique=True)
    id_mantenimiento = models.ForeignKey(Mantenimiento, db_column='id_mantenimiento')
    id_inventario = models.ForeignKey(Inventario, db_column='id_inventario')
    fecha = models.TimeField()
    estado = models.CharField(max_length=25, blank=True)
    cantidad = models.FloatField()
    notas = models.CharField(max_length=600, blank=True)
    registro = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'mantenimiento_detalle'

class Proveedor(models.Model):
    id_proveedor = models.CharField(primary_key=True, max_length=13)
    id_ciudad = models.ForeignKey(Ciudad, db_column='id_ciudad', blank=True, null=True)
    id_contacto = models.ForeignKey(Contacto, db_column='id_contacto', blank=True, null=True)
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=500)
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=30, blank=True)
    credito = models.IntegerField(blank=True, null=True)
    notas = models.TextField(blank=True)
    registro = models.DateTimeField()
    def __unicode__(self):
        return str(self.nombre)

    class Meta:
        managed = False
        db_table = 'proveedor'

class Provincia(models.Model):
    id_provincia = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True)
    def __unicode__(self):
        return str(self.nombre)
    class Meta:
        managed = False
        db_table = 'provincia'

class Reparacion(models.Model):
    id_reparacion = models.IntegerField(primary_key=True)
    id_viaje = models.ForeignKey('Viaje', db_column='id_viaje')
    id_vehiculo = models.ForeignKey('Vehiculo', db_column='id_vehiculo')
    id_ciudad = models.ForeignKey(Ciudad, db_column='id_ciudad', blank=True, null=True)
    periodo = models.IntegerField()
    kilometros = models.CharField(max_length=45)
    fecha_entrada = models.DateTimeField()
    fecha_salida = models.DateTimeField()
    notas = models.TextField(blank=True)
    registro = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'reparacion'

class ReparacionDetalle(models.Model):
    id_reparacion_detalle = models.IntegerField(primary_key=True)
    id_reparacion = models.ForeignKey(Reparacion, db_column='id_reparacion')
    id_inventario = models.ForeignKey(Inventario, db_column='id_inventario')
    fecha = models.TimeField()
    estado = models.CharField(max_length=25, blank=True)
    cantidad = models.IntegerField()
    notas = models.CharField(max_length=600, blank=True)
    registro = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'reparacion_detalle'

class Tecnico(models.Model):
    id_tecnico = models.CharField(primary_key=True, max_length=10)
    nombres = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15, blank=True)
    celular = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=100, blank=True)
    notas = models.TextField(blank=True)
    registro = models.DateTimeField()
    def __unicode__(self):
        return str(self.nombre)
    class Meta:
        managed = False
        db_table = 'tecnico'

class TecnicoViaje(models.Model):
    id_tecnico = models.ForeignKey(Tecnico, db_column='id_tecnico')
    id_viaje = models.ForeignKey('Viaje', db_column='id_viaje')
    registro = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'tecnico_viaje'

class Vehiculo(models.Model):
    id_vehiculo = models.CharField(max_length=17)
    id_cliente = models.ForeignKey(Cliente, db_column='id_cliente')
    id_contacto = models.ForeignKey(Contacto, db_column='id_contacto', blank=True, null=True)
    id_ciudad = models.ForeignKey(Ciudad, db_column='id_ciudad', blank=True, null=True)
    modelo = models.CharField(max_length=45)
    nro_motor = models.CharField(max_length=25, blank=True)
    ingreso = models.DateField(blank=True, null=True)
    notas = models.TextField(blank=True)
    registro = models.DateTimeField()

    def __unicode__(self):
        return str(self.id_vehiculo)

    class Meta:
        managed = False
        db_table = 'vehiculo'

class Viaje(models.Model):
    id_viaje = models.IntegerField(primary_key=True)
    fecha_salida = models.DateField()
    fecha_regreso = models.DateField()
    nro_vehiculos = models.IntegerField()
    provincias_destino = models.CharField(max_length=500)
    varlor_caja = models.DecimalField(max_digits=5, decimal_places=2)
    informe = models.TextField()
    registro = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'viaje'