from numeroEntero import numeroEntero

if __name__ == '__main__':
    numero1 = int(input("Primer número:  "))
    numero2 = int(input("Segundo número: "))

    operacion = numeroEntero()
    print(f"MCD de {numero1} {numero2} es {operacion.MCD(numero1, numero2)}")
    print(f"MCM de {numero1} {numero2} es {operacion.MCM(numero1, numero2)}")