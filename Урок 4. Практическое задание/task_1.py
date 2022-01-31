"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = []
    [new_arr.append(i) for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


def func_3(nums):
    new_arr = filter(lambda i: nums[i] % 2 == 0, range(len(nums)))
    return list(new_arr)


def func_4(nums):
    new_arr = []
    for i, num in enumerate(nums):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


if __name__ == '__main__':
    import timeit

    # print(func_1(nums=[547398, 5, 56345, 56, 436, 990, 932, 5, 322, 564, 322, 33, 32345, 55]))
    # print(func_2(nums=[547398, 5, 56345, 56, 436, 990, 932, 5, 322, 564, 322, 33, 32345, 55]))
    # print(func_3(nums=[547398, 5, 56345, 56, 436, 990, 932, 5, 322, 564, 322, 33, 32345, 55]))
    # print(func_4(nums=[547398, 5, 56345, 56, 436, 990, 932, 5, 322, 564, 322, 33, 32345, 55]))

    t = timeit.Timer(lambda: func_1(nums=[547398, 5, 56345, 56, 436, 990, 932, 5, 322, 564, 322, 33, 32345, 55]))
    print(t.repeat(3))
    t = timeit.Timer(lambda: func_2(nums=[547398, 5, 56345, 56, 436, 990, 932, 5, 322, 564, 322, 33, 32345, 55]))
    print(t.repeat(3))
    t = timeit.Timer(lambda: func_3(nums=[547398, 5, 56345, 56, 436, 990, 932, 5, 322, 564, 322, 33, 32345, 55]))
    print(t.repeat(3))
    t = timeit.Timer(lambda: func_4(nums=[547398, 5, 56345, 56, 436, 990, 932, 5, 322, 564, 322, 33, 32345, 55]))
    print(t.repeat(3))

    # Из четырех вариантов быстрее выполнятся обычный цикл for.
    # Вариант с использованием оптимизированной функции enumerate дает приблизительно схожие с циклом результаты
    # (однако, чем больше массив, тем больше видна разница в скорости в пользу цикла c range).
    # LC выполняется немного дольше обычного цикла.
    # Самым долгим оказалось использование функции filter при условии преобразования в список
    # для получения идентичного типа данных на выходе.
