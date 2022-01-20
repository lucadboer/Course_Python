"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer geralmente temos:

entrada -> processamento -> saída

Se a gente pensar em uma função , já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída.

#  Refatorando uma função

def quadrado(num):
    return num * num
    # return num ** 2

print(quadrado(5))
print(quadrado(7))
print(quadrado(10))

ret = quadrado(8)
print(ret)

#  Refatorando a função

def cantar_parabens(niver):
    print('FELIZ ANIVERSÁRIO KARALHOOOO')
    print('TUDO DE BOM PRA VOCÊ')
    print(f'TAMO JUNTO {niver}')

niver = input('Qual o nome dele?\n')

cantar_parabens(niver)

#  Funções podem ter n parâmetros de entrada, ou seja, podemos receber como entrada em uma função
#  quantos parâmetros forem necessários. Eles são separados por vírgula.

#  Exemplos:

def soma(a, b):
    return a + b

def mult(a, b):
    return a * b

a = int(input("Digite o número 'a' por favor"))
b = int(input("Digite o número 'b' por favor"))

print(f'A soma desses números é = {soma(a, b)}')
print(f'A multiplicação desses números é = {mult(a, b)}')

#  Nomeando parâmetros

#  Erro comum na utilização de parâmetro

def soma_pares(tuple):
    total = 0
    for n in tuple:
        if n % 2 == 0:
            total += n
    return total  # Certo
    #   return total - Errado

tuple = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

print(soma_pares(tuple))
"""

