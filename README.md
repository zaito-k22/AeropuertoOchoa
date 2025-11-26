# RápidoOchoa - Prototipo de Sistema de Gestión de Aerolínea

Prototipo funcional para exposición de 10 minutos del sistema de gestión de aerolínea RápidoOchoa, desarrollado con Python y Flask.

## Características

### Pantalla Inicial
- Selección de tipo de usuario (Cliente o Empleado)

### Menú Cliente
- **Buscar Vuelos**: Búsqueda de vuelos por origen, destino, fecha y número de pasajeros con resultados en tiempo real
- **Mis Reservas**: Visualización de reservas existentes con estados (Confirmada/Pendiente)
- **Mi Perfil**: Información del perfil del cliente

### Menú Empleado
- **Mis Horarios**: Visualización de horarios de vuelo asignados con detalles
- **Gestión de Empleados**: Lista de empleados con opciones de gestión y registro de nuevos empleados
- **Reportes**: Dashboard con estadísticas clave (Ventas, Ocupación, Empleados, Reservas)

## Requisitos

- Python 3.7 o superior
- Flask (se instala automáticamente con requirements.txt)

## Instalación

1. Asegúrate de tener Python instalado en tu sistema
2. Instala las dependencias:
```bash
python -m pip install -r requirements.txt
```

## Cómo Ejecutar

1. Abre una terminal en la carpeta del proyecto
2. Ejecuta la aplicación:
```bash
python app.py
```

3. Abre tu navegador y ve a:
```
http://localhost:5000
```

## Estructura del Proyecto

```
Aeropuerto/
├── app.py                 # Aplicación Flask principal
├── requirements.txt        # Dependencias de Python
├── README.md              # Este archivo
├── templates/             # Plantillas HTML
│   ├── base.html         # Plantilla base
│   ├── index.html        # Página de selección de rol
│   ├── cliente_menu.html # Menú de cliente
│   ├── buscar_vuelos.html
│   ├── mis_reservas.html
│   ├── perfil_cliente.html
│   ├── empleado_menu.html # Menú de empleado
│   ├── horarios.html
│   ├── gestion_empleados.html 
│   └── reportes.html
└── static/               # Archivos estáticos
    └── styles.css       # Estilos CSS
```

## Tecnologías Utilizadas

- **Python 3**: Lenguaje de programación
- **Flask**: Framework web ligero
- **Jinja2**: Motor de plantillas (incluido con Flask)
- **HTML5/CSS3**: Frontend

## Notas

- Este es un prototipo de demostración, no incluye base de datos real
- Los datos mostrados son de ejemplo almacenados en memoria
- Diseñado para una presentación de 10 minutos
- Interfaz responsive y moderna
- No requiere JavaScript complejo, toda la lógica está en Python

## Funcionalidades Implementadas

✅ Selección de rol (Cliente/Empleado)  
✅ Búsqueda de vuelos con filtros  
✅ Visualización de reservas  
✅ Perfil de cliente  
✅ Horarios de empleados  
✅ Gestión de empleados (listar y registrar)  
✅ Dashboard de reportes  
✅ Mensajes de confirmación/error  

## Para Desarrollo

Si quieres modificar el código:
- Los datos de ejemplo están en `app.py` (VUELOS_EJEMPLO, RESERVAS_EJEMPLO, etc.)
- Los estilos están en `static/styles.css`
- Las plantillas HTML están en `templates/`
