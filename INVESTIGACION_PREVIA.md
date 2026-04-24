# Investigacion Previa: Analisis de una Papeleria

Este documento detalla el funcionamiento basico de una papeleria tradicional en Mexico y los procesos que se deben considerar para el desarrollo del software.

# Descripcion General del Negocio

- Tipo de Negocio: Papeleria urbana mediana enfocada en articulos escolares y oficina.
- Publico Objetivo: Estudiantes, padres de familia, maestros y pequeños negocios.
- Servicios Adicionales: Fotocopiado, impresiones, enmicado y engargolado.

# Actores del Negocio

- Dueño o Gerente: Administra finanzas, compras y politicas de precio.
- Cajeros: Realizan ventas, cobran y atienden dudas en el mostrador.
- Proveedores: Distribuidores mayoristas de marcas de papeleria.
- Clientes: Personas fisicas o empresas que requieren productos o servicios.
- Autoridades: SAT (facturacion e impuestos) y gobierno municipal (licencias).

# Procesos Basicos Identificados

# 1. Ventas y Atencion al Cliente
- Escaneo de productos por codigo de barras o busqueda manual.
- Suma de servicios adicionales (copias, impresiones).
- Aplicacion de descuentos por volumen (por ejemplo, compra de cajas de hojas).
- Recepcion de pagos en efectivo, tarjeta o transferencias digitales.

# 2. Gestion de Inventarios
- Registro de entrada de mercancia nueva.
- Control de existencias actuales (stock).
- Alerta automatica cuando un producto llega a su nivel minimo.
- Registro de mermas o productos dañados que no se pueden vender.

# 3. Facturacion y Obligaciones Fiscales
- Generacion de facturas individuales CFDI 4.0 cuando el cliente lo solicita.
- Creacion de la factura global diaria por ventas al publico en general.
- Registro de impuestos aplicables (IVA en productos gravados).

# 4. Compras a Proveedores
- Lista de productos faltantes segun el nivel de stock.
- Comparacion de precios entre diferentes proveedores.
- Registro de facturas de compra para control de gastos.

# Reglas de Negocio Preliminares

- Emision Obligatoria: Toda venta debe generar un ticket o factura segun la ley.
- Politica de Devoluciones: Solo se aceptan devoluciones con ticket de compra.
- Stock Minimo: Los productos de alta rotacion deben tener una alerta de reabastecimiento.
- Servicios Digitales: Las impresiones solo se realizan si el archivo es legible.

# Preguntas para Profundizar en el Analisis

- ¿Como se registran actualmente las copias e impresiones si no tienen codigo de barras?
- ¿Cual es el criterio para decidir cuando un producto necesita reabastecimiento?
- ¿Que metodos de pago son los mas utilizados por los clientes actuales?
- ¿Como se maneja el corte de caja si hay varios empleados en diferentes turnos?
