from test_alg import universal_test_system
from test_for_all_tasks3 import task34


# Bellman-Ford`s algorithm
def func(graph, start, end):
    nodes = set()
    for u, v, _ in graph:
        nodes.add(u)
        nodes.add(v)

    distance = {node: -1 for node in nodes}
    parent = {node: None for node in nodes}

    distance[start] = 0

    for _ in range(len(nodes) - 1):
        update = False

        for node, v, w in graph:
            if distance[node] != -1 and distance[node] + w > distance[v]:
                distance[v] = distance[node] + w
                parent[v] = node
                update = True

        if not update:
            break

    return distance[end] if distance[end] > 0 else "No solution"


name, solution, tasks = task34()

solution[name] = func

universal_test_system(solution, tasks)
