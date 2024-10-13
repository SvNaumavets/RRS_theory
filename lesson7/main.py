from lesson7.LessonException import RegistrationError
from lesson7.functions import registration

print("Ex. 2: Регистрация")

while True:
    username = input("Input username: ")
    password = input("Input password: ")
    try:
        registration(username, password)
    except RegistrationError:
        print("Ошибка регистрации!")
    else:
        print("Успешно!")
        break

##########################################################################################

print("Ex.3: Дорогой дневник...")

while True:
    action = input("Введите одно из действий 'прочитать', 'записать', 'выйти': ")
    match action:
        case 'прочитать':
            with open('journal.txt', 'r', encoding='utf-8') as file:
                for line in file:
                     print(line)
            # break
        case 'записать':
            line = input("Введите строку, которую нужно добавить в файл: ")
            with open('journal.txt', 'a', encoding='utf-8') as file:
                file.write(line + "\n")
            # break
        case 'выйти':
            print("Еще увидимся!")
            break