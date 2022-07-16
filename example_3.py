# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input('Введите количество чисел n: '))
my_list = []
sum = 0
for i in range(1, n + 1):
    temp = (1 + 1/i)**i
    sum += temp
    t = str(i) + ': ' + str(round(temp, 3))
    my_list.append(t)
print('n =', n, ':', my_list)