def mod(a, b):
    while b:
        a, b = b, a % b
    return a

n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))
m = mod(n1, n2)

print(f"El Máximo Común Divisor entre {n1} y {n2} es {m}")
