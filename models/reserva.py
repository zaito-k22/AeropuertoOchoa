class Reserva:
    _reservas = [
        {
            'codigo': 'RO-2025-001',
            'estado': 'Confirmada',
            'origen': 'Bogota (BOG)',
            'destino': 'Medellin (MDE)',
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

    @classmethod
    def get_all(cls):
        return cls._reservas