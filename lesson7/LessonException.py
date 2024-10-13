class RegistrationError(Exception):

    def __init__(self):
        super().__init__("Введено некорректное значение username или password")
