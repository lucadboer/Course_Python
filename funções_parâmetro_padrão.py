"""
Funções com parâmetro padrão - Default Paramters

- Funções onde a passagem de parâmetro seja OPCIONAL:
print('Bom dia')
print()

- Exemplo de parâmetro OBRIGATÓRIO:

def quadrado(num):
    return num ** 2

print(quadrado(5))
print(quadrado())

def exponencial(numero=10, potencia=2):
    return numero ** potencia

print(exponencial(5, 3))  # Usou os dois argumentos
print(exponencial(4))  # Usou só o primeiro argumento
print(exponencial())  # Usou nenhum argumento, então os parâmetros usaram o valor estabelecido por padrão a eles

#  OBS: Em funções Python, os parâmetros com valores default (padrão) devem SEMPRE estar no FINAL da declaração.

#  ERRO!
def teste(num=2, potencia):
    return num ** potencia

# print(teste(6))

#  Correto:
def teste(potencia, num=2):
    return num ** potencia

print(teste(6))
"""






