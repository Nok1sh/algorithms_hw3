def task3():
    tests = {
        "Задание 3": [
            {"input": [10, 5, [30, 3, 14, 19, 21]], "expected": 2},
            {"input": [1, 2, [0, 2]], "expected": 1},
            {"input": [1, 2, [0, 3]], "expected": 2},
            {"input": [2, 3, [0, 2, 4]], "expected": 1},
            {"input": [3, 3, [0, 2, 4]], "expected": 1},
            {"input": [0, 5, [1, 2, 3, 4, 5]], "expected": 5},
            {"input": [100, 3, [0, 100, 200]], "expected": 1},
            {"input": [5, 4, [0, 1, 2, 3]], "expected": 1},
            {"input": [3, 6, [0, 1, 4, 5, 8, 9]], "expected": 2},
            {"input": [1, 1, [42]], "expected": 1},
            {"input": [10, 7, [1, 2, 3, 10, 11, 12, 13]], "expected": 1},
        ]
    }

    solution = {
        "Задание 3": None
    }

    return "Задание 3", solution, tests


def task5():
    tests = {
        "Задание 5": [
            {"input": [1, 3], "expected": "0.(3)"},
            {"input": [1, 6], "expected": "0.1(6)"},
            {"input": [1, 7], "expected": "0.(142857)"},
            {"input": [1, 10], "expected": "0.1"},
            {"input": [1, 12], "expected": "0.08(3)"},
            {"input": [1, 16], "expected": "0.0625"},
            {"input": [3, 8], "expected": "0.375"},
            {"input": [5, 14], "expected": "0.3(571428)"},
            {"input": [1, 17], "expected": "0.(0588235294117647)"},
            {"input": [11, 30], "expected": "0.3(6)"}
        ]
    }
    solution = {
        "Задание 5": None
    }
    return "Задание 5", solution, tests


def task9():
    tests = {
        "Задание 9": [
            {"input": [5, 15], "expected": ("10117", "97111")},
            {"input": [1, 2], "expected": ("1", "1")},
            {"input": [1, 3], "expected": ("7", "7")},
            {"input": [1, 7], "expected": ("8", "9")},
            {"input": [2, 4], "expected": ("11", "11")},
            {"input": [2, 5], "expected": ("17", "71")},
            {"input": [2, 10], "expected": ("22", "97S")},
            {"input": [3, 6], "expected": ("111", "111")},
            {"input": [3, 9], "expected": ("112", "777")},
            {"input": [10, 1], "expected": "NO SOLUTION"}
        ]
    }
    solution = {
        "Задание 9": None
    }
    return "Задание 9", solution, tests


def task11():
    tests = {
        "Задание 11": [
            {"input": ["abacaba", "abaabc"], "expected": 2},
            {"input": ["algorithm", "logarithm"], "expected": 3},
            {"input": ["abcde", "edcba"], "expected": 4},
            {"input": ["intention", "execution"], "expected": 5},
            {"input": ["cat", "catsup"], "expected": 3},
            {"input": ["banana", "ban"], "expected": 3},
            {"input": ["levenshtein", "levenshtein"], "expected": 0},
            {"input": ["", "distance"], "expected": 8},
            {"input": ["aaaa", "a"], "expected": 3},
            {"input": ["z", "q"], "expected": 1}
        ]
    }
    solution = {
        "Задание 11": None
    }
    return "Задание 11", solution, tests


def task16():
    tests = {
        "Задание 16": [
            {"input": [6, 10], "expected": 55252},
            {"input": [28, 12], "expected": 35806106077437501422929813320},
            {"input": [2, 10], "expected": 10},
            {"input": [4, 10], "expected": 670},
            {"input": [2, 2], "expected": 2},
            {"input": [4, 2], "expected": 6},
            {"input": [28, 12], "expected": 35806106077437501422929813320},
            {"input": [6, 2], "expected": 20},
            {"input": [8, 10], "expected": 4816030}
        ]
    }
    solution = {
        "Задание 16": None
    }
    return "Задание 16", solution, tests


