"""
List Comprehensions (LC)

- Utilizando List Comprehensions nós podemos gerar novas listas com dados processados a partir de
outro iterável.

#  Sintaxe de LC

[ dado for dado in iterável ]

numeros = [1, 2, 3, 4, 5, 6]

res = [numero * 10 for numero in numeros]

print(res)


Para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:

- A primeira parte: for numero in numeros
- A segunda parte :numero * 10

res = [numero / 2 for numero in numeros]
print(res)

def quadrado(valor):
    return valor * valor

res = [quadrado(numero) for numero in numeros]
print(res)

#  LC versus Loop

# Loop
numeros = [1, 2, 3, 6, 8]

numeros_dobrados = []

for numero in numeros:
    res = numero * 2
    numeros_dobrados.append(res)

print(numeros_dobrados)

# List Comprehenions
print([numero * 2 for numero in numeros])

#  Outros exemplos:

# 1

nome = 'Heloisa Ferreira'
print([letra.upper() for letra in nome])

# 2

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['marte', 'breno', 'renan', 'olivia', 'pamela']

print([caixa_alta(amigo) for amigo in amigos])

# 3

print([(numero * 3) / 10 for numero in range(1, 10+1)])

# 4

print([bool(valor) for valor in [' ', [], 'a', 2, 2.5, 2*10]])

# 5

print([str(numero)  for numero in range(1, 5+1)])

Parte 2 - List Comprehensions

Nós podemos adicionar estruturas condicionais lógicas as nossas List Comprehensions

# Exemplo 1:

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

impares = [numero for numero in numeros if numero % 2 == 1]
print(impares)

#  Refatorando

#  Qualquer número que for par módulo de 2 é 0 e 0 em Pyhton é False. not False = True
pares = [numero for numero in numeros if not numero % 2]

#  Qualquer número ímpar módulo 2 é 1, e 1 em Python é True
impares = [numero for numero in numeros if numero % 2 == 1]

print(pares)
print(impares)

# Exemplo 2:

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)# Exemplo 1:

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

impares = [numero for numero in numeros if numero % 2 == 1]
print(impares)

#  Refatorando

#  Qualquer número que for par módulo de 2 é 0 e 0 em Pyhton é False. not False = True
pares = [numero for numero in numeros if not numero % 2]

#  Qualquer número ímpar módulo 2 é 1, e 1 em Python é True
impares = [numero for numero in numeros if numero % 2 == 1]

print(pares)
print(impares)

# Exemplo 2:

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
"""









