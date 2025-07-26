#!/usr/bin/env python

import numpy as np
import numpy.linalg as linalg

import argparse
import argcomplete

from typing import Callable, List, Optional, Protocol, TypeVar
import collections
import functools


# Beats 99.42 % of other submissions.
# Initially from ChatGPT, and then optimised manually as I thought.
def solution(matrix: list[list[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]  # Memoisation table

    def dfs(i: int, j: int) -> int:
        if dp[i][j] != 0:
            return dp[i][j]
        x = matrix[i][j]

        dp[i][j] = 1 + max(
            dfs(i - 1, j) if i > 0 and matrix[i - 1][j] > x else 0,
            dfs(i + 1, j) if i < m - 1 and matrix[i + 1][j] > x else 0,
            dfs(i, j - 1) if j > 0 and matrix[i][j - 1] > x else 0,
            dfs(i, j + 1) if j < n - 1 and matrix[i][j + 1] > x else 0,
        )

        return dp[i][j]

    return max(dfs(i, j) for i in range(m) for j in range(n))


# Beats 98.25 % of other submissions.
# Not from me, from ChatGPT.
def solution2(self, matrix: list[list[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]  # Memoisation table

    def dfs(i: int, j: int) -> int:
        if dp[i][j] != 0:
            return dp[i][j]

        val = matrix[i][j]
        best = 1  # Minimum path length starting here is 1 (the cell itself)

        # Unrolled directional checks
        if i > 0 and matrix[i - 1][j] > val:
            best = max(best, 1 + dfs(i - 1, j))
        if i < m - 1 and matrix[i + 1][j] > val:
            best = max(best, 1 + dfs(i + 1, j))
        if j > 0 and matrix[i][j - 1] > val:
            best = max(best, 1 + dfs(i, j - 1))
        if j < n - 1 and matrix[i][j + 1] > val:
            best = max(best, 1 + dfs(i, j + 1))

        dp[i][j] = best
        return best

    return max(dfs(i, j) for i in range(m) for j in range(n))


# Beats 96 % of other submissions.
def solution3(self, matrix: List[List[int]]) -> int:
    if 1 == len(matrix) and 1 == len(matrix[0]):
        return 1

    @functools.cache
    def dfs(i, j):
        return max(
            0,
            (
                (1 + dfs(i + 1, j))
                if (i + 1 < len(matrix) and matrix[i][j] < matrix[i + 1][j])
                else 0
            ),
            (
                (1 + dfs(i, j + 1))
                if (j + 1 < len(matrix[0]) and matrix[i][j] < matrix[i][j + 1])
                else 0
            ),
            (
                (1 + dfs(i - 1, j))
                if (0 <= i - 1 and matrix[i][j] < matrix[i - 1][j])
                else 0
            ),
            (
                (1 + dfs(i, j - 1))
                if (0 <= j - 1 and matrix[i][j] < matrix[i][j - 1])
                else 0
            ),
        )

    return 1 + max(
        [dfs(i, j) for i in range(len(matrix)) for j in range(len(matrix[0]))]
    )


# Beats 95.61 % of other submissions.
def solution4(self, matrix: List[List[int]]) -> int:
    if 1 == len(matrix) and 1 == len(matrix[0]):
        return 1

    @functools.cache
    def dfs(i, j):
        if not (0 <= i and i < len(matrix)):
            return 0
        elif not (0 <= j and j < len(matrix[0])):
            return 0
        x = matrix[i][j]

        return max(
            0,
            (
                (1 + dfs(i + 1, j))
                if (i + 1 < len(matrix) and x < matrix[i + 1][j])
                else 0
            ),
            (
                (1 + dfs(i, j + 1))
                if (j + 1 < len(matrix[0]) and x < matrix[i][j + 1])
                else 0
            ),
            (1 + dfs(i - 1, j)) if (0 <= i - 1 and x < matrix[i - 1][j]) else 0,
            (1 + dfs(i, j - 1)) if (0 <= j - 1 and x < matrix[i][j - 1]) else 0,
        )

    return 1 + max(
        [dfs(i, j) for i in range(len(matrix)) for j in range(len(matrix[0]))]
    )


# Beats 62.34 % of other submissions.
# Not from me, from Neetcode
def solution5(self, matrix: List[List[int]]) -> int:
    ROWS, COLS = len(matrix), len(matrix[0])
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    indegree = [[0] * COLS for _ in range(ROWS)]

    for r in range(ROWS):
        for c in range(COLS):
            for d in directions:
                nr, nc = d[0] + r, d[1] + c
                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] < matrix[r][c]:
                    indegree[r][c] += 1

    q = deque()
    for r in range(ROWS):
        for c in range(COLS):
            if indegree[r][c] == 0:
                q.append([r, c])

    LIS = 0
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[r][c]:
                    indegree[nr][nc] -= 1
                    if indegree[nr][nc] == 0:
                        q.append([nr, nc])
        LIS += 1
    return LIS


# Beats 5.21 % of other submissions.
def solution6(self, matrix: List[List[int]]) -> int:
    if 1 == len(matrix) and 1 == len(matrix[0]):
        return 1

    @functools.cache
    def dfs(v, i, j):
        if v < matrix[i][j]:
            return 1 + max(
                dfs(matrix[i][j], i + 1, j) if i + 1 < len(matrix) else 0,
                dfs(matrix[i][j], i, j + 1) if j + 1 < len(matrix[0]) else 0,
                dfs(matrix[i][j], i - 1, j) if 0 <= i - 1 else 0,
                dfs(matrix[i][j], i, j - 1) if 0 <= j - 1 else 0,
            )
        return 0

    max_value = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            max_value = max(max_value, dfs(-1, i, j))
    return max_value


# Beats 6.06 % of other submissions.
def solution7(self, matrix: List[List[int]]) -> int:
    if 1 == len(matrix) and 1 == len(matrix[0]):
        return 1

    @functools.cache
    def dfs(v, i, j):
        if v < matrix[i][j]:
            return 1 + max(
                dfs(matrix[i][j], i + 1, j) if i + 1 < len(matrix) else 0,
                dfs(matrix[i][j], i, j + 1) if j + 1 < len(matrix[0]) else 0,
                dfs(matrix[i][j], i - 1, j) if 0 <= i - 1 else 0,
                dfs(matrix[i][j], i, j - 1) if 0 <= j - 1 else 0,
            )
        return 0

    return max(
        [dfs(-1, i, j) for i in range(len(matrix)) for j in range(len(matrix[0]))]
    )


def main(args):
    return solution(args.input)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=", ".join(
            "Neetcode 2024",
            "XXX",
            "problem XXX.",
        )
    )
    parser.add_argument(
        "--input",
        "-i",
        type=lambda s: [int(i) for i in s.split(",")],
        required=True,
        help="The input array as a comma-separated list of integers: `1,2,3`.",
    )

    # https://kislyuk.github.io/argcomplete/#installation
    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    print(main(args))
    exit(0)
