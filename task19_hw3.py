from test_alg import universal_test_system
from test_for_all_tasks3 import task19


def func(n, a, b):

    first_album = []
    second_album = []

    for _ in range(n+1):
        first_album.append([0] * (a+1))
        second_album.append([0]*(b+1))

    first_album[1][1] = 1
    second_album[1][1] = 1

    for i in range(2, n+1):

        ending_2 = 0
        for j in range(1, b+1):
            ending_2 += second_album[i-1][j]

        first_album[i][1] = ending_2

        for j in range(2, a+1):
            first_album[i][j] = first_album[i-1][j-1]

        ending_1 = 0
        for j in range(1, a + 1):
            ending_1 += first_album[i - 1][j]

        second_album[i][1] = ending_1

        for j in range(2, b + 1):
            second_album[i][j] = second_album[i - 1][j - 1]

    result = 0
    for i in range(a+1):
        result += first_album[n][i]
    for i in range(b+1):
        result += second_album[n][i]
    return result % (10**9 + 7)


name, solution, tasks = task19()

solution[name] = func

universal_test_system(solution, tasks)
