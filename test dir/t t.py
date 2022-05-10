#
# lst_in = ['Номер;Имя;Оценка;Зачет', '1;Портос;5;Да', '2;Арамис;3;Да', '3;Атос;4;Да', "4;д'Артаньян;2;Нет", '5;Балакирев;1;Нет']
#
#
#
#
# lst_in = [x.split(";") for x in lst_in]
# for i in lst_in :
#     for k,v in enumerate(i):
#         if v.isdigit():
#             i[k] = int(v)
#
#
#
# t = tuple(tuple(i) for i in lst_in)
# # t_sorted = [sorted(i,key=lambda x: x%0 == 1) for i in t[1:]]
#
#
#
# print(t)
#
# # mask = [3, 0, 2, 1]
# #
#
# # t_sorted = tuple(tuple(x) for x in [sorted(x, key=lambda i: mask[x.index(i)]) for x in t_sorted])
# order = "Имя;Зачет;Оценка;Номер"
#
# t_sorted = tuple(zip(*sorted()))
#
# list(zip(*t)), key=lambda x: order.find(x[0])


# lst_in = ['Атос=лейтенант', 'Портос=прапорщик', "д'Артаньян=капитан",'Арамис=лейтенант', 'Балакирев=рядовой']
# lst_in = tuple(map(lambda x: x.split('='),lst_in))
# mask = "'рядовой', 'сержант', 'старшина', 'прапорщик', 'лейтенант', 'капитан', 'майор', 'подполковник', 'полковник'"
# lst = sorted(lst_in, key= lambda x: mask.index(x[1]))
#
# print(lst)
#


# def get_sum(s):
#     summ = sum(filter(lambda x: type(x) == int,s))
#     if not summ:
#         return 0
#     return summ
#
# print(get_sum([1,2,3,1.1,2.3]))

# def get_even_sum(it):
#     summ = filter(lambda x: type(x) == int and x%2 == 0,it)
#     if summ:
#         summ = sum(summ)
#         return summ
#     else:
#         return 0
#
#
#
# print(get_even_sum([1,2,3,4,3,1.1,2.3]))

# def get_list_dig(lst):
#     lst = list(filter(lambda x: type(x) in (float,int),lst) )
#     return lst
#
# print(get_list_dig([1,2,34,5,'a']))
#
#
#
#
#

# s = any(map(lambda x: x < 3, map(int,input().split())))
# if s:
#     print('отчислен')
# else:
#     print('учится')
#
#
#

# lst = [['x', '', '0'],['x', 'x', 'x'],['0', '0', 'x']]
#
#
# def is_free(lst):
#     return any(list(any(map(lambda x: x== '#', i)) for i in lst))
# ab = 'as'
# print(is_free(lst))
#
# n = 100
# mask = 8
# res = mask | n
#
# print(bin(res))
# #'0b110 0 100' 100
# #'0b110 1 100' 108
#
# # '0b100 1 1001' 153
# # '0b100 0 1001' 137

# m = 153
# mask = 9
# res = mask | n
# print(bin(res))

# n = 'ѩкю[щюлцхZ'
# key=123
#
# s = ''
# for i in n:
#     print(i)
#     i = ord(i) ^ key
#     s += chr(i)
# print(s)
#
# #'0b1101010' 106
# #0b11010001 209
#
# 0b11011001

# mask = int(input())
# flag = 72
# res = flag & mask
# if res == flag:
#     print('ДА')
# else:
#     print('НЕТ')
# print(res)

# '0b1101010' 106
# '0b1001000' 72
# 0b11011001
# mask = int(input())
# flag = 108
# res = flag | mask
# if res == flag:
#     print('ДА')
# else:
#     print('НЕТ')
#
#
import random
# lst_in = ['1 2 3 4', '5 6 7 8', '9 8 6 7']

# lst = map(lambda x: x.split(','),lst_in)
# lst = [j.split() for i in lst for j in i]
# lst = [[int(j) for j in i] for i in lst ]
# random.shuffle(lst)
# lst = zip(lst)
#
# for i in lst:
#     for j in i:
#         print(*j)

# students = input().split()
# print(*random.sample(students,3))

