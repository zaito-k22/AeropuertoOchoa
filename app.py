from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'rapidoochoa_demo_key_2025'

# Datos de ejemplo - Vuelos disponibles
VUELOS_EJEMPLO = [
    {
        'numero': 'RO-123',
        'origen': 'Bogotá (BOG)',
        'destino': 'Medellín (MDE)',
        'fecha': '2025-01-15',
        'hora_salida': '14:30',
        'hora_llegada': '15:45',
        'duracion': '1h 15m',
        'precio': 250000,
        'asientos': 45
    },
    {
        'numero': 'RO-124',
        'origen': 'Bogotá (BOG)',
        'destino': 'Medellín (MDE)',
        'fecha': '2025-01-15',
        'hora_salida': '18:00',
        'hora_llegada': '19:15',
        'duracion': '1h 15m',
        'precio': 280000,
        'asientos': 32
    },
    {
        'numero': 'RO-125',
        'origen': 'Bogotá (BOG)',
        'destino': 'Cali (CLO)',
        'fecha': '2025-01-15',
        'hora_salida': '10:00',
        'hora_llegada': '11:30',
        'duracion': '1h 30m',
        'precio': 300000,
        'asientos': 28
    },
    {
        'numero': 'RO-126',
        'origen': 'Medellín (MDE)',
        'destino': 'Barranquilla (BAQ)',
        'fecha': '2025-01-15',
        'hora_salida': '16:00',
        'hora_llegada': '17:45',
        'duracion': '1h 45m',
        'precio': 320000,
        'asientos': 15
    },
    {
        'numero': 'RO-127',
        'origen': 'Cali (CLO)',
        'destino': 'Bogotá (BOG)',
        'fecha': '2025-01-16',
        'hora_salida': '12:00',
        'hora_llegada': '13:30',
        'duracion': '1h 30m',
        'precio': 290000,
        'asientos': 40
    }
]

# Datos de ejemplo - Reservas
RESERVAS_EJEMPLO = [
    {
        'codigo': 'RO-2025-001',
        'estado': 'Confirmada',
        'origen': 'Bogotá (BOG)',
        'destino': 'Medellín (MDE)',
        'fecha': '15 de Enero, 2025',
        'hora_salida': '14:30',
        'hora_llegada': '15:45',
        'numero_vuelo': 'RO-123',
        'asiento': '12A',
        'pasajeros': 1
    },
    {
        'codigo': 'RO-2025-002',
        'estado': 'Pendiente',
        'origen': 'Cali (CLO)',
        'destino': 'Barranquilla (BAQ)',
        'fecha': '20 de Enero, 2025',
        'hora_salida': '10:00',
        'hora_llegada': '11:30',
        'numero_vuelo': 'RO-456',
        'asiento': '8B',
        'pasajeros': 1
    }
]

# Datos de ejemplo - Empleados
EMPLEADOS_EJEMPLO = [
    {
        'id': 'EMP-2025-001',
        'nombre': 'Carlos Rodríguez',
        'cargo': 'Piloto',
        'email': 'carlos.rodriguez@rapidoochoa.com',
        'avatar': '👨‍✈️'
    },
    {
        'id': 'EMP-2025-002',
        'nombre': 'María González',
        'cargo': 'Tripulación',
        'email': 'maria.gonzalez@rapidoochoa.com',
        'avatar': '👩‍✈️'
    },
    {
        'id': 'EMP-2025-003',
        'nombre': 'Pedro Martínez',
        'cargo': 'Recepcionista',
        'email': 'pedro.martinez@rapidoochoa.com',
        'avatar': '👨‍💼'
    }
]

# Datos de ejemplo - Horarios
HORARIOS_EJEMPLO = [
    {
        'dia': 15,
        'mes': 'Ene',
        'vuelo': 'RO-123',
        'ruta': 'Bogotá → Medellín',
        'hora_reporte': '13:00',
        'hora_salida': '14:30',
        'aeronave': 'N123RO',
        'estado': 'Asignado'
    },
    {
        'dia': 18,
        'mes': 'Ene',
        'vuelo': 'RO-456',
        'ruta': 'Medellín → Cali',
        'hora_reporte': '08:00',
        'hora_salida': '09:30',
        'aeronave': 'N456RO',
        'estado': 'Asignado'
    },
    {
        'dia': 22,
        'mes': 'Ene',
        'vuelo': None,
        'ruta': 'Día Libre',
        'hora_reporte': None,
        'hora_salida': None,
        'aeronave': None,
        'estado': 'Libre'
    }
]

