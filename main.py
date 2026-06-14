"""Точка запуска программы."""

from console_application import ConsoleApplication


def main():
    """Создает и запускает консольную программу."""
    application = ConsoleApplication()
    application.run()


if __name__ == '__main__':
    main()