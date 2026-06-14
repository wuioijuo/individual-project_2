"""Узел двусвязного списка."""


class DigitNode:
    """Один элемент кольца."""
    def __init__(self, digit):
        """Создает узел, в котором хранится одна цифра."""
        self.digit = digit
        self.next = None
        self.prev = None