# Datos de ejemplo - Reportes
REPORTES_EJEMPLO = {
    'ventas_mes': 125450000,
    'reservas_confirmadas': 150,
    'ocupacion_promedio': 87,
    'empleados_activos': 45,
    'reservas_pendientes': 23
}

# Función auxiliar para obtener nombre de ciudad
def get_ciudad_nombre(codigo):
    ciudades = {
        'BOG': 'Bogotá',
        'MDE': 'Medellín',
        'CLO': 'Cali',
        'BAQ': 'Barranquilla'
    }
    return ciudades.get(codigo, codigo)

# Ruta principal - Selección de rol
@app.route('/')
def index():
    return render_template('index.html')

# Rutas de Cliente
@app.route('/cliente')
def cliente_menu():
    return render_template('cliente_menu.html')

@app.route('/cliente/buscar-vuelos', methods=['GET', 'POST'])
def buscar_vuelos():
    vuelos_encontrados = []
    
    if request.method == 'POST':
        origen = request.form.get('origen', '')
        destino = request.form.get('destino', '')
        fecha = request.form.get('fecha_salida', '')
        pasajeros = int(request.form.get('pasajeros', 1))
        
        if origen and destino and fecha:
            # Filtrar vuelos
            for vuelo in VUELOS_EJEMPLO:
                origen_nombre = get_ciudad_nombre(origen)
                destino_nombre = get_ciudad_nombre(destino)
                
                if origen_nombre in vuelo['origen'] and destino_nombre in vuelo['destino']:
                    vuelos_encontrados.append({
                        **vuelo,
                        'total': vuelo['precio'] * pasajeros
                    })
        else:
            flash('Por favor complete todos los campos requeridos', 'error')
    
    return render_template('buscar_vuelos.html', 
                         vuelos=vuelos_encontrados,
                         origen_seleccionado=request.form.get('origen', ''),
                         destino_seleccionado=request.form.get('destino', ''),
                         fecha_seleccionada=request.form.get('fecha_salida', ''),
                         pasajeros_seleccionados=request.form.get('pasajeros', '1'))

@app.route('/cliente/mis-reservas')
def mis_reservas():
    return render_template('mis_reservas.html', reservas=RESERVAS_EJEMPLO)

@app.route('/cliente/perfil')
def perfil_cliente():
    return render_template('perfil_cliente.html')

@app.route('/cliente/reservar/<vuelo_numero>')
def reservar_vuelo(vuelo_numero):
    # Buscar el vuelo
    vuelo = next((v for v in VUELOS_EJEMPLO if v['numero'] == vuelo_numero), None)
    if vuelo:
        flash(f'Reserva del vuelo {vuelo_numero} realizada exitosamente! (Simulación)', 'success')
    return redirect(url_for('buscar_vuelos'))

# Rutas de Empleado
@app.route('/empleado')
def empleado_menu():
    return render_template('empleado_menu.html')

@app.route('/empleado/horarios')
def horarios():
    return render_template('horarios.html', horarios=HORARIOS_EJEMPLO)

@app.route('/empleado/gestion-empleados', methods=['GET', 'POST'])
def gestion_empleados():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '')
        cargo = request.form.get('cargo', '')
        email = request.form.get('email', '')
        
        if nombre and cargo and email:
            flash(f'Empleado "{nombre}" registrado exitosamente como {cargo}. (Simulación)', 'success')
            return redirect(url_for('gestion_empleados'))
        else:
            flash('Por favor complete todos los campos', 'error')
    
    return render_template('gestion_empleados.html', empleados=EMPLEADOS_EJEMPLO)

@app.route('/empleado/reportes')
def reportes():
    return render_template('reportes.html', reportes=REPORTES_EJEMPLO)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

