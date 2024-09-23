def is_triangle(side1, side2, side3):
    """
    Определяет существует ли треугольник.
    :param side1, side2, side3: Стороны треугольника.
    :return: True, если существует.
    """

    temp = 0
    if side1 + side2 <= side3:
        temp += 1
    if side1 + side3 <= side2:
        temp += 1
    if side3 + side2 <= side1:
        temp += 1
    if temp > 0:
        return False
    else:
        return True

def sum_ignore_non_number(items):
    """
    Находит сумму всех числовых элементов
    :param items: Список или кортеж значений
    :return: Сумма
    """

    summa = 0
    for item in items:
        if isinstance(item, (int, float)):
            summa += item
    return summa

def average(*args):
    """
    Функция возвращает среднее арифметическое всех переданных чисел.
    :param args: числа, произвольное количество
    :return: Среднее арифметическое чисел, 0, если нет ни одного аргумента
    """

    if len(args) > 0:
        return sum(args) / len(args)
    else:
        return 0

def common_strings(list1, list2, ignore_case=True):
    """
    Функция возвращает список пересекающихся значений. При этом, если ignore_case равен True, то функция должна
    игнорировать регистр. В противном случае функция должна учитывать регистр символов и считать такие строки разными.
    :param list1
           list2
           ignore_case
    :return: Список
    """

    result_list = []
    if ignore_case:
        for i in range(len(list1)):
            list1[i] = list1[i].lower()

        for i in range(len(list2)):
            if list2[i].lower() in list1:
                result_list.append(list2[i])
    else:
        for i in range(len(list2)):
            if list2[i] in list1:
                result_list.append(list2[i])

    return result_list