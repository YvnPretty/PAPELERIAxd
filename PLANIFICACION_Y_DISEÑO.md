# Planificación y Diseño del Sistema de Papelería - BLOC-2

## 1. Casos de Uso
El sistema está diseñado para facilitar la interacción entre el empleado/administrador y las operaciones del negocio.

### Caso de Uso 1: Registro de Venta Directa
*   **Actor:** Vendedor / Empleado.
*   **Descripción:** El vendedor escanea los productos, el sistema calcula el total con IVA, se registra el pago y se descuenta automáticamente del inventario.
*   **Interacción:** El usuario ingresa a la pantalla de "Nueva Venta", agrega productos al carrito y finaliza con el botón de "Cobrar".

### Caso de Uso 2: Gestión de Stock y Alertas
*   **Actor:** Administrador.
*   **Descripción:** El sistema monitorea los niveles de stock. Cuando un producto llega al "mínimo establecido", envía una alerta visual.
*   **Interacción:** El administrador recibe una notificación en el tablero principal y genera una orden de compra sugerida.

---

## 2. Elaboración de Mockups
*   **Herramienta utilizada:** Se utilizó **Figma** para el diseño de alta fidelidad y bocetos a mano alzada para la arquitectura de información inicial.
*   **Proceso de elaboración:** 
    1.  **Sketching:** Dibujo preliminar de los módulos de ventas y catálogos.
    2.  **Wireframing:** Definición de la jerarquía de botones y formularios.
    3.  **Prototipado:** Creación de las pantallas finales (archivos .png presentes en el repositorio) que muestran la interfaz de usuario moderna.

---

## 3. Planificación del Proyecto (Cronograma)

| Etapa | Actividad | Tiempo Estimado |
| :--- | :--- | :--- |
| **Análisis** | Levantamiento de requerimientos y reglas de negocio | 1 semana |
| **Diseño** | Creación de casos de uso y mockups de interfaz | 4 días |
| **Desarrollo Base** | Configuración de base de datos y Backend | 2 semanas |
| **Frontend** | Implementación de módulos de ventas e inventario | 2 semanas |
| **Pruebas** | QA, corrección de errores y validación con usuario | 1 semana |
| **Despliegue** | Puesta en marcha y capacitación | 3 días |

---

## 4. Listado de Tareas (Reflejado en Jira)
Se han definido las siguientes tareas dentro del tablero de Jira bajo la épica del sistema de papelería:
1. **PAP-1:** Diseño de esquema de base de datos (Est. 4h).
2. **PAP-2:** Implementación de módulo de autenticación (Est. 6h).
3. **PAP-3:** Desarrollo de interfaz de punto de venta (Est. 12h).
4. **PAP-4:** Integración de API de facturación SAT (Est. 16h).
