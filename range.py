"""
Função Range:

- Precisamos conhecer o loop para utilizar o range
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória, mas sim
de maneira especificada.

#  Forma 1:

range -> (valor_de_parada)

for num in range(11):
    print(num)

# Forma 2:

range -> (valor_de_inicio, valor_de_parada)

for num in range (1, 11):
    print(num)

# Forma 3:

range -> (valor_de_inicio, valor_de_parada, passo(ex: 5 em 5)

for num in range (5, 50, 5):
    print(num)

# Forma 4:

range -> (valor_de_inicio, valor_de_parada, passo(ex: contagem regressiva) 20 19 18 17...

for num in range (20, -1, -1):
    print(num)

"""