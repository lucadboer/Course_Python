"""
Set Comprehensions

lista = [1, 2, 3, 4, 5]
Set = {1, 2, 3, 4, 5}
"""

#  Exemplos

numeros = {1, 8, 7, 9, 6}
res = {num for num in numeros}
print(res)

res2 = {num for num in range(0, 100+1)}
print(res2)

res3 = {num ** 2 for num in range(1, 5+1)}
print(res3)

res4 = {num: num ** 2 for num in range(1, 5+1)}
print(res4)

res5 = {letra for letra in 'Geek University'}
print(res5)
