from django.db import models

class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='ID_Categoria', primary_key=True)  # Field name made lowercase.
    descripcion_categoria = models.CharField(db_column='Descripcion_Categoria', max_length=100, blank=True, null=True)  # Field name made lowercase.
    estado_categoria = models.BooleanField(db_column='Estado_Categoria')  # Field name made lowercase.
    fecharegistrocategoria = models.DateField(db_column='FechaRegistroCategoria')  # Field name made lowercase.

    def __str__(self):
        return str(self.id_categoria)

class Cliente(models.Model):
    id_cliente = models.AutoField(db_column='ID_Cliente', primary_key=True)  # Field name made lowercase.
    nombre_cliente = models.CharField(db_column='Nombre_Cliente', max_length=50)  # Field name made lowercase.
    apellido_cliente = models.CharField(db_column='Apellido_Cliente', max_length=50)  # Field name made lowercase.
    correo_cliente = models.CharField(db_column='Correo_Cliente', max_length=50)  # Field name made lowercase.
    clave_cliente = models.CharField(db_column='Clave_Cliente', max_length=50)  # Field name made lowercase.
    telefono_cliente = models.CharField(db_column='Telefono_Cliente', max_length=50)  # Field name made lowercase.
    fecharegistrocliente = models.DateField(db_column='FechaRegistroCliente')  # Field name made lowercase.

class Compra(models.Model):
    id_compra = models.AutoField(db_column='ID_Compra', primary_key=True)  # Field name made lowercase.
    usuario_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='USUARIO_ID_Usuario')  # Field name made lowercase.
    proveedor_id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='PROVEEDOR_ID_Proveedor')  # Field name made lowercase.
    tipodocumento_compra = models.CharField(db_column='TipoDocumento_Compra', max_length=50)  # Field name made lowercase.
    numerodocumento_compra = models.CharField(db_column='NumeroDocumento_Compra', max_length=50)  # Field name made lowercase.
    montototal_compra = models.IntegerField(db_column='MontoTotal_Compra')  # Field name made lowercase.
    fecharegistrocompra = models.DateField(db_column='FechaRegistroCompra')  # Field name made lowercase.

class DetalleCompra(models.Model):
    id_detallecompra = models.AutoField(db_column='ID_DetalleCompra', primary_key=True)  # Field name made lowercase.
    compra_id_compra = models.ForeignKey(Compra, models.DO_NOTHING, db_column='COMPRA_ID_Compra')  # Field name made lowercase.
    materia_prima_id_materiaprima = models.ForeignKey('MateriaPrima', models.DO_NOTHING, db_column='MATERIA_PRIMA_ID_MateriaPrima')  # Field name made lowercase.
    preciocompra = models.IntegerField(db_column='PrecioCompra')  # Field name made lowercase.
    precioventa = models.IntegerField(db_column='PrecioVenta')  # Field name made lowercase.
    cantidad_detallecompra = models.IntegerField(db_column='Cantidad_DetalleCompra')  # Field name made lowercase.
    montototal_detallecompra = models.IntegerField(db_column='MontoTotal_DetalleCompra')  # Field name made lowercase.
    fecharegistrodetallecompra = models.DateField(db_column='FechaRegistroDetalleCompra')  # Field name made lowercase.

class DetalleVenta(models.Model):
    id_detalleventa = models.AutoField(db_column='ID_DetalleVenta', primary_key=True)  # Field name made lowercase.
    venta_id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='VENTA_ID_Venta')  # Field name made lowercase.
    producto_elaborado_id_producto = models.ForeignKey('ProductoElaborado', models.DO_NOTHING, db_column='PRODUCTO_ELABORADO_ID_Producto')  # Field name made lowercase.
    precioventa = models.IntegerField(db_column='PrecioVenta')  # Field name made lowercase.
    cantidad_detalleventa = models.IntegerField(db_column='Cantidad_DetalleVenta')  # Field name made lowercase.
    subtotal_detalleventa = models.IntegerField(db_column='SubTotal_DetalleVenta')  # Field name made lowercase.
    fecharegistrodetalleventa = models.DateField(db_column='FechaRegistroDetalleVenta')  # Field name made lowercase.


