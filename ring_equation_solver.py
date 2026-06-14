"""Поиск равенства A+B=C в числовом кольце."""

from digit_ring import DigitRing
from long_number import LongNumber


class RingEquationSolver:
    """Класс для решения задачи про числовое кольцо."""

    NO_ANSWER = "No"

    def __init__(self, digits):
        """Подготавливает строку цифр к поиску решения."""
        self.digits = digits.strip()
        self.digits_count = len(self.digits)

        self.ring = DigitRing(self.digits)
        self.doubled_digits = self.ring.to_doubled_string()

        self.long_number = LongNumber()
        self.prefix_digit_sum = []

        self.build_prefix_digit_sum()

    def solve(self):
        """Ищет любое равенство A+B=C."""
        if self.digits_count < 3 or self.digits_count > 1000:
            return self.NO_ANSWER

        if not self.contains_only_digits(self.digits):
            return self.NO_ANSWER

        for start_position in range(self.digits_count):
            for first_length in range(1, self.digits_count - 1):
                possible_lengths = self.get_possible_lengths(first_length)

                for lengths in possible_lengths:
                    second_length = lengths[0]
                    sum_length = lengths[1]

                    result = self.check_variant(
                        start_position,
                        first_length,
                        second_length,
                        sum_length
                    )

                    if result != "":
                        return result

        return self.NO_ANSWER

    def contains_only_digits(self, text):
        """Проверяет, что строка состоит только из цифр."""
        if text == "":
            return False

        for symbol in text:
            if symbol < "0" or symbol > "9":
                return False

        return True

    def build_prefix_digit_sum(self):
        """Считает суммы цифр от начала строки до каждой позиции."""
        self.prefix_digit_sum = [0] * (len(self.doubled_digits) + 1)

        for index in range(len(self.doubled_digits)):
            digit = ord(self.doubled_digits[index]) - ord("0")
            self.prefix_digit_sum[index + 1] = (
                self.prefix_digit_sum[index] + digit
            )

    def get_possible_lengths(self, first_length):
        """Подбирает возможные длины второго числа и суммы."""
        variants = []

        # Сумма двух чисел может иметь длину как у большего числа
        # или быть длиннее него на одну цифру.
        second_length = self.digits_count - first_length - first_length

        if 1 <= second_length <= first_length:
            variants.append([second_length, first_length])

        second_length = self.digits_count - first_length - first_length - 1

        if 1 <= second_length <= first_length:
            variants.append([second_length, first_length + 1])

        remaining_length = self.digits_count - first_length

        if remaining_length % 2 == 0:
            second_length = remaining_length // 2

            if second_length > first_length:
                variants.append([second_length, second_length])

        remaining_length = self.digits_count - first_length - 1

        if remaining_length > 0 and remaining_length % 2 == 0:
            second_length = remaining_length // 2

            if second_length > first_length:
                variants.append([second_length, second_length + 1])

        return variants

    def check_variant(
        self,
        start_position,
        first_length,
        second_length,
        sum_length
    ):
        """Проверяет один вариант разбиения кольца на A, B и C."""
        first_start = start_position
        second_start = first_start + first_length
        sum_start = second_start + second_length

        if not self.is_correct_segment(first_start, first_length):
            return ""

        if not self.is_correct_segment(second_start, second_length):
            return ""

        if not self.is_correct_segment(sum_start, sum_length):
            return ""

        if not self.quick_check(
            first_start,
            first_length,
            second_start,
            second_length,
            sum_start,
            sum_length
        ):
            return ""

        first_number = self.get_segment_as_string(first_start, first_length)
        second_number = self.get_segment_as_string(
            second_start,
            second_length
        )
        sum_number = self.get_segment_as_string(sum_start, sum_length)

        if self.long_number.add(first_number, second_number) == sum_number:
            return first_number + "+" + second_number + "=" + sum_number

        return ""

    def is_correct_segment(self, start_position, length):
        """Проверяет, можно ли считать участок обычным числом."""
        if length <= 0:
            return False

        if start_position < 0:
            return False

        if start_position + length > len(self.doubled_digits):
            return False

        if length > 1 and self.doubled_digits[start_position] == "0":
            return False

        return True

    def get_segment_as_string(self, start_position, length):
        """Возвращает часть строки по началу и длине."""
        return self.doubled_digits[start_position:start_position + length]

    def quick_check(
        self,
        first_start,
        first_length,
        second_start,
        second_length,
        sum_start,
        sum_length
    ):
        """Быстро отбрасывает варианты, которые точно не подходят."""
        last_first = ord(
            self.doubled_digits[first_start + first_length - 1]
        ) - ord("0")
        last_second = ord(
            self.doubled_digits[second_start + second_length - 1]
        ) - ord("0")
        last_sum = ord(
            self.doubled_digits[sum_start + sum_length - 1]
        ) - ord("0")

        # Последняя цифра A+B должна совпадать с последней цифрой C.
        if (last_first + last_second) % 10 != last_sum:
            return False

        first_mod = self.segment_digit_sum_mod_9(first_start, first_length)
        second_mod = self.segment_digit_sum_mod_9(
            second_start,
            second_length
        )
        sum_mod = self.segment_digit_sum_mod_9(sum_start, sum_length)

        # Остаток числа по 9 можно найти через сумму его цифр.
        if (first_mod + second_mod - sum_mod) % 9 != 0:
            return False

        return True

    def segment_digit_sum_mod_9(self, start_position, length):
        """Возвращает сумму цифр участка по модулю 9."""
        digit_sum = (
            self.prefix_digit_sum[start_position + length]
            - self.prefix_digit_sum[start_position]
        )

        return digit_sum % 9