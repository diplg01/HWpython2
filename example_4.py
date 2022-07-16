# Реализуйте алгоритм перемешивания списка.

import random
n = int(input('Введите длину списка n = '))

my_list = []
for i in range(0, n):
    my_list.append(i)
print(f'Упорядоченный список: {my_list}')

revers = []
while (n > 0):
    index = random.randint(0, n-1)
    revers.append(my_list[index])
    del my_list[index]
    n -= 1
print(f'Перемешанный список:  {revers}')