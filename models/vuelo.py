class Vuelo:
    _vuelos = [
        {
            'numero': 'RO-123',
            'origen': 'Bogota (BOG)',
            'destino': 'Medellin (MDE)',
            'fecha': '2025-01-15',
            'hora_salida': '14:30',
            'hora_llegada': '15:45',
            'duracion': '1h 15m',
            'precio': 250000,
            'asientos': 45
        },
        {
            'numero': 'RO-124',
            'origen': 'Bogota (BOG)',
            'destino': 'Medellin (MDE)',
            'fecha': '2025-01-15',
            'hora_salida': '18:00',
            'hora_llegada': '19:15',
            'duracion': '1h 15m',
            'precio': 280000,
            'asientos': 32
        },
        {
            'numero': 'RO-125',
            'origen': 'Bogota (BOG)',
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
            'origen': 'Medellin (MDE)',
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
            'destino': 'Bogota (BOG)',
            'fecha': '2025-01-16',
            'hora_salida': '12:00',
            'hora_llegada': '13:30',
            'duracion': '1h 30m',
            'precio': 290000,
            'asientos': 40
        }
    ]

    @classmethod
    def get_all(cls):
        return cls._vuelos
    
    @classmethod
    def buscar(cls, origen=None, destino=None, fecha=None, pasajeros=1):
        vuelos_encontrados = []
        
        if origen and destino and fecha:
            for vuelo in cls._vuelos:
                origen_nombre = cls._get_ciudad_nombre(origen)
                destino_nombre = cls._get_ciudad_nombre(destino)

                if origen_nombre in vuelo['origen'] and destino_nombre in vuelo['destino']:
                    vuelos_encontrados.append({
                        **vuelo,
                        'total': vuelo['precio'] * pasajeros
                    })
        
        return vuelos_encontrados
    
    @classmethod
    def get_by_numero(cls, numero):
        for vuelo in cls._vuelos:
            if vuelo['numero'] == numero:
                return vuelo
        return None
    
    @staticmethod
    def _get_ciudad_nombre(codigo):
        ciudades = {
            'BOG': 'Bogota',
            'MDE': 'Medellin',
            'CLO': 'Cali',
            'BAQ': 'Barranquilla'
        }
        return ciudades.get(codigo, codigo)