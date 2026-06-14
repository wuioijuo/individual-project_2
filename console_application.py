"""Консольное меню для задачи «Числовое кольцо»."""

from file_manager import FileManager, FileManagerError
from input_validator import InputValidator, InputValidationError
from ring_equation_solver import RingEquationSolver


class ConsoleApplication:
    """Главный класс программы."""

    OUTPUT_FILE_NAME = 'output.txt'

    def __init__(self):
        """Создает объекты, которые нужны для работы программы."""
        self.validator = InputValidator()
        self.file_manager = FileManager()

        self.current_digits = ''
        self.last_answer = ''

    def run(self):
        """Запускает программу и показывает меню, пока пользователь не выйдет."""
        self.print_program_description()

        is_running = True

        while is_running:
            self.print_menu()
            choice = input('Выберите пункт меню: ').strip()
            is_running = self.process_menu_choice(choice)

    def process_menu_choice(self, choice):
        """Выполняет действие по выбранному пункту меню."""
        try:
            if choice == '1':
                self.input_manually()
            elif choice == '2':
                self.input_from_file()
            elif choice == '3':
                self.show_current_data()
            elif choice == '0':
                print('Программа завершена.')
                return False
            else:
                print('Ошибка: такого пункта меню нет.')
        except InputValidationError as error:
            self.print_error(error)
        except FileManagerError as error:
            self.print_error(error)

        return True

    def print_program_description(self):
        """Показывает краткое описание программы."""
        print()
        print('Добро пожаловать в программу «Числовое кольцо»!')
        print()
        print('Здесь можно проверить строку цифр и найти в ней')
        print('равенство вида A+B=C.')
        print()
        print('Строка воспринимается как кольцо.')
        print('Это значит, что после последней цифры снова идет первая,')
        print('поэтому начинать чтение можно с любой позиции.')
        print()
        print('Программа будет пробовать разделить это кольцо на три подряд идущих числа:')
        print('A — первое слагаемое,')
        print('B — второе слагаемое,')
        print('C — сумма.')
        print()
        print('Пример:')
        print('Вход:  01902021')
        print('Ответ: 190+20=210')
        print()
        print('После ввода строки ответ сразу появится в консоли')
        print('и будет сохранен в файл output.txt.')

    def print_menu(self):
        """Показывает главное меню."""
        print()
        print('========== ГЛАВНОЕ МЕНЮ ==========')
        print('1. Ввести строку цифр вручную')
        print('2. Загрузить строку цифр из файла')
        print('3. Показать текущие данные')
        print('0. Выход')
        print('==================================')

    def input_manually(self):
        """Получает строку цифр от пользователя."""
        text = input('Введите строку цифр без пробелов: ').strip()
        self.process_new_digits(text)

    def input_from_file(self):
        """Получает строку цифр из файла."""
        file_path = input('Введите путь к входному файлу: ').strip()

        self.validator.validate_file_path(file_path)

        text = self.file_manager.read_digits_from_file(file_path)

        print('Строка успешно загружена из файла.')
        self.process_new_digits(text)

    def process_new_digits(self, text):
        """Проверяет строку, решает задачу и сохраняет ответ."""
        self.validator.validate_digits(text)

        self.current_digits = text
        self.last_answer = ''

        self.solve_and_save_answer()

    def solve_and_save_answer(self):
        """Ищет решение и записывает ответ в output.txt."""
        print()
        print('Идет поиск решения...')

        solver = RingEquationSolver(self.current_digits)
        self.last_answer = solver.solve()

        print()
        print('========== РЕЗУЛЬТАТ ==========')
        print('Входная строка:')
        print(self.current_digits)
        print()
        print('Ответ:')
        print(self.last_answer)
        print('===============================')

        self.file_manager.write_answer_to_file(
            self.OUTPUT_FILE_NAME,
            self.last_answer
        )

        print('Ответ записан в файл', self.OUTPUT_FILE_NAME)

    def show_current_data(self):
        """Показывает последнюю введенную строку и последний ответ."""
        if self.current_digits == '':
            print('Текущая строка еще не задана.')
            return

        print()
        print('========== ТЕКУЩИЕ ДАННЫЕ ==========')
        print('Текущая строка цифр:')
        print(self.current_digits)

        if self.last_answer != '':
            print()
            print('Последний найденный ответ:')
            print(self.last_answer)
        else:
            print()
            print('Решение для текущей строки еще не выполнялось.')

        print('====================================')

    def print_error(self, error):
        """Показывает ошибку и возвращает пользователя в меню."""
        print()
        print('Ошибка:', error)
        print('Операция отменена. Вы возвращены в главное меню.')