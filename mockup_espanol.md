# Gestión de Inventario - Papelería

Organiza los productos faltantes y pedidos de clientes para mantener tu stock actualizado.

## Introducción
Esta interfaz ha sido diseñada para facilitar el control de inventario en una papelería. Su objetivo principal es permitir a los propietarios y empleados organizar eficientemente dos aspectos fundamentales del negocio: los productos que se han agotado (o están a punto de hacerlo) y los pedidos específicos que realizan los clientes. A través de un panel administrativo moderno y limpio, el usuario puede mantener su stock actualizado garantizando una gestión fluida.

## Cómo construimos el mockup
Para desarrollar esta interfaz, tomamos una serie de decisiones técnicas y de diseño orientadas a la simplicidad y la usabilidad:

*   **React con useState y useEffect:** Elegimos React por su capacidad para manejar interfaces dinámicas. Utilizamos `useState` para crear listas interactivas y `useEffect` para reaccionar a los cambios de estado.
*   **Separación entre productos y pedidos:** Hemos dividido la información en dos categorías lógicas: "Productos faltantes" para venta regular y "Pedidos nuevos" para encargos de clientes, evitando confusión visual.
*   **Pestañas para cambiar de vista:** Implementamos un sistema de pestañas (Tabs) tipo botón ('pill') que permite concentrarse en una sola tarea manteniendo la interfaz minimalista.
*   **localStorage para persistencia:** Conectamos el estado de la aplicación con el navegador. Así, la información perdura de forma local sin necesidad de configurar una base de datos externa.
*   **Botón de exportación:** Incorporamos una acción global destacada en verde para exportar los datos, una función vital en el entorno comercial.
*   **Iconos y jerarquía visual:** Utilizamos iconos representativos, fondos claros, bordes suaves y tarjetas estructuradas para guiar la vista hacia el contenido importante.

## Estructura visual del mockup

1.  **Encabezado:** Título grande y claro acompañado de un subtítulo descriptivo que contextualiza rápidamente la herramienta.
2.  **Navegación por Pestañas:** Diseño en formato 'pill' interactivo, donde el color azul vivo indica la sección activa frente al fondo blanco inactivo.
3.  **Panel de Productos Faltantes:** Tarjeta principal expansiva que contiene listas de inventario o un estado vacío claro y amigable.
4.  **Panel de Pedidos Nuevos:** Vista alternativa estructurada para listar los requerimientos específicos solicitados por clientes directos.
5.  **Acción de Exportar:** Botón superior derecho contrastante (verde) para generar reportes de manera accesible e inmediata.

## Flujo de uso

1.  **Revisión:** El encargado inspecciona el local y abre la pestaña de faltantes.
2.  **Registro:** Anota los productos que se agotan y clasifica su urgencia.
3.  **Atención:** En la segunda pestaña, toma nota de los encargos de clientes.
4.  **Exportación:** Al final del día, pulsa "Exportar a PDF" para el proveedor.

## Ejemplo de productos y prioridades

*   **Cuadernos A4 Cuadriculados:** Sin stock disponible (Prioridad: **ALTA**)
*   **Bolígrafos Azules (Caja x50):** Quedan 2 unidades (Prioridad: **MEDIA**)
*   **Gomas de borrar:** En stock, pero bajo (Prioridad: **BAJA**)

## Código Principal (React + Tailwind)

```tsx
import React, { useState, useEffect } from "react";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Package, ShoppingCart, Download, Plus } from "lucide-react";

interface ProductoFaltante {
  id: string;
  nombre: string;
  enStock: boolean;
  urgencia: "baja" | "media" | "alta";
  foto?: string;
}

interface PedidoNuevo {
  id: string;
  nombreProducto: string;
  cantidadSolicitada: number;
}

export default function AppInventario() {
  const [productosFaltantes, setProductosFaltantes] = useState<ProductoFaltante[]>([]);
  const [pedidosNuevos, setPedidosNuevos] = useState<PedidoNuevo[]>([]);

  // Cargar datos desde localStorage al montar el componente
  useEffect(() => {
    const faltantesGuardados = localStorage.getItem("productosFaltantes");
    if (faltantesGuardados) {
      setProductosFaltantes(JSON.parse(faltantesGuardados));
    }

    const pedidosGuardados = localStorage.getItem("pedidosNuevos");
    if (pedidosGuardados) {
      setPedidosNuevos(JSON.parse(pedidosGuardados));
    }
  }, []);

  // Guardar en localStorage cuando cambian los datos
  useEffect(() => {
    localStorage.setItem("productosFaltantes", JSON.stringify(productosFaltantes));
    localStorage.setItem("pedidosNuevos", JSON.stringify(pedidosNuevos));
  }, [productosFaltantes, pedidosNuevos]);

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-6xl mx-auto">
        <header className="mb-8 flex justify-between items-start">
          <div>
            <h1 className="text-4xl font-bold text-gray-900 mb-2">
              Gestión de Inventario - Papelería
            </h1>
            <p className="text-gray-600">
              Organiza productos faltantes y pedidos de clientes para mantener tu stock actualizado.
            </p>
          </div>
          <button className="bg-emerald-600 hover:bg-emerald-700 text-white px-4 py-2 rounded-lg flex items-center gap-2 transition-colors">
            <Download className="w-4 h-4" />
            Exportar a PDF
          </button>
        </header>

        <Tabs defaultValue="faltantes" className="w-full">
          <div className="flex justify-between items-center mb-6">
            <TabsList className="bg-white border p-1 h-12">
              <TabsTrigger value="faltantes" className="flex items-center gap-2 px-6">
                <Package className="w-4 h-4" />
                Productos Faltantes
              </TabsTrigger>
              <TabsTrigger value="pedidos" className="flex items-center gap-2 px-6">
                <ShoppingCart className="w-4 h-4" />
                Pedidos Nuevos
              </TabsTrigger>
            </TabsList>
            
            <button className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg flex items-center gap-2">
              <Plus className="w-4 h-4" />
              Agregar Item
            </button>
          </div>

          <TabsContent value="faltantes" className="mt-0">
            <div className="bg-white border rounded-xl p-8 min-h-[400px] flex flex-col items-center justify-center text-gray-500">
              {productosFaltantes.length === 0 ? (
                <p>No hay productos faltantes registrados.</p>
              ) : (
                <div className="w-full grid gap-4">
                  {/* Aquí iría la lista de productos */}
                </div>
              )}
            </div>
          </TabsContent>

          <TabsContent value="pedidos" className="mt-0">
            <div className="bg-white border rounded-xl p-8 min-h-[400px] flex flex-col items-center justify-center text-gray-500">
              {pedidosNuevos.length === 0 ? (
                <p>No hay pedidos nuevos registrados.</p>
              ) : (
                <div className="w-full grid gap-4">
                  {/* Aquí iría la lista de pedidos */}
                </div>
              )}
            </div>
          </TabsContent>
        </Tabs>
      </div>
    </div>
  );
}
```