def task19():
    tests = {
        "Задание 19": [
            {"input": [3, 2, 1], "expected": 4},
            {"input": [5, 3, 2], "expected": 21},
            {"input": [4, 1, 1], "expected": 2},
            {"input": [6, 4, 3], "expected": 53},
            {"input": [10, 5, 5], "expected": 928},
            {"input": [7, 3, 3], "expected": 88},
            {"input": [2, 1, 1], "expected": 2},
            {"input": [8, 4, 2], "expected": 131},
            {"input": [1, 1, 1], "expected": 2},
            {"input": [10, 1, 1], "expected": 2},
        ]
    }
    solution = {"Задание 19": None}
    return "Задание 19", solution, tests


def task22():
    tests = {
        "Задание 22": [
            {"input": [4, 4, [[1, 2, 5], [1, 3, 6], [2, 4, 8], [3, 4, 3]]], "expected": 19},
            {"input": [3, 3, [[1, 2, 1], [1, 2, 2], [2, 3, 1]]], "expected": 3},
            {"input": [2, 0, []], "expected": "Oops! I did it again"},
            {"input": [1, 0, []], "expected": 0},
            {"input": [5, 7, [[1, 2, 10], [1, 3, 6], [2, 3, 5], [2, 4, 8], [3, 4, 7], [3, 5, 3], [4, 5, 9]]], "expected": 34},
            {"input": [3, 1, [[1, 2, 4]]], "expected": "Oops! I did it again"},
            {"input": [4, 2, [[1, 2, 1], [3, 4, 2]]], "expected": "Oops! I did it again"},
            {"input": [4, 5, [[1, 2, 1], [2, 3, 2], [3, 4, 3], [1, 4, 4], [2, 4, 5]]], "expected": 12},
            {"input": [2, 1, [[1, 2, 100]]], "expected": 100},
            {"input": [3, 2, [[1, 2, 1], [2, 3, 2]]], "expected": 3}
        ]
    }
    solution = {
        "Задание 22": None
    }
    return "Задание 22", solution, tests


