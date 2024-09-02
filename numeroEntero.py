class numeroEntero:
    def MCD(self,a,b):
        x = abs(a)  # Tomar el valor absoluto para evitar problemas con números negativos
        y = abs(b)  # Tomar el valor absoluto para evitar problemas con números negativos

        while y != 0:
            remainder = x % y
            x = y
            y = remainder

        return x

    def MCM(self, a, b):
        return a*b/self.MCD(a, b)

if __name__ == '__main__':
    operacion = numeroEntero()
    print(f"MCD de {5} {10} es {operacion.MCD(5, 10)}")