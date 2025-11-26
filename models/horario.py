class Horario:
    _horarios = [
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

    @classmethod
    def get_all(cls):
        return cls._horarios