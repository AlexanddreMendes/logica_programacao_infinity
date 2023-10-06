maior_numero = 0
for i in range(1,6):
    numero = float(input(f"digite o {i}º número: "))
    if numero > maior_numero:
        maior_numero = numero

print(maior_numero)

