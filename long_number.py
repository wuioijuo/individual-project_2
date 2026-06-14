"""Работа с большими числами, записанными строками."""


class LongNumber:
    """Класс для сложения больших чисел без перевода в int."""

    def is_correct_notation(self, number):
        """Проверяет, нет ли лишних нулей в начале числа."""
        if number == "":
            return False

        if len(number) > 1 and number[0] == "0":
            return False

        return True

    def add(self, first_number, second_number):
        """Складывает два числа, записанных строками."""
        first_index = len(first_number) - 1
        second_index = len(second_number) - 1

        carry = 0
        result = []

        while first_index >= 0 or second_index >= 0 or carry > 0:
            digit_sum = carry

            if first_index >= 0:
                digit_sum += ord(first_number[first_index]) - ord("0")
                first_index -= 1

            if second_index >= 0:
                digit_sum += ord(second_number[second_index]) - ord("0")
                second_index -= 1

            result.append(chr(ord("0") + digit_sum % 10))
            carry = digit_sum // 10

        result.reverse()
        return "".join(result)