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


word_1 = 'privet'
word_2 = 'poka'
word_3 = word_1 + word_2
print(word_3)

num_1 = 5
num_2 = 21
num_3 = num_1 + num_2
num_4 = num_2 / num_1
num_5 = num_1 * num_2
num_6 = num_2 // num_1
num_7 = num_2 % num_1
print(num_3, num_4, num_5, num_6, num_7, sep = '\n')

