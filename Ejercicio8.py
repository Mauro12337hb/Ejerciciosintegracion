class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    # Setters y Getters de Persona
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad

    def set_dni(self, dni):
        self.__dni = dni

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_dni(self):
        return self.__dni

    def mostrar(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"DNI: {self.__dni}")

class Cuenta:
    def __init__(self, titular=None, cantidad=0.0):
        if titular is None:
            self.__titular = Persona()
        else:
            self.__titular = titular
        self.__cantidad = cantidad

    # Getter y Setter de Cuenta
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def get_cantidad(self):
        return self.__cantidad

    def mostrar(self):
        print("Datos de la cuenta:")
        self.__titular.mostrar()
        print(f"Cantidad en la cuenta: {self.__cantidad}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad


if __name__ == "__main__":
    titular = Persona("Juan Pérez", 30, "123456789")
    cuenta = Cuenta(titular, 1000.0)

    cuenta.mostrar()
    
    cuenta.ingresar(500.0)
    cuenta.retirar(200.0)
    
    cuenta.mostrar()


class CuentaJoven(Cuenta):
    def __init__(self, titular=None, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    # Setter y Getter de bonificacion
    def set_bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def get_bonificacion(self):
        return self.__bonificacion

    def es_titular_valido(self):
        edad = self._Cuenta__titular.get_edad()
        return edad >= 18 and edad < 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("No es posible retirar dinero. El titular no es válido.")

    def mostrar(self):
        super().mostrar()
        print(f"Tipo de cuenta: Cuenta Joven")
        print(f"Bonificación: {self.__bonificacion}%")
