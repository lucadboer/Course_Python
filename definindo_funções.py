"""
Definindo Funções

- Funções são pequenas partes de códigos que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito uteis para executar procedimentos similares repetidas vezes;

OBS: Se vc escrever uma função que realiza várias tarefas dentro dela
é bom fazer uma verificação para que a função seja simplificada.

Já utlizamos várias funções desde que iniciamos o curso:
- print()
- len()
- max()
- min()
- append()
- e muitas outras...

#  Exemplo de utilização de funções

cores = ['verde', 'azul', 'amarelo', 'roxo']

#  Utilizando a função integradada (Built-in) do Python print()

print(cores)

#  DRY - Don't repeat yourself - Não repita você mesmo / Não repita seu código.

#  Como definir funções:


Em Python, a forma geral de definir uma função é :

def nome_da_função(parâmetrod_de_entrada):
    bloco_da_função 

Onde:

nome_da_função -> SEMPRE com letras minúsculas e seperadas por underline (Snake Case);
parâmetros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_função -> Também chamado de corpo da função ou implementação , é onde o processamento da função acontece.
Nesse bloco pode ter retorno ou não da função

OBS: Veja que para definir uma função utilizamos a palavra def informando ao Python que estamos definindo uma função.
Também abrimos o bloco de código com o já conhecido dois pontos ( : ) que
é utilizado em Python para definir blocos.
"""

#  Definindo uma função

#  Exemplo 1:

def diz_oi():
    print('Eai!')

#  Exemplo 2:

def cantar_parabens():
    diz_oi()
    print('FELIZ ANIVERSÁRIO KARALHOOOO')
    print('TUDO DE BOM PRA VOCÊ')
    print('TAMO JUNTO')


"""
OBS: 

1 - Veja que, dentro das nossas funções podemos utilizar outras funções;
2 - Veja que, nossa função só executa uma tarefa, ou seja, a única tarefa que ela faz é dizer oi;
3 - Veja que esta função não recebe nenhum parâmetro de entrada;
4 - Veja que esta função não retorna nada;
"""

#  Utilizando funções

#  Chamada de execução
diz_oi()

cantar_parabens()

#for n in range(5):
 #   print(n)
  #  diz_oi()

#  Em Python podemos criar variáveis do tipo de uma função e executar esta função através da variável

diz = diz_oi
diz()