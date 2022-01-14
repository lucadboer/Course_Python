"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários em Python são conhecidos por mapas.

Dicionários são coleções do tipo chave /valor.

Dicionários são representados por {}.

print(type({}))

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor'
    - Tanto chave quanto valor podem ser de qualquer tipo de dado
    - Podemos misturar tipos de dados

#  Criação de dicionários

#  Forma 1: (mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

#  Forma 2: (menos comum)

paises = dict(br = 'Brasil', eua = 'Estados Unidos', py = 'Paraguai')
print(paises)
print(type(paises))

#  Forma 1: - Acessando via chave, da mesma forma que listas/tuplas
print(paises['br'])
print(paises['py'])

#  Forma 2: - Acessando via get (Recomendada
print(paises.get('br'))
print(paises.get('py'))
print(paises.get('teste'))

#  Caso o get não encontre o valor informado, será retornado o tipo None e não será gerado KeyError

pais = paises.get('ru')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Pais não encontrado...')

#  Podemos definir um padrão para caso não encontremos o valor da chave informada: ('...', 'pais nao encontrado')

pais = paises.get('jp', 'país não encontrado')

print(f'Encontrei o pais: {pais}')

#  Podemos verificar sse determinada chave se encontra no dicionário

print('br' in paises)
print('eua' in paises)
print('py' in paises)
print('jp' in paises)
print('Brasil' in paises)

if 'ru' in paises:
    russia = paises['ru']

#  Podemos utilizar QUALQUER tipo de dado dentro de um dicionário

#  Tuplas por exemplo são bastante interessantes de serem utilizadas como
#  chaves de dicionários, pois as mesmas são imutáveis

localidades = {
    (17.5454, 18.5115): 'Escritório em São Paulo',
    (45.5554, 12.2115): 'Escritório em Tokyo',
    (98.3654, 89.6515): 'Escritório em California',
}

print(localidades)
print(type(localidades))

#  Podemos encontrar o valor conforme abaixo
print(localidades[45.5554, 12.2115])

#  Adicionar elementos em um dicionário

receitas = {'jan': 500, 'fev': 250, 'mar': 800}
print(receitas)

#  Forma 1: - Mais comum
receitas['abr'] = 1000
print(receitas)

#  Forma 2:
novo_dado = {'mai': 900}
receitas.update(novo_dado)  # receitas.update({'maio': 900})
print(receitas)

#  Atualizando dados em um dicionário

#  Forma 1:

receitas['mai'] = 500
print(receitas)

#  CONCLUSÃO 1: A forma de adicionar novos elementos e atualizar dados em um dicionário é a mesma.
#  CONCLUSÃO 2: Em dicionários NÃO podemos ter chaves repetidas

#  Remover dados de um dicionário

receitas = {'jan': 500, 'fev': 250, 'mar': 800}
print(receitas)

#  Forma 1:
ret = receitas.pop('mar')
print(ret)

print(receitas)

# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, KeyError é retornado.
# OBS 2: Sempre que removermos um objeto, o valor do mesmo será retornado.

# Forma 2:

del receitas['fev']
print(receitas)

#  Se a chave não existir será gerado um KeyError: del receitas['fev']
#  Neste caso o valor removido não é retornado
"""







