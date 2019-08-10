# Дан список из чисел и индекс элемента в списке k.
# Удалите из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k.

# a). Программа получает на вход список, затем число k.
# Программа сдвигает все элементы,
# а после этого удаляет последний элемент списка при помощи метода pop() без параметров.

# b). Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов.
# Также нельзя использовать дополнительный список.
#
# c). Также не следует использовать метод pop(k) с параметром.
#
# d). Использовать оператор del НЕЛЬЗЯ!

from random import randint

lst = [randint(1, 50) for _ in range(10)]
print(lst)

k = int(input('Введите индекс k (от 0 до 9): '))
print('Число с индексом k равняется', lst[k])

for i in range(k, len(lst)):
    if i < len(lst) - 1:
        lst[i] = lst[i + 1]

lst.pop()
print(lst)
