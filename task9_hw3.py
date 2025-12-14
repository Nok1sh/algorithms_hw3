from test_alg import universal_test_system
from test_for_all_tasks3 import task9

numbers = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4,
           5: 5, 6: 6, 7:3, 8: 7, 9: 6}


def create_max_number(n, k):
    result = ""
    for i in range(n):
        digit = 9
        while not(numbers[digit] <= k and (k - numbers[digit]) >= (n-i-1)*2):
            digit -= 1
        k -= numbers[digit]
        result += str(digit)
    return result


def create_min_number(n, k):
    result = ""
    for i in range(n):
        digit = 1 if i == 0 else 0
        while not(numbers[digit] <= k
                  and (k - numbers[digit]) >= (n - i - 1) * 2
                  and (k - numbers[digit]) <= (n - i - 1) * 7):
            digit += 1
        k -= numbers[digit]
        result += str(digit)
    return result


def func(n, k):
    minimum_count_k = numbers[1] * n
    if minimum_count_k > k:
        return "NO SOLUTION"
    elif minimum_count_k == k:
        number = "1" * n
        return number, number

    max_number = create_max_number(n, k)
    min_number = create_min_number(n, k)
    return min_number, max_number


name, solution, tasks = task9()

solution[name] = func

universal_test_system(solution, tasks)