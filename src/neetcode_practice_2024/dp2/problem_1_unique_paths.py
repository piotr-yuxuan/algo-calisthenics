#!/usr/bin/env python

import argparse
import argcomplete


def solution(m: int, n: int) -> int:
    if 1 == m or 1 == n:
        return 1

    # dp[m-1][n-1] for m lines, n columns.
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[-1][-2] = 1
    dp[-2][-1] = 1
    for j in reversed(range(n)):
        for i in reversed(range(m)):
            dp[i][j] = (
                dp[i][j]
                + (dp[i + 1][j] if i + 1 < m else 0)
                + (dp[i][j + 1] if j + 1 < n else 0)
            )

    return dp[0][0]


def main(args):
    return solution(args.m, args.n)
