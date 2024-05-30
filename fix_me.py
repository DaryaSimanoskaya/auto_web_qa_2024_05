"""Модуль для расчёта среднего значения списка чисел."""


def calculate_average(numbers) -> float:
    """
    Вычисляет среднее значение списка чисел.

    Args:
        numbers (list of float|int): Список чисел.

    Returns:
        float: Среднее значение чисел.
    """
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)
