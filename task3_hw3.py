from test_alg import universal_test_system
from test_for_all_tasks3 import task3
from tools.mergesort import MergeSort


def func(l, n, array):

    intervals = []
    for i in range(n):
        point = array[i]
        intervals.append((point - l, point + l))

    intervals = MergeSort.merge_inter(intervals)

    count_points = 0
    last = -10**9-1
    for left, right in intervals:
        if left > last:
            count_points += 1
            last = right

    return count_points


name, solution, tasks = task3()

solution[name] = func

universal_test_system(solution, tasks)
