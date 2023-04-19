# 1) FizzBuzz
# перебрать числа от 1 до 100
# если число делится на 3 - вывести вместо него Fizz
# если на 5 - вывести вместо него Buzz
# если и на 3 и на 5 - вывести вместо него FizzBuzz

for chislo in range(1, 101):
    if chislo % 3 == 0 and chislo % 5 == 0:
        print('Fizz' + 'Buzz')
    elif chislo % 3 == 0:
        print('Fizz')
    elif chislo % 5 == 0:
        print('Buzz')
    else:
        print(f'[{chislo}]')
print('\n')

# 2) отсортировать 1й список по элементам 2го
# дан массив a = [1, 4, 6] и массив  b = [11, 33, 22]
# если отсортировать первый массив по второму должен получиться массив [1,6,4]

a = sorted([1, 4, 6], key=lambda x: x==4)
b = sorted([11, 33, 22], key=lambda x: x==33)
print(a)
print(b)
print('\n')

# 3) Дан список строк.
# Нужно вывести все буквы, которые встречаются в каждой из строк списка
# (включая дубли).
#
# Example
# ["bella","label","roller"] -> ["e","l","l"] ["cool","lock","cook"] -> ["c","o"]

spisok1 = []
spisok2 = []
for x in ["bella","label","roller"]:
    for y in x:
        spisok1.append(y)
for a in ["cool","lock","cook"]:
    for b in a:
        spisok2.append(b)
print(spisok1[1:4])
print(spisok2[0:2])
print('\n')

# 4) Римские цифры представлены семью различными символами: I - 1, V - 5, X - 10, L - 50, C - 100, D - 500 и M - 1000.
# Например, 2 записывается как II. 12 записывается как XII, то есть просто X + II. Число 27 записывается как XXVII, то есть XX + V + II.
#
# Римские цифры обычно пишутся слева направо от большего к меньшему. Но цифра четыре пишется как IV. Так как единица предшествует пятерке,
# мы вычитаем ее и получаем четыре. Тот же принцип применим к числу девять, которое пишется как IX. Есть шесть случаев, когда используется вычитание:
#
# I перед V (5) и X (10) — 4 и 9.
# X перед L (50) и C (100 —  40 и 90.
# C перед D (500) и M (1000) — 400 и 900.
# Дана римская цифра, преобразовать ее в целое число.

x = input('Введите римскую цифру: ')
slovar = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
rez = 0
k = 0
for i in x[::-1]:
    if slovar[i] >= k:
        rez = rez + slovar[i]
        k = slovar[i]
    else:
        rez = rez - slovar[i]
print(rez)