# N = int(input())
# P = [[0] * N for i in range(N)]
#
# # здесь продолжайте программу
#
# import random
# random.seed(1)
#
# N = int(input())
# P = [[0] * N for i in range(N)]
# M = 10
# count = 0
# counter = 0
# def surround_with_zeros(lst):
#     n = len(lst)
#     lst.insert(0, [0] * n)
#     lst.append([0] * n)
#     for i in lst:
#         i.insert(0, 0)
#         i.append(0)
# def remove_surrounding_zeros(lst):
#     n = len(lst)
#     lst.pop(0)
#     lst.pop()
#     for i in lst:
#         i.pop(0)
#         i.pop()
# def verify(lst, i, j):
#     return sum([lst[i - 1][j - 1], lst[i - 1][j], lst[i - 1][j + 1],
#                 lst[i][j - 1], lst[i][j + 1], lst[i + 1][j - 1],
#                 lst[i + 1][j], lst[i + 1][j + 1]]) == 0
#
# surround_with_zeros(P)
#
# for i in range(M):
#     while counter < 10:
#         row = random.randint(1, N )
#         col = random.randint(1, N)
#         if P[row][col] != 1 and verify(P, row, col):
#             P[row][col] = 1
#             counter +=1
#
#
#
#
# remove_surrounding_zeros(P)
# [print(*i) for i in P]
#

# def s(*args):
#     print(args)
# s('45 4 8 11 12 0')

# def get_biggest_city(*args):
#     len_word_max = 0
#     for i in args:
#         if len(i) > len_word_max:
#             len_word_max = len(i)
#             word = i
#     return word
#
# lst = ['Питер', 'Москва', 'Самара', 'Воронеж']
#
# print(get_biggest_city('Питер', 'Москва', 'Самара', 'Воронеж','Воронew'))

# def get_data_fig(*args,**kwargs):
#
#     perimeter = sum(args),
#     if "type" in kwargs:
#         perimeter += kwargs['type'],
#     if "color" in kwargs:
#         perimeter+= kwargs['color'],
#     if "closed" in kwargs:
#         perimeter += kwargs['width'],
#     return perimeter
#
# print(get_data_fig(10,122,1,2,3,4,5,type = True,color='yellow'))

# lst = [[1, 0, 0, 0, 0],
#        [0, 0, 1, 0, 0],
#        [0, 0, 0, 0, 0],
#        [0, 0, 0, 1, 0],
#        [0, 1, 0, 0, 0]]
#
# # a = []
#
# for i in range(len(lst)-1):
#     a.append([str(x+y) for x,y in zip(lst[i],lst[i+1])])
# b = [''.join(i) for i in a]
# for i in b:
#     if '2' in i or '11' in i:
#         print('wrong')
#         break
#
#
#
# print(b)
#


# weight = float(input())
# tall = float(input())
# res = weight/tall**2
# if res <= 18.5:
#     print ('Недостаточная масса')
# if 18.5 < res <= 25:
#     print('Оптимальная масса')
# if res > 25:
#     print('Избыточная масса')
#
# string = input()
#
# summa = str(len(string) * 60 / 100).split('.')
#
# print(f'{summa[0]} р. {int(summa[1])*10} коп.')

# string = (int(input()) - 8)%12
#
# d = {0:'Дракон',1:'Змея',2:'Лошадь',3:'Овца',4:'Обезьяна',5:'Петух',6:'Собака',7:'Свинья',8:'Крыса',9:'Бык',10:'Тигр',11:'Заяц'}
#
# print(d[string])

# string = input()
# if len(string) > 5:
#     print(string[0] + string[:-6:-1])
# else:
#     print(string[:-6:-1].replace('0',''))
#
#

# d = {'a':123,'1':'dfg'}
# b = ''.join(d)
# print(b)

# n = input()
#
# if int(n)%100 == 0 and int(n) / 100 < 10:
#     nn = [i for i in n[1::3]]
#     n = n[0]+ ','.join(nn)
#
#
# print(n)
#


# t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
#      ["Я", "Python", "выучил", "с", "каналом"],
#      ["Балакирев", "что", "раздавал?"]]
#
# for i in t:
#     print(str(i))

