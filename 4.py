import os
os.system("clear")

# 1 Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# from math import pi
# d = int(input("Задайте точность: "))
# print(f"Число π с указанной точностью = {round(pi, d)}")

# 2 Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

# n = int(input("Задайте натуральное число N: "))

# list_n = []

# while n % 2 == 0:
#     list_n = list_n + [2]
#     n = n / 2
# while n % 3 == 0:
#     list_n = list_n + [3]
#     n = n / 3
# while n % 5 == 0:
#     list_n = list_n + [5]
#     n = n / 5
# while n % 7 == 0:
#     list_n = list_n + [7]
#     n = n / 7
# if n % n == 0:
#     list_n = list_n + [round(n)]

# print(list_n.sub())

# 3 Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# from random import randint

# list_1 = []

# for i in range(1, 10):
#     list_1.append(randint(1, 6))

# print(list_1)

# list_2 = []

# for i in list_1:
#     if i not in list_2:
#         list_2.append(i)

# print(list_2)

# 4 Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random

# def polynomial():
#      k = int(input("Введите степень: "))
#      num1 = random.randint(0,100)
#      num2 = random.randint(0,100)
#      num3 = random.randint(0,100)
#      polynomial = str(f"Запись многочлена: {num1}x^{k} + {num2}x^{k} + {num3} = 0")
#      return polynomial

# p = polynomial()
# p2 = polynomial()

# data = open('file', 'w')
# data.writelines(p)
# data.close

# 5 Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import random

def polynomial():
     k = int(input("Введите степень: "))
     num1 = random.randint(0,100)
     num2 = random.randint(0,100)
     num3 = random.randint(0,100)
     polynomial = str(f"{num1}x^{k} + {num2}x^{k} + {num3} = 0")
     return polynomial

p = polynomial()
p2 = polynomial()

data = open('file', 'w')
data.writelines(p)
data.close

data = open('file2', 'w')
data.writelines(p2)
data.close