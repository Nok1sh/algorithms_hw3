from test_alg import universal_test_system
from test_for_all_tasks3 import task26


def dfs(graph, x, y, height, width):
    if not(x < 0 or y < 0 or x >= height or y >= width) and graph[x][y] == "+":
        graph[x][y] = "x"

        dfs(graph, x - 1, y, height, width)
        dfs(graph, x + 1, y, height, width)
        dfs(graph, x, y - 1, height, width)
        dfs(graph, x, y + 1, height, width)


def func(graph, height, width):
    count_carpets = 0

    for x in range(height):
        for y in range(width):
            if graph[x][y] == "+":
                dfs(graph, x, y, height, width)
                count_carpets += 1

    return count_carpets


name, solution, tasks = task26()

solution[name] = func

universal_test_system(solution, tasks)