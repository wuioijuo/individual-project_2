"""Кольцо цифр на основе двусвязного списка."""

from digit_node import DigitNode


class DigitRing:
    """Циклический двусвязный список для хранения цифр."""

    def __init__(self, digits):
        """Создает кольцо из строки цифр."""
        self.head = None
        self.size = 0

        for digit in digits:
            self.append(digit)

    def append(self, digit):
        """Добавляет цифру в конец кольца."""
        new_node = DigitNode(digit)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            tail = self.head.prev

            tail.next = new_node
            new_node.prev = tail

            new_node.next = self.head
            self.head.prev = new_node

        self.size += 1

    def to_string(self):
        """Возвращает все цифры кольца в виде строки."""
        if self.head is None:
            return ""

        result = []
        current_node = self.head

        for _ in range(self.size):
            result.append(current_node.digit)
            current_node = current_node.next

        return "".join(result)

    def to_doubled_string(self):
        """Возвращает строку, повторенную два раза."""
        text = self.to_string()
        return text + text