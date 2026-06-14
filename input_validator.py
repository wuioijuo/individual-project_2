"""Проверка входных данных."""


class InputValidationError(Exception):
    """Ошибка при неправильном вводе данных."""
    pass


class InputValidator:
    """Класс для проверки строки цифр и пути к файлу."""
    MIN_LENGTH = 3
    MAX_LENGTH = 1000

    def validate_digits(self, text):
        """Проверяет, подходит ли строка под условие задачи."""
        if text == "":
            raise InputValidationError("Строка не должна быть пустой.")

        if len(text) < self.MIN_LENGTH:
            raise InputValidationError(
                "В строке должно быть минимум 3 цифры."
            )

        if len(text) > self.MAX_LENGTH:
            raise InputValidationError(
                "В строке должно быть не более 1000 цифр."
            )

        for symbol in text:
            if symbol < "0" or symbol > "9":
                raise InputValidationError(
                    "Строка должна содержать только цифры без пробелов."
                )

        return True

    def validate_file_path(self, file_path):
        """Проверяет, что путь к файлу не пустой."""
        if file_path == "":
            raise InputValidationError("Путь к файлу не должен быть пустым.")
        return True