from django.contrib import admin
from.models import Cliente,Rol,Venta,DetalleVenta,DetalleCompra,Compra,Permiso,Usuario,TipoPago,Proveedor,Categoria,MateriaPrima,ProductoElaborado, CompraPaypal

admin.site.register(Cliente)
admin.site.register(Rol)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(DetalleCompra)
admin.site.register(Compra)
admin.site.register(Permiso)
admin.site.register(Usuario)
admin.site.register(TipoPago)
admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(MateriaPrima)
admin.site.register(ProductoElaborado)
admin.site.register(CompraPaypal)


