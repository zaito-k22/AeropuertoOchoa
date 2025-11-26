class Reporte:
    _datos = {
        'ventas_mes': 125450000,
        'reservas_confirmadas': 150,
        'ocupacion_promedio': 87,
        'empleados_activos': 45,
        'reservas_pendientes': 23
    }

    @classmethod
    def get_datos(cls):
        return cls._datos