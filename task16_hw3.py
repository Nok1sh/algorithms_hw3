from test_alg import universal_test_system
from test_for_all_tasks3 import task16


def func(n, m):

    half_len = n//2

    maximum_sum = m * half_len

    dp = []  #  первый индекс - количество используемых цифр, второй - сумма
    for _ in range(half_len+1):
        dp.append([0] * (maximum_sum+1))

    dp[0][0] = 1

    for i in range(1, half_len+1):
        for s in range(0, maximum_sum+1):
            current_sum = 0
            for digit in range(m):
                if s - digit >= 0:
                    current_sum += dp[i-1][s-digit]

            dp[i][s] = current_sum

    result = 0
    for s in range(maximum_sum+1):
        result += dp[half_len][s]**2
    return result


name, solution, tasks = task16()

solution[name] = func

universal_test_system(solution, tasks)