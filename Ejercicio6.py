class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print("La edad no puede ser un valor negativo.")

    def set_dni(self, dni):
        if len(dni) == 9:
            self.__dni = dni
        else:
            print("El DNI debe tener 9 caracteres.")

    # Getters
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

    def es_mayor_de_edad(self):
        return self.__edad >= 18

class Cuenta:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo

    # Setter y Getter para el saldo
    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def mostrar(self):
        print(f"Titular de la cuenta: {self.__titular.get_nombre()}")
        print(f"Saldo de la cuenta: {self.__saldo}")

# Ejemplo de uso:
if __name__ == "__main__":
    persona1 = Persona("Juan Pérez", 25, "123456789")
    cuenta1 = Cuenta(persona1, 1000)

    persona1.mostrar()
    cuenta1.mostrar()

    print(f"{persona1.get_nombre()} es mayor de edad: {persona1.es_mayor_de_edad()}")

