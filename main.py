class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):
        color = color.lower()
        if color == "rojo":
            self.color = color
            
        elif color == "verde":
            self.color = color
        
        elif color == "amarillo":
            self.color = color
        
        elif color == "negro":
            self.color = color

        elif color == "blanco":
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro
    def asignarTipo(self, tipo):
        tipo = tipo.lower()
        if tipo == "gasolina":
            self.tipo = tipo
        elif tipo == "electrico":
            self.tipo = tipo

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    
    def cantidadAsientos(self):
        contador = 0
        for n in self.asientos:
            if n != None:
                cont+=1
        return contador
    
    def verificarIntegridad(self):
        valido = self.registro == self.motor.registro
        if(valido):
            for asiento in self.asientos:
                if asiento != None:
                    if(asiento.registro!= self.registro):
                        valido = False
                        break
        return "Auto original" if valido else "Las piezas no son originales"