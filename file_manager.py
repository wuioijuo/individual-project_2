"""Чтение данных из файла и запись ответа в файл."""


class FileManagerError(Exception):
    """Ошибка при работе с файлом."""

    pass


class FileManager:
    """Класс для файлового ввода и вывода."""
    def read_digits_from_file(self, file_path):
        """Считывает строку цифр из входного файла."""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
        except OSError as error:
            raise FileManagerError(
                "Не удалось открыть или прочитать файл: " + str(error)
            )

        not_empty_lines = []

        for line in lines:
            clean_line = line.strip()

            if clean_line != "":
                not_empty_lines.append(clean_line)

        if len(not_empty_lines) == 0:
            raise FileManagerError("Файл пустой.")

        if len(not_empty_lines) > 1:
            raise FileManagerError(
                "Файл должен содержать только одну строку с цифрами."
            )

        return not_empty_lines[0]

    def write_answer_to_file(self, file_path, answer):
        """Записывает ответ программы в выходной файл."""
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(answer)
        except OSError as error:
            raise FileManagerError(
                "Не удалось записать данные в файл: " + str(error)
            )

        return True