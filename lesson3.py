
print("ex 1")
"""
Сгенерируйте список numbers, состоящий из чисел в диапазоне от 0 до 100
включительно, которые делятся без остатка как на 2, так и на 3.
Выведите список numbers на экран.
"""
# numbers = [i for i in range(0, 100, 6)]
# print(numbers)
numbers = []
for i in range(0, 100, 6):
    numbers.append(i)
print(numbers)
##########################################################################
print("ex 2")
"""
Имеется список items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
- Составьте новый список numbers, который содержит только целые числа
(int) и вещественные числа (float) из списка items.
- Выведите на экран сумму чисел в numbers.
"""
items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
numbers = []
for i in range(len(items)):
    if isinstance(items[i], (int, float)):
        numbers.append(items[i])
print(sum(numbers))
############################################################################
print("ex 3")
"""
Создать список messages, который будет хранить “сообщения”.
- Программа должна в бесконечном цикле запрашивать у пользователя
ввести сообщение (строку) с клавиатуры и сохранять ее в список messages.
Причем программа должна запоминать не более 5 последних сообщений.
То есть, если длина списка messages превысила 5, то первое сообщение в
нем должно быть удалено.
- Если пользователь ввел “Пока”, то программа должна вывести “Ну ладно,
пока!” и список последних сообщения на экран.
"""
messages = []
while True:
    message = input("Input your message: ")
    messages.append(message)
    if len(messages) > 5:
        del messages[0]
    if message == "Пока":
        break
print("Ну ладно, пока!")
print(messages)
###############################################################################
print("ex 4")
"""
Имеется список numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
- Создайте новый список, где будут удалены все дубликаты из списка
numbers.
- Отсортируйте итоговый список и выведите на экран.
"""
numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
lst = []
for num in numbers:
    if num not in lst:
        lst.append(num)
lst.sort()
print(lst)
###############################################################################

