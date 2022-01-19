"""
Funções com retorno

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno do pop: {ret_pop}')

ret_print = print(numeros)  # Função print() não retorna nada

print(f'Retorno de print: {ret_print}')

OBS: Em Python, quando uma função não reotrna nenhum valor, o retorno é None

OBS: Funções Python que retornam valores, devem retornar estes valores com a
palavra reservada "return"

OBS: Não precisamos necessariamente criar uma variável para receber retorno
de uma função. Podemos passar a execução da função para outras funções.

#  Refatorando a função para que ela retorne o valor calculado
def quadrado_de_set():
    return 7 * 7

#  Criamos uma variável para receber o retorno de função
ret = quadrado_de_set()
print(f'Retorno {ret}')

print(f'Retorno {quadrado_de_set() + 10}')

#  Refatorando a primeira função

def diz_oi():
    return 'Oi '

ser = 'Bruno!'

print(diz_oi() + ser)

OBS: Sobre a palavra return:

- Ela finaliza a função, ou seja, ela sai da execução da função;
- Podemos ter, em uma função, diferentes returns;
- Podemos em uma função retornar qualquer tipo de dado e até mesmo multiplos valores.

# Exemplo 1 - - Ela finaliza a função, ou seja, ela sai da execução da função;

def diz_oi():
    print('Estou sendo executado antes do retorno')
    return 'Oi'
    print('Estou sendo executado após o retorno')

print(diz_oi())

# Exemplo 2 - - Podemos ter, em uma função, diferentes returns;

def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 5
    return 'ff'

print(nova_funcao())

# Exemplo 3 - - Podemos em uma função retornar qualquer tipo de dado e até mesmo multiplos valores.

def outra_funcao():
    return 5, 6, 7, 8

n1, n2, n3, n4, = outra_funcao()
print(n1, n2, n3, n4)

print(outra_funcao())

#  Vamos criar uma função para jogar uma moeda

from random import random

def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    # valor = random()
    # if valor > 0.5:
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(f'O Resultado deu {joga_moeda()}')

#  Erros comuns na utilização do retorno que na verdade nem é erro, mas sim codificação desnecessária.

def eh_impar():
    numero = 6
    if numero % 2 != 0:
        return True
    return False

print(eh_impar())
"""

















