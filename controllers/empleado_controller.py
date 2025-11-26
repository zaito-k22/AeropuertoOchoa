from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.empleado import Empleado
from models.horario import Horario
from models.reporte import Reporte

empleado_bp = Blueprint('empleado', __name__, url_prefix='/empleado')

@empleado_bp.route('/')
def menu():
    return render_template('empleado_menu.html')

@empleado_bp.route('/horarios')
def horarios():
    horarios = Horario.get_all()
    return render_template('horarios.html', horarios=horarios)

@empleado_bp.route('/gestion-empleados', methods=['GET', 'POST'])
def gestion_empleados():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '')
        cargo = request.form.get('cargo', '')
        email = request.form.get('email', '')

        if nombre and cargo and email:
            Empleado.create(nombre=nombre, cargo=cargo, email=email)
            flash(f'Empleado "{nombre}" registrado exitosamente como {cargo}. (Simulación)', 'success')
            return redirect(url_for('empleado.gestion_empleados'))
        else:
            flash('Por favor complete todos los campos', 'error')

    empleados = Empleado.get_all()
    return render_template('gestion_empleados.html', empleados=empleados)

@empleado_bp.route('/reportes')
def reportes():
    reportes = Reporte.get_datos()
    return render_template('reportes.html', reportes=reportes)