class OperasBas:
    'Declaracion de propiedades de clase'
    num1 = 0
    num2 = 0
    res = 0

    'Declaracion de propiedades de constructor'
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
        
    'Declaracion de propiedades de métodso'
    'Si la funcuion esta dentro de la clase poner self'
    def suma(self):
        self.res = self.num1 + self.num2
        print("La suma es: {}".format(self.res))

'No forma parte de la clase'
def main():
    obj = OperasBas(3, 4)
    'referencia a la operacopm'
    obj.suma()

if __name__ == "__main__":
    main()