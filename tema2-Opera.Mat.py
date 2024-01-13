num1 = 20
num2 = 4

print("La suma es: ", (num1+num2))
print("La resta es: ", (num1-num2))
print("La multiplación es: ", (num1*num2))
print("La división exacta es: ", (num1//num2))
print("La división es: ", (num1/num2))
print("La potencia es: ", (num1 ** num2))


#Concatenacion en python

texto = "hola"
texto2 = "mundo"
textoFinal = texto + " " + texto2
print(textoFinal)
print("El saludo es: %s %s" %(texto,texto2))
saludoFinal = "Saludo {} {}".format(texto,texto2)
print(saludoFinal)

sueldoFinal2 = "Saludo2: {y} {x}".format(x=texto, y=texto2)
print(sueldoFinal2)