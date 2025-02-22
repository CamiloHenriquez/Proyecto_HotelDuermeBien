class TipoHabitacion:
    def __init__(self, idHabitacion, numeroCamas, numeroPasajeros):
        self.__idHabitacion = idHabitacion
        self.__numeroCamas = numeroCamas
        self.__numeroPasajeros = numeroPasajeros
    
    def getIdHabitacion(self):
        return self.__idHabitacion
    
    def setIdHabitacion(self, idHabitacion):
        self.__idHabitacion = idHabitacion
    
    def getNumeroCamas(self):
        return self.__numeroCamas
    
    def setNumeroCamas(self, numeroCamas):
        self.__numeroCamas = numeroCamas
    
    def getNumeroPasajeros(self):
        return self.__numeroPasajeros
    
    def setNumeroPasajeros(self, numeroPasajeros):
        self.__numeroPasajeros = numeroPasajeros
    
    def __str__(self):
        cadena = ""
        cadena += f"ID Habitación: {self.__idHabitacion}\n"
        cadena += f"Número de Camas: {self.__numeroCamas}\n"
        cadena += f"Número de Pasajeros: {self.__numeroPasajeros}\n"
        return cadena