class MateriaPrima(models.Model):
    id_materiaprima = models.AutoField(db_column='ID_MateriaPrima', primary_key=True)  # Field name made lowercase.
    categoria_id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='CATEGORIA_ID_Categoria')  # Field name made lowercase.
    codigo_materiaprima = models.CharField(db_column='Codigo_MateriaPrima', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nombre_materiaprima = models.CharField(db_column='Nombre_MateriaPrima', max_length=50)  # Field name made lowercase.
    descripcion_materiaprima = models.CharField(db_column='Descripcion_MateriaPrima', max_length=100, blank=True, null=True)  # Field name made lowercase.
    stock_materiaprima = models.IntegerField(db_column='Stock_MateriaPrima')  # Field name made lowercase.
    preciocompra_materiaprima = models.IntegerField(db_column='PrecioCompra_MateriaPrima')  # Field name made lowercase.
    estado_materiaprima = models.BooleanField(db_column='Estado_MateriaPrima')  # Field name made lowercase.
    fecharegistro_materiaprima = models.DateField(db_column='FechaRegistro_MateriaPrima')  # Field name made lowercase.

class Permiso(models.Model):
    id_permiso = models.AutoField(db_column='ID_Permiso', primary_key=True)  # Field name made lowercase.
    id_rol = models.ForeignKey('Rol', models.DO_NOTHING, db_column='ID_Rol')  # Field name made lowercase.
    nombremenu = models.CharField(db_column='NombreMenu', max_length=100)  # Field name made lowercase.
    fecharegistropermiso = models.DateField(db_column='FechaRegistroPermiso')  # Field name made lowercase.

class ProductoElaborado(models.Model):
    id_producto = models.AutoField(db_column='ID_Producto', primary_key=True)  # Field name made lowercase.
    categoria_id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='CATEGORIA_ID_Categoria')  # Field name made lowercase.
    codigo_producto = models.CharField(db_column='Codigo_Producto', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nombre_producto = models.CharField(db_column='Nombre_Producto', max_length=50)  # Field name made lowercase.
    descripcion_producto = models.CharField(db_column='Descripcion_Producto', max_length=200, blank=True, null=True)  # Field name made lowercase.
    stock_producto = models.IntegerField(db_column='Stock_Producto')  # Field name made lowercase.
    preciocompra = models.IntegerField(db_column='PrecioCompra')  # Field name made lowercase.
    precioventa = models.IntegerField(db_column='PrecioVenta')  # Field name made lowercase.
    estado_producto = models.BooleanField(db_column='Estado_Producto')  # Field name made lowercase.
    fecharegistroproducto = models.DateField(db_column='FechaRegistroProducto')  # Field name made lowercase.
    imagen = models.ImageField(upload_to='Imagen', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.id_producto
    

class Proveedor(models.Model):
    id_proveedor = models.AutoField(db_column='ID_Proveedor', primary_key=True)  # Field name made lowercase.
    rutempresa = models.CharField(db_column='RutEmpresa', max_length=50)  # Field name made lowercase.
    dvempresa = models.CharField(db_column='DVEmpresa', max_length=1)  # Field name made lowercase.
    razonsocial = models.CharField(db_column='RazonSocial', max_length=50)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=50)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=50)  # Field name made lowercase.
    fecharegistroproveedor = models.DateField(db_column='FechaRegistroProveedor')  # Field name made lowercase.

    def __str__(self):
        return self.rutempresa

class Rol(models.Model):
    id_rol = models.AutoField(db_column='ID_Rol', primary_key=True)  # Field name made lowercase.
    descripcion_rol = models.CharField(db_column='Descripcion_Rol', max_length=50)  # Field name made lowercase.
    fecharegistrorol = models.DateField(db_column='FechaRegistroRol')  # Field name made lowercase.
    id_permiso = models.IntegerField(db_column='ID_Permiso')  # Field name made lowercase.

class TipoPago(models.Model):
    id_pago = models.AutoField(db_column='ID_Pago', primary_key=True)  # Field name made lowercase.
    venta_id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='VENTA_ID_Venta')  # Field name made lowercase.
    metodopago = models.CharField(db_column='MetodoPago', max_length=50)  # Field name made lowercase.
    montopago = models.CharField(db_column='MontoPago', max_length=50)  # Field name made lowercase.
    fecharegistrotipopago = models.DateField(db_column='FechaRegistroTipoPago')  # Field name made lowercase.

class Usuario(models.Model):
    id_usuario = models.AutoField(db_column='ID_Usuario', primary_key=True)  # Field name made lowercase.
    rol_id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='ROL_ID_Rol')  # Field name made lowercase.
    rut_usuario = models.CharField(db_column='Rut_Usuario', max_length=50)  # Field name made lowercase.
    dv_usuario = models.CharField(db_column='DV_Usuario', max_length=1)  # Field name made lowercase.
    nombre_usuario = models.CharField(db_column='Nombre_Usuario', max_length=50)  # Field name made lowercase.
    apellidos_usuario = models.CharField(db_column='Apellidos_Usuario', max_length=50)  # Field name made lowercase.
    correo_usuario = models.CharField(db_column='Correo_Usuario', max_length=50)  # Field name made lowercase.
    clave_usuario = models.CharField(db_column='Clave_Usuario', max_length=50)  # Field name made lowercase.
    telefono_usuario = models.CharField(db_column='Telefono_Usuario', max_length=50)  # Field name made lowercase.
    estado_usuario = models.BooleanField(db_column='Estado_Usuario')  # Field name made lowercase.
    fecharegistrousuario = models.DateField(db_column='FechaRegistroUsuario')  # Field name made lowercase.

class Venta(models.Model):
    id_venta = models.AutoField(db_column='ID_Venta', primary_key=True)  # Field name made lowercase.
    cliente_id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='CLIENTE_ID_Cliente')  # Field name made lowercase.
    usuario_id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='USUARIO_ID_Usuario')  # Field name made lowercase.
    tipodocumento_venta = models.CharField(db_column='TipoDocumento_Venta', max_length=50)  # Field name made lowercase.
    numerodocumento_venta = models.CharField(db_column='NumeroDocumento_Venta', max_length=50)  # Field name made lowercase.
    nombrecliente = models.CharField(db_column='NombreCliente', max_length=50)  # Field name made lowercase.
    montopago_venta = models.DecimalField(db_column='MontoPago_Venta', max_digits=28, decimal_places=0)  # Field name made lowercase.
    montovuelto_venta = models.DecimalField(db_column='MontoVuelto_Venta', max_digits=28, decimal_places=0)  # Field name made lowercase.
    montototal_venta = models.DecimalField(db_column='MontoTotal_Venta', max_digits=28, decimal_places=0)  # Field name made lowercase.
    fecharegistroventa = models.DateField(db_column='FechaRegistroVenta')  # Field name made lowercase.

class CompraPaypal(models.Model):
    id = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=100)
    codigo_estado = models.CharField(max_length=100)
    producto = models.ForeignKey(ProductoElaborado, models.DO_NOTHING)
    total_de_la_compra = models.CharField(max_length=50)
    nombre_cliente  = models.CharField(max_length=100)
    apellido_cliente = models.CharField(max_length=100)
    correo_cliente = models.CharField(max_length=100)
    direccion_cliente = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_cliente