def task26():
    tests = {
        "Задание 26": [
            {
                "input": [
                    [
                        ['.', '+', '+', '+', '.', '+'],
                        ['+', '.', '.', '.', '.', '.'],
                        ['+', '+', '+', '.', '.', '.'],
                        ['+', '.', '+', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.'],
                        ['+', '+', '.', '.', '.', '.']
                    ],
                    6,
                    6
                ],
                "expected": 6
            },
            {
                "input": [
                    [
                        ['.', '+', '+', '.', '.', '+', '+', '.', '+', '+'],
                        ['+', '.', '+', '.', '.', '.', '+', '+', '+', '+'],
                        ['.', '.', '.', '.', '.', '.', '.', '.', '+', '+'],
                        ['+', '.', '.', '.', '+', '+', '.', '.', '.', '.'],
                        ['+', '+', '+', '+', '.', '+', '+', '+', '.', '+'],
                        ['.', '.', '.', '.', '+', '.', '+', '.', '.', '.'],
                        ['+', '.', '+', '.', '+', '+', '+', '+', '+', '+'],
                        ['+', '+', '+', '+', '.', '+', '+', '.', '.', '+'],
                        ['+', '+', '+', '+', '+', '.', '.', '+', '+', '.'],
                        ['+', '.', '.', '.', '+', '.', '+', '.', '.', '.']
                    ],
                    10,
                    10
                ],
                "expected": 9
            },
            {
                "input": [
                    [
                        ['.', '+', '.', '.', '.'],
                        ['.', '+', '+', '+', '.'],
                        ['.', '+', '.', '+', '.'],
                        ['+', '+', '.', '+', '+'],
                        ['+', '+', '+', '+', '+']
                    ],
                    5,
                    5
                ],
                "expected": 1
            },
            {
                "input": [
                    [
                        ['+', '+', '+', '+'],
                        ['+', '+', '+', '+'],
                        ['+', '+', '+', '+'],
                        ['+', '+', '+', '+']
                    ],
                    4,
                    4
                ],
                "expected": 1
            },
            {
                "input": [
                    [
                        ['.'],
                        ['.'],
                        ['.']
                    ],
                    3,
                    1
                ],
                "expected": 0
            },
            {
                "input": [
                    [
                        ['+'],
                        ['+'],
                        ['+']
                    ],
                    3,
                    1
                ],
                "expected": 1
            },
            {
                "input": [
                    [
                        ['+', '.', '+'],
                        ['.', '+', '.'],
                        ['+', '.', '+']
                    ],
                    3,
                    3
                ],
                "expected": 5
            },
            {
                "input": [
                    [
                        ['+', '+'],
                        ['+', '+']
                    ],
                    2,
                    2
                ],
                "expected": 1
            },
            {
                "input": [
                    [
                        ['+', '.', '+'],
                        ['+', '.', '+'],
                        ['+', '.', '+']
                    ],
                    3,
                    3
                ],
                "expected": 2
            },
            {
                "input": [
                    [
                        ['+', '+', '+', '+', '+'],
                        ['+', '+', '+', '+', '+'],
                        ['+', '+', '+', '+', '+'],
                        ['+', '+', '+', '+', '+'],
                        ['+', '+', '+', '+', '+']
                    ],
                    5,
                    5
                ],
                "expected": 1
            }
        ]
    }
    solution = {
        "Задание 26": None
    }
    return "Задание 26", solution, tests


def task28():
    tests = {
        "Задание 28": [
            {
                "input": [
                    [(0, 1, 100), (1, 2, 100), (2, 0, -100), (0, 2, 1000), (3, 1, 15)],
                    0
                ],
                "expected": [0, 100, 200, "UNREACHABLE"]
            },
            {
                "input": [
                    [(0, 1, 5), (1, 2, 8), (2, 0, -20)],
                    0
                ],
                "expected": "IMPOSSIBLE"
            },
            {
                "input": [
                    [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 4, 1), (0, 4, 10), (4, 0, -5)],
                    0
                ],
                "expected": "IMPOSSIBLE"
            },
            {
                "input": [
                    [],
                    0
                ],
                "expected": [0]
            },
            {
                "input": [
                    [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 0, -4)],
                    0
                ],
                "expected": "IMPOSSIBLE"
            },
            {
                "input": [
                    [(2, 3, 5), (3, 4, -2), (4, 2, -1)],
                    0
                ],
                "expected": ["UNREACHABLE", "UNREACHABLE", "UNREACHABLE", "UNREACHABLE", 0]
            }
        ]
    }
    solution = {
        "Задание 28": None
    }
    return "Задание 28", solution, tests


def task34():
    tests = {
        "Задание 34": [
            {
                "input": [
                    [(6, 5, 10), (1, 4, 11), (1, 2, 4), (3, 1, 5), (2, 4, 5), (6, 3, 1), (6, 1, 3)],
                    6,
                    4
                ],
                "expected": 17
            },
            {
                "input": [
                    [(1, 2, 5), (2, 3, 3)],
                    1,
                    3
                ],
                "expected": 8
            },
            {
                "input": [
                    [(1, 2, 1), (2, 3, 2), (3, 4, 3)],
                    1,
                    4
                ],
                "expected": 6
            },
            {
                "input": [
                    [(1, 2, 100)],
                    1,
                    2
                ],
                "expected": 100
            },
            {
                "input": [
                    [(1, 2, 1), (2, 3, 1), (3, 4, 1), (4, 5, 1)],
                    1,
                    5
                ],
                "expected": 4
            },
            {
                "input": [
                    [(1, 2, 1), (2, 3, 1), (1, 3, 5)],
                    1,
                    3
                ],
                "expected": 5
            },
            {
                "input": [
                    [(1, 2, 1), (2, 3, 1), (3, 5, 10), (1, 4, 5), (4, 5, 1)],
                    1,
                    5
                ],
                "expected": 12
            },
            {
                "input": [
                    [],
                    1,
                    1
                ],
                "expected": "No solution"
            }
        ]
    }
    solution = {
        "Задание 34": None
    }
    return "Задание 34", solution, tests