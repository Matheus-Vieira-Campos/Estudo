"""
Exercício 3 — Difícil
Faça um programa que percorra a palavra "Brasil" e monte uma nova string onde cada letra é separada pelo seu índice (posição).
Resultado esperado: B0r1a2s3i4l5
"""

nome = "Brasil"
indice = 0 
novo_nome = ""

while indice < len(nome):
    letra = nome[indice]
    novo_nome += letra + str(indice)
    indice += 1

print(novo_nome)