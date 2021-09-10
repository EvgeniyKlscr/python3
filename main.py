#Homework 1

string = str('string')
integer = int(2021)
float = float(11.0)
bytes = bytes('privet', encoding = 'utf-8')
list = [1, 'word', 157]
tuple = (18, 19, 20)
set = set('hell')
frozen_set = frozenset('world')
dict = dict([(1, 9), (2, 16)])
print(string, type(string))
print(integer, type(integer))
print(float, type(float))
print(bytes, type(bytes))
print(list, type(list))
print(tuple, type(tuple))
print(set, type(set))
print(frozen_set, type(frozen_set))
print(dict, type(dict))
print()


word_1 = 'privet'
word_2 = 'poka'
word_3 = word_1 + word_2
print(word_3)
print()

num_1 = 5
num_2 = 21
num_3 = num_1 + num_2
num_4 = num_2 / num_1
num_5 = num_1 * num_2
num_6 = num_2 // num_1
num_7 = num_2 % num_1
print(num_3, num_4, num_5, num_6, num_7, sep = '\n')
print()

#Homework 2

s_1 = 'kalinka'
s_2 = 'malinka'

i_1 = 10
i_2 = 15
i_3 = 20
i_4 = 25

f_1 = 11.1
f_2 = 21.5
f_3 = 34.9

res_int_1 = i_1 > i_2
res_int_2 = i_1 < i_2
res_int_3 = i_3 >= i_4
res_int_4 = i_3 <= i_4
res_int_5 = i_1 == i_4
res_int_6 = i_1 != i_4
res_int_7 = i_1 >= i_2
res_int_8 = i_1 <= i_2
res_int_9 = i_1 == i_2
res_int_10 = i_1 != i_2
res_int_11 = i_3 > i_4
res_int_12 = i_3 < i_4
res_int_13 = i_3 == i_4
res_int_14 = i_3 != i_4
res_int_15 = i_1 <= i_4
print(res_int_1, res_int_2, res_int_3, res_int_4, res_int_5, res_int_6, res_int_7, res_int_8, res_int_9, res_int_10, res_int_11, res_int_12, res_int_13, res_int_14, res_int_15, sep = '\n')
print()

res_float_1 = f_1 > f_2
res_float_2 = f_1 < f_2
res_float_3 = f_3 >= f_1
res_float_4 = f_3 <= f_1
res_float_5 = f_1 == f_3
res_float_6 = f_1 != f_3
res_float_7 = f_1 >= f_2
res_float_8 = f_1 <= f_2
res_float_9 = f_1 == f_2
print(res_float_1, res_float_2, res_float_3, res_float_4, res_float_5, res_float_6, res_float_7, res_float_8, res_float_9, sep = '\n')
print()

res_and_1 = i_1 > i_2 and i_3 > i_4
res_and_2 = i_1 > i_2 or i_3 < i_4
res_and_3 = not i_1 == i_2
res_and_4 = i_3 >= i_2 and i_4 >= i_1
res_and_5 = i_3 <= i_2 or i_4 <= i_1
res_and_6 = i_3 != i_2 or i_3 > i_1
res_and_7 = not i_3 >= i_2
res_and_8 = i_4 == i_2 and i_4 != i_3
res_and_9 = i_4 < i_1 or i_2 >= i_3
res_and_10 = not i_4 != i_1
print(res_and_1, res_and_2, res_and_3, res_and_4, res_and_5, res_and_6, res_and_7, res_and_8, res_and_9, res_and_10, sep = '\n')
print()

a = int(input())
if a < 30:
    print('Вы ввели число = ', a, ', которое меньше 30', sep = '')
if a > 30:
    print('Вы ввели число = ', a, ', которое больше 30', sep = '')
if a == 30:
    print('Вы ввели число = ', a, ', которое равно 30', sep = '')
print()

import random
b = int(input())
c = random.randint(1, 100)
if b > c:
    print('Вы ввели число = ', b, ', которое больше сгенерированного числа', sep='')
if b < c:
    print('Вы ввели число = ', b, ', которое меньше сгенерированного числа', sep='')
if b == c:
    print('Вы ввели число = ', b, ', которое равно сгенерированному числу', sep='')
print()

import random
g = int(input())
k = random.randint(1, 100)
l = random.randint(1, 100)
if g > k:
    if g < l:
        print('Вы ввели число = ', g, ', которое больше и меньше сгенерированных чисел', sep='')
if g > k:
    if g == l:
        print('Вы ввели число = ', g, ', которое больше и равно сгенерированному числу', sep='')
if g > k:
    if g > l:
        print('Вы ввели число = ', g, ', которое больше сгенерированных чисел', sep='')

if g == k:
    if g < l:
        print('Вы ввели число = ', g, ', которое равно и меньше сгенерированных чисел', sep='')
if g == k:
    if g == l:
        print('Вы ввели число = ', g, ', которое равно сгенерированным числам', sep='')
if g == k:
    if g > l:
        print('Вы ввели число = ', g, ', которое равно и больше сгенерированного числа', sep='')

if g < k:
    if g < l:
        print('Вы ввели число = ', g, ', которое меньше сгенерированных чисел', sep='')
if g < k:
    if g == l:
        print('Вы ввели число = ', g, ', которое меньше и равно сгенерированным числам', sep='')
if g < k:
    if g > l:
        print('Вы ввели число = ', g, ', которое меньше и больше сгенерированных чисел', sep='')
