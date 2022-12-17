# 14. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:  - 6782 -> 23  - 0,67 -> 13   198.45 -> 27

# num = input('Введите число: ')
# sum = 0
# for a in num:
#     if a.isdigit():
#         sum += int(a)
# print(f"Сумма {num} равна: ", sum)

# 15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: (1, 1*2, 1*2*3, 1*2*3*4)   - 4 -> [ 1, 2, 6, 24 ]   - 6 -> [1, 2, 6, 24, 120, 720]

# input_num = int(input('Введите число: '))
# list = [1]
# for i in range (1,input_num):
#     list.append ((i+1) * list [i-1])
# print(list)

# 16. Задайте список из n чисел последовательности (1 +1\n)**n и выведите на экран их сумму.
# Пример:  - Для n = 6: [2, 2, 2, 2, 2, 3] ->13

# number = int(input("Введите количество чисел в списке: "))
# sum = 0
# def sequence(number):
#     return[round((1 + 1 / i)**i, 2) for i in range (1, number + 1)]          
# print(f'Список для {number} чисел =',sequence(number))
# for i in range(1, number + 1):
#     sum += (1 + 1 / i) ** i
# print(f'Сумма последовательности из {number} чисел равна: {sum}')

# 17. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях (не индексах). 
# Position one - 1
# Position two – 3
# Number of elements 5     -> [-5, -4, -3, 2, 3]     -> 15

# from random import randint
# numbers = []
# for i in range(5):
#     numbers.append(randint (-5,5))
# print(numbers)

# def get_numbers(numbers):
#     count =0 
#     for element in numbers:
    
#         count +=1
#     return count
# print('Number of elements: ', get_numbers(numbers))

# x = int(input('Enter  position of first element: '))
# y = int(input('Enter position of second element: '))

# for i in range(len(numbers)):
#     mult = numbers[x -1]*numbers[y - 1]
# print(f'Mult of elements: {numbers[x -1]} * {numbers[y -1]} =', mult)

# 18. Реализуйте алгоритм перемешивания списка, без функции shuffle из модуля random.
# 10               -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]            -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

# import random
# list = [0,1,2,3,4,5,6,7,8,9]
# print ("Начальный список: " + str(list))
# for i in range(len(list)-1, 0, -1):
#     j = random.randint(0, i + 1) 
#     list[i], list[j] = list[j], list[i] 
# print ("Перемешанный список: " +  str(list))



