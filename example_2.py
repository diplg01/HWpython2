# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

multiplication = 1
my_list = []
n = int(input('Введите количество чисел n: '))
for i in range(1, n + 1):
    multiplication *= i
    my_list.append(multiplication)
print(f'n = {n} -> {my_list}')