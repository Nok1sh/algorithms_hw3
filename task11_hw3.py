from test_alg import universal_test_system
from test_for_all_tasks3 import task11


def func(s, t):
    if s == t:
        return 0

    n = len(s)
    m = len(t)

    matrix = []
    for _ in range(m+1):
        matrix.append([0]*(n+1))

    for i in range(n+1):
        matrix[0][i] = i

    for i in range(m+1):
        matrix[i][0] = i

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[j-1] == t[i-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = 1 + min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) # удаление, вставка и замена
    return matrix[m][n]


name, solution, tasks = task11()

solution[name] = func

universal_test_system(solution, tasks)



