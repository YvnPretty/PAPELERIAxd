# Reglas de Negocio: Papeleria

Este documento define las normas, politicas y restricciones que el sistema de software debe implementar para garantizar la correcta operacion del negocio.

# Politicas de Venta y Cobro

- Registro de Ventas: Toda transaccion debe quedar registrada en el sistema con fecha, hora y el empleado que la realizo.
- Metodos de Pago: El sistema debe permitir pagos combinados (por ejemplo, una parte en efectivo y otra con tarjeta).
- Descuentos: Solo el gerente puede aplicar descuentos directos mayores al 10 por ciento sobre el total de la venta.
- Tickets: El sistema debe generar un ticket de venta automaticamente al finalizar cada transaccion.

# Politicas de Facturacion (CFDI)

- Solicitud de Factura: El cliente tiene hasta el ultimo dia del mes en curso para solicitar la factura de su ticket de compra.
- Datos Fiscales: Es obligatorio capturar el RFC, Regimen Fiscal y Codigo Postal exactos segun la Constancia de Situacion Fiscal.
- Factura Global: Al final del dia, todas las ventas que no fueron facturadas individualmente deben agruparse en una factura global al publico en general.

# Gestion de Inventarios y Productos

- Stock Minimo: Cada producto debe tener un valor de stock minimo. Si el inventario cae por debajo de este valor, el sistema debe mostrar una alerta visual.
- Precios de Venta: El precio de venta debe ser siempre mayor al costo de adquisicion mas un margen minimo de utilidad definido por la gerencia.
- Unidades de Medida: El sistema debe permitir la venta por unidad (una pluma) o por paquete (caja de 12 plumas) con precios diferenciados.
- Inventario Negativo: El sistema no debe permitir realizar ventas de productos con stock en cero, a menos que se trate de servicios (copias, impresiones).

# Reglas para Servicios Especiales

- Costo de Impresion: El precio de la impresion dependera del tipo de archivo (color o blanco y negro) y del tamaño de papel (carta, oficio).
- Anticipos: Para trabajos especiales como engargolados de gran volumen o laminados, se debe requerir un anticipo minimo del 50 por ciento.

# Devoluciones y Garantias

- Plazo de Devolucion: Se aceptan cambios o devoluciones dentro de los primeros 30 dias naturales despues de la compra.
- Estado del Producto: No se aceptan devoluciones de productos que hayan sido abiertos, usados o dañados (por ejemplo, cuadernos con hojas arrancadas).
- Comprobante: Es requisito indispensable presentar el ticket original para cualquier proceso de cambio.

# Horarios y Seguridad

- Corte de Caja: Al final de cada turno, el empleado debe realizar un cierre de caja comparando el efectivo fisico contra el registro del sistema.
- Roles de Usuario: Los cajeros solo tienen acceso a realizar ventas. Solo el gerente puede modificar inventarios o ver reportes financieros.
