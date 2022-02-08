"""
try e expect -> servem para tratar os possíveis erros que serão gerados no código

Afinal quando eu me preocupo em tratar um erro de código? Bom, SEMPRE que houver algum
tipo de entrada de dado, deve ser tratado possíveis erros

"""

# Exemplo: Forma Geral -> Genérico

try:
    geek()
except :
    print('Deu algum problema na execução do programa')

# Exemplo: Melhor forma de uso

try:
    geek()
except NameError:
    print('"NameError" foi dado na execução do programa')

# Exemplo 2

try:
    geek()
except NameError as err:
    print(f'"NameError" foi dado na execução do programa: {err}')

def get_values(dict, key):
    try:
        return dict[key]
    except NameError as erra:
        print(f'Foi gerado um erro de "NameError: {erra}')
    except TypeError as errb:
        print(f'Foi gerado um erro de "TypeError": {errb}')
    except KeyError:
        return None


dic = {"Nome": "Heloisa"}

print(get_values(dic, "Nome"))
print(get_values(dic, "Game"))

# Exemplo com ENTRADA de dados

def dividr(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor digitado incorreto!'
    except ZeroDivisionError:
        return 'Não existe divisão por 0'

num1 = (input('Digite o primeiro valor: '))
num2 = (input('Digite o segundo valor: '))

print(f'O resultado da divisão pelos números é: {dividr(num1, num2)}')

# Exemplo Semi-Genérico de tratamento de erros

def dividr(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError):
        return 'Ocorreu algum problema!'
    finally:  # O finally, geralmente, é utilizado para fechar ou desalocar recursos.
        print('Executando finally')



num1 = (input('Digite o primeiro valor: '))
num2 = (input('Digite o segundo valor: '))

print(f'O resultado da divisão pelos números é: {dividr(num1, num2)}')





