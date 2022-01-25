"""
**kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca valores extras em uma tupla, o **kwargs
exige que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário

def cores_favoritas(**kwargs):
    for pessoas, cor in kwargs.items():
        print(f'A cor favorita de {pessoas.title()} é {cor}')

cores_favoritas(marcos= 'Branco', heloisa= 'Azul', luca= 'Preto')

# OBS: Os parâmetros *argd e **kwargs não são obrigatórios

#  Exemplo mais complexo:

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek"
    return 'Não sabemos avaliar quem é você'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Eai'))
print(cumprimento_especial(geek='ESPECIAL'))

#  Nas nossas funções devemos seguir (NESTA ORDEM):

- Parâmetros obrigatórios;
- *args;
- Parâmetro default (não obrigatório);
- **kwargs

#  Desempacotar **kwargs

def nome_inteiro(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Heloisa', 'sobrenome': 'Ferreira'}

print(nome_inteiro(nome= 'Heloisa', sobrenome= 'Ferreira'))  # Forma 1
print(nome_inteiro(**nomes))  # Forma 2 utilizando a variável 'nomes'

#  OBS: Os nomes das chaves de um dicionário, devem ser o mesmo dos parâmetros da função
"""





