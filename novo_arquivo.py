# Exercício.
# Faça um programa que percorra a palavra "Matheus" e coloque um * antes e depois de cada letra.
# Resultado esperado: *M**a**t**h**e**u**s*

nome = "Matheus"
indice = 0 
novo_nome = ""

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f"**{letra}"
    indice += 1

novo_nome += "*"
print(novo_nome)