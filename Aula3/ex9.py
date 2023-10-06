soma = 0

palavra = "casa"

for letra in palavra:
    if letra not in "aeiou":
        soma = soma + 1
print(soma)