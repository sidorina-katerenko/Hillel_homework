# Дана строка, в которой буква h встречается минимум два раза.
# Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними.
# При решении этой задачи использовать циклы - ЗАПРЕЩЕНО!
# (Задача решается в 3 (три) строчки кода.
# Понадобятся методы поиска, срезы и метод replace)

s = input('Введите строку, в которой буква h встречается минимум два раза: ')

# firstPart = s[:s.find('h')]
# secondPart = s[s.rfind('h') + 1:]
#
# print(firstPart + ' ' + secondPart)

theVeryDeletedPart = s[s.find('h'):s.rfind('h') + 1]

print(s.replace(theVeryDeletedPart, ' '))
