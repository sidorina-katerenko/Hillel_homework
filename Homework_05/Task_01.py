# Дана строка.
# a. выведите третий символ этой строки.
# b. выведите предпоследний символ этой строки.
# c. выведите первые пять символов этой строки.
# d. выведите всю строку, кроме последних двух символов.
# e. выведите все символы с четными индексами (считая, что индексация начинается с 0,
# поэтому символы выводятся начиная с первого).
# f. выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
# g. выведите все символы в обратном порядке.
# h. выведите все символы строки через один в обратном порядке, начиная с последнего.
# i. выведите длину данной строки.

t = input('Введите строку: ')

print('третий символ этой строки: ', t[2])
print('предпоследний символ этой строки: ', t[-2])
print('первые пять символов этой строки: ', t[:5])
print('вся строка, кроме последних двух символов: ', t[:-2])
print('все символы с четными индексами: ', t[::2])
print('все символы с нечетными индексами: ', t[1::2])
print('все символы в обратном порядке: ', t[::-1])
print('все символы строки через один в обратном порядке, начиная с последнего: ', t[-1::-2])
print('длина данной строки: ', len(t))
