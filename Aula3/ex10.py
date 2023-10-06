palavra = str(input("digite uma palavra: "))

invertida = palavra[::-1]

if palavra == invertida:
    print("é um palindromo")

else:
    print("não é um palindromo")