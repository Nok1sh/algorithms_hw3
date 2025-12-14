from test_alg import universal_test_system
from test_for_all_tasks3 import task5


def division_two_and_five(number):
    non_repeat_2 = 0
    non_repeat_5 = 0
    while number % 2 == 0:
        number //= 2
        non_repeat_2 += 1
    while number % 5 == 0:
        number //= 5
        non_repeat_5 += 1
    return number, max(non_repeat_2, non_repeat_5)


def find_length_period_part(den):
    new_d, non_repeat = division_two_and_five(den)

    if new_d == 1:
        return 0, 0

    length_part = 1
    remain = 10 % new_d
    while remain != 1:
        remain = (remain*10)%new_d
        length_part += 1
        if length_part > new_d:
            break
    return length_part, non_repeat


def func(n, m):
    repeat_length, non_repeat_length = find_length_period_part(m)
    result = n / m
    if repeat_length == 0:
        return result
    result = str(result)
    return result[:non_repeat_length+2] + f"({result[non_repeat_length+2:non_repeat_length+repeat_length+2]})"


name, solution, tasks = task5()

solution[name] = func

universal_test_system(solution, tasks)