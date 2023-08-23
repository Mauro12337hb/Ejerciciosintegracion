def get_int():
    while True:
        try:
            valor = int(input("Ingrese un valor entero: "))
            return valor
        except ValueError:
            print("Valor no válido. Inténtelo nuevamente.")


valor_entero = get_int()
print(f"Ha ingresado el valor entero: {valor_entero}")


#Forma Recursiva
def get_int():
    while True:
        try:
            valor = int(input("Ingrese un valor entero: "))
            return valor
        except ValueError:
            print("Valor no válido. Inténtelo nuevamente.")


valor_entero = get_int()
print(f"Ha ingresado el valor entero: {valor_entero}")
