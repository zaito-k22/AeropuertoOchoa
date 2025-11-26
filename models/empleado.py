class Empleado:
    _empleados = [
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

    @classmethod
    def get_all(cls):
        return cls._empleados
    
    @classmethod
    def create(cls, nombre, cargo, email):
        nuevo_id = f"EMP-2025-{len(cls._empleados) + 1:03d}"
        nuevo_empleado = {
            'id': nuevo_id,
            'nombre': nombre,
            'cargo': cargo,
            'email': email,
            'avatar': '👨‍💼'  # Avatar por defecto
        }
        cls._empleados.append(nuevo_empleado)
        return nuevo_empleado