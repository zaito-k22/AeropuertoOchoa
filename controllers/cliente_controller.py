from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.vuelo import Vuelo
from models.reserva import Reserva

cliente_bp = Blueprint('cliente', __name__, url_prefix='/cliente')

@cliente_bp.route('/')
def menu():
    return render_template('cliente_menu.html')


@cliente_bp.route('/buscar-vuelos', methods=['GET', 'POST'])
def buscar_vuelos():
    vuelos_encontrados = []

    if request.method == 'POST':
        origen = request.form.get('origen', '')
        destino = request.form.get('destino', '')
        fecha = request.form.get('fecha_salida', '')
        pasajeros = int(request.form.get('pasajeros', 1))

        if origen and destino and fecha:
            vuelos_encontrados = Vuelo.buscar(
                origen=origen,
                destino=destino,
                fecha=fecha,
                pasajeros=pasajeros
            )
        else:
            flash('Por favor complete todos los campos requeridos', 'error')

    return render_template('buscar_vuelos.html',
                         vuelos=vuelos_encontrados,
                         origen_seleccionado=request.form.get('origen', ''),
                         destino_seleccionado=request.form.get('destino', ''),
                         fecha_seleccionada=request.form.get('fecha_salida', ''),
                         pasajeros_seleccionados=request.form.get('pasajeros', '1'))

@cliente_bp.route('/mis-reservas')
def mis_reservas():
    reservas = Reserva.get_all()
    return render_template('mis_reservas.html', reservas=reservas)

@cliente_bp.route('/perfil')
def perfil_cliente():
    return render_template('perfil_cliente.html')

@cliente_bp.route('/reservar/<vuelo_numero>')
def reservar_vuelo(vuelo_numero):
    vuelo = Vuelo.get_by_numero(vuelo_numero)
    if vuelo:
        flash(f'Reserva del vuelo {vuelo_numero} realizada exitosamente! (Simulación)', 'success')
    return redirect(url_for('cliente.buscar_vuelos'))