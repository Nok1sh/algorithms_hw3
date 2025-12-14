from test_alg import universal_test_system
from test_for_all_tasks3 import task22
from tools.mergesort import MergeSort


def find(parents, v):
    if parents[v] != v:
        parents[v] = find(parents, parents[v])
    return parents[v]


def union(parents, ranks, x, y):

    root_x = find(parents, x)
    root_y = find(parents, y)

    if root_x != root_y:
        if ranks[root_x] > ranks[root_y]:
            parents[root_y] = root_x
        elif ranks[root_x] < ranks[root_y]:
            parents[root_x] = root_y
        else:
            parents[root_x] = root_y
            ranks[root_y] += 1


# Kruskal`s algorithm
def func(n, m, graph):

    graph = MergeSort.merge_graph(graph)

    parents = {v : v for v in range(1, n+1)}
    ranks = {r: 0 for r in range(1, n+1)}

    i = 0
    vertexes = n
    result = []

    for u, v, w in graph:
        i += 1

        x = find(parents, u)
        y = find(parents, v)

        if x != y:
            vertexes -= 1
            result.append((u, v, w))
            union(parents, ranks, x, y)

    if vertexes > 1:
        return "Oops! I did it again"
    sum_result = 0
    for i in result:
        sum_result += i[2]
    return sum_result


name, solution, tasks = task22()

solution[name] = func

universal_test_system(solution, tasks)