# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]
import math
def is_simple(num):
    i=2
    while i<=math.sqrt(num):
        if num%i==0:
            return False
        else:
            i+=1
    return True

number = int(input("Введите целое положительное число: "))
i=2
simple_list=[]
while i<number:
    if is_simple(i)==True and number%i==0:
        simple_list.append(i)
    i+=1
print(simple_list)