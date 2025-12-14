from test_alg import universal_test_system
from test_for_all_tasks3 import task28


# Bellman-Ford`s algorithm
def func(graph, start):
    max_distance = 1001
    distance = {node[0]: max_distance for node in graph}

    distance[start] = 0

    for _ in range(len(distance) - 1):
        update = False

        for node, v, w in graph:
            if distance[node] != max_distance and distance[node] + w < distance[v]:
                distance[v] = distance[node] + w
                update = True

        if not update:
            break

    for node, v, w in graph:
        if distance[node] != max_distance and distance[node] + w < distance[v]:
            return "IMPOSSIBLE"

    result = []
    for ver, dist in distance.items():
        if dist == 1001:
            result.append("UNREACHABLE")
        else:
            result.append(dist)
    return result


name, solution, tasks = task28()

solution[name] = func

universal_test_system(solution, tasks)
