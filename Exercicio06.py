quadrado = lambda numero: numero ** 2
triplo = lambda numero: numero ** 3
numero = int(input("Digite um Número:"))
numeroQ = quadrado(numero)
numeroT = triplo(numero)
print(numero, "Ao Quadrado é:", numeroQ)
print(numero, "Ao Triplo é:", numeroT)