# s = "шалаш"
#
# print('да' if s == s[::-1] else 'нет')
#
# booly = set(['m','a']) == frozenset(['m','a','a'])
# k = 0
# for i in (['a','m']):
#     if i[0] == 'm':
#         k += 1
# print(booly*k)
#
#
# print('a', 'b', 'c', sep='*')
# print('d', 'e', 'f', sep='**', end='')
# print('g', 'h', 'i', sep='+', end='%')
# print('j', 'k', 'l', sep='-', end='\n')
# print('m', 'n', 'o', sep='/', end='!')
# print('p', 'q', 'r', sep='1', end='%')
# print('s', 't', 'u', sep='&', end='\n')
# print('v', 'w', 'x', sep='%')
# print('y', 'z', sep='/', end='!')
# a,b,c,sep = input(),input(),input(),input()
# print(a, b, c,sep=sep)

# import sys
#
# # считывание списка из входного потока
# s = sys.stdin.readlines()
# lst = [list(map(int, x.strip().split())) for x in s]
#
# # здесь продолжайте программу (используйте список lst_in)
# for i in range(len(lst)):
#     for j in range(i+1,len(lst[i])):
#         if lst[i][j] != lst[j][i]:
#             print('НЕТ')
#             break
#     else:
#         continue
#     break
# else:
#     print('ДА')


from random import sample

# n = int(input())
# a,b,c = str(n // 100),str((n % 100) // 10),str(n % 10)
#
# print(a + b + c,a + c + b,b + a + c,b + c + a,c + a + b,c + b + a,sep = '\n')
# a,b,c = '123'
# print(a)

# put your python code here
# n = int(input())
#
# n1 = n // 1000
# n2 = (n // 100) % 10
# n3 = (n % 100) // 10
# n4 = n % 10
#
# print(f'Цифра в позиции тысяч равна {n1}')
# print(f'Цифра в позиции сотен равна {n2}')
# print(f'Цифра в позиции десятков равна {n3}')
# print(f'Цифра в позиции единиц равна {n4}')
# str = ''
# print (str.rjust(17, '*'))
# print (str.rjust(1, '*'),str.center(13,' '),str.ljust(1,'*'))
# print (str.rjust(1, '*'),str.center(13,' '),str.ljust(1,'*'))
# print (str.rjust(17, '*'))

# a,b = int(input()),int(input())
#
# print(f'Квадрат суммы {a} и {b} равен {(a + b)**2}\nСумма квадратов {a} и {b} равна {a**2 + b**2}')
# n = input()
# n1 = int(n*2)
# n2 = int(n*3)
# print(int(n)+n1+n2)

# my_list2 = [66, 77, 88, 99]
# print(" ".join(map(str, my_list2)))

# a = {1,2,3,5,7}
#
# n = int(input())
#
# factors = []
#
# d = 5
#
# while True:
#     if d == 1:
#         break
#     if n % d == 0:
#
#         factors.append(d)
#
#         n//=d
#
#     else:
#
#         d -= 1
#
# test = set(a) & set(factors)
#
# if test == {2,3,5}:
#
#     print("ДА")
#
# else:
#
#     print("НЕТ")
#
#
#
#
# n = int(input())
#
# sett = set()
# d = 2
# while d * d <= n:
#     if n % d == 0:
#         sett.add(d)
#         n //= d
#     else:
#         d += 1
# if n > 1:
#     sett.add(n)
#
# print('ДА' if {2, 3, 5} <= sett else 'НЕТ')

# boys = ['Peter', 'Alex', 'John', 'Arthur','Richard']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
#
# print('Кто-то может остаться без пары!') if len(boys) != len(girls) else None
# list.sort (boys)
# list.sort (girls)
# print (*(f'{pair[0]} и {pair[1]}' for pair in zip(boys, girls)),sep='\n')
#
# counter = 0
# while True:
#     amount = int(input())
#     for i in [25,10,5,1]:
#         if amount > i :
#             amount  = amount -  i
#             counter = counter + (amount//i)
#     print(counter)

num = 12345
product = 1
while num != 0:
    last_digit = num % 10
    product = product * last_digit
    num = num // 10
print(product)
