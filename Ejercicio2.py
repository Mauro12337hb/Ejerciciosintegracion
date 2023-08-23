def mcm (a,b):
    c= max(a,b)
    
    while True:
        if (c% a==0) and (c% b==0):
            return c
        
        c+=1


n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))
resultado = mcm(n1, n2)
print(f"El Minimo Común Divisor entre {n1} y {n2} es {resultado}")
