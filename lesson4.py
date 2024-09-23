from functions import sum_ignore_non_number
from functions import is_triangle
from functions import average
from functions import common_strings


print("ex. 1")
print(f"sum_ignore_non_number([1, 2, 'Hey', None, 4.3]) = {sum_ignore_non_number([1, 2, 'Hey', None, 4.3])}")

print("ex. 2")
print(f"is_triangle(2, 4, 9) = {is_triangle(2, 4, 9)}", f"is_triangle(3, 4, 5) = {is_triangle(3, 4, 5)}", sep="\n")

print("ex. 3")
print(f"average() = {average()}", f"average(1, 2, 3, 4, 5, 6, 7, 8) = {average(1, 2, 3, 4, 5, 6, 7, 8)}", sep="\n")

print("ex. 4")
fruits_1 = ['banana', 'APPLE', 'watermelon', 'cherry']
fruits_2 = ['Mango', 'apple', 'orange', 'cherry']
print(f"common_strings(fruits_1, fruits_2) = {common_strings(fruits_1, fruits_2)}")

print("Повторение: КаКоЕ-тО вОлНеНиЕ")
text = input("Input text: ")
result = ''.join([char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(text)])
print(result)

