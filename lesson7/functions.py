from lesson7.LessonException import RegistrationError


def is_username(username):
    return isinstance(username, str) and 4 <= len(username) <= 15 and username.isalpha()

def is_password(password):
    return isinstance(password, str) and 8 <= len(password) <= 45 and password.isalnum()

def registration(username, password):
    """
    Определяет корректно ли введены значения параметров
    :param username: строка, кол-во символов от 4 до 15, только буквы
    :param password: строка, кол-во символов от 8 до 45, только буквы и цифры
    :return: True или исключение RegistrationError
    """

    if is_username(username) and is_password(password):
        return True
    else:
        raise RegistrationError()

