class Habitacion:
    def __init__(self, codigoHabitacion, numero, orientacion, ocupacion, idReserva, idHabitacion, idHuesped):
        self.__codigoHabitacion = codigoHabitacion
        self.__numero = numero
        self.__orientacion = orientacion
        self.__ocupacion = ocupacion
        self.__idReserva = idReserva
        self.__idHabitacion = idHabitacion
        self.__idHuesped = idHuesped
    
    def getCodigoHabitacion(self):
        return self.__codigoHabitacion
    
    def setCodigoHabitacion(self, codigoHabitacion):
        self.__codigoHabitacion = codigoHabitacion
    
    def getNumero(self):
        return self.__numero
    
    def setNumero(self, numero):
        self.__numero = numero
    
    def getOrientacion(self):
        return self.__orientacion
    
    def setOrientacion(self, orientacion):
        self.__orientacion = orientacion
    
    def getOcupacion(self):
        return self.__ocupacion
    
    def setOcupacion(self, ocupacion):
        self.__ocupacion = ocupacion
    
    def getIdReserva(self):
        return self.__idReserva
    
    def setIdReserva(self, idReserva):
        self.__idReserva = idReserva
    
    def getIdHabitacion(self):
        return self.__idHabitacion
    
    def setIdHabitacion(self, idHabitacion):
        self.__idHabitacion = idHabitacion
    
    def getIdHuesped(self):
        return self.__idHuesped
    
    def setIdHuesped(self, idHuesped):
        self.__idHuesped = idHuesped
    
    def __str__(self):
        cadena = ""
        cadena += f"Código de Habitación: {self.__codigoHabitacion}\n"
        cadena += f"Número: {self.__numero}\n"
        cadena += f"Orientación: {self.__orientacion}\n"
        cadena += f"Ocupación: {self.__ocupacion}\n"
        cadena += f"ID Reserva: {self.__idReserva}\n"
        cadena += f"ID Habitación: {self.__idHabitacion}\n"
        cadena += f"ID Huésped: {self.__idHuesped}\n"
        return cadena
