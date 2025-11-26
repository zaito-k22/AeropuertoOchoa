from flask import Flask
from controllers.main_controller import main_bp
from controllers.cliente_controller import cliente_bp
from controllers.empleado_controller import empleado_bp

app = Flask(__name__)
app.secret_key = 'rapidoochoa_demo_key_2025'

# Registrar blueprints
app.register_blueprint(main_bp)
app.register_blueprint(cliente_bp)
app.register_blueprint(empleado_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)