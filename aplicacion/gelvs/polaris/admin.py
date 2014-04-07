from django.contrib import admin

# Register your models here.
from gelvs.polaris.models import *

admin.site.register(Ciudad)
admin.site.register(Cliente)
admin.site.register(Compra)
admin.site.register(Contacto)
admin.site.register(Factura)
admin.site.register(FacturaDetalle)
admin.site.register(GastosViaje)
admin.site.register(Inspeccion)
admin.site.register(Inventario)
admin.site.register(Mantenimiento)
admin.site.register(MantenimientoDetalle)
admin.site.register(Proveedor)
admin.site.register(Provincia)
admin.site.register(Reparacion)
admin.site.register(ReparacionDetalle)
admin.site.register(Tecnico)
admin.site.register(TecnicoViaje)
admin.site.register(Vehiculo)
admin.site.register(Viaje)
