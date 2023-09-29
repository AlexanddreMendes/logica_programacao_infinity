nota_p1 = float(input("digite nota parcial 1: "))

nota_p2 = float(input("digite nota parcial 2: "))

media = (nota_p1 + nota_p2) /2

if media >= 7 and media < 10:
    print("foi aprovado")
elif media < 7:
    print("foi reprovado")

else: 
    print("aprovado com distinção")
    