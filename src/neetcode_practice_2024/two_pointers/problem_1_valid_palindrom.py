#!/usr/bin/env python

import argparse
import argcomplete

from typing import Callable, List, Optional, Protocol, TypeVar
import collections
import functools


def solution_longest_palindromic_length(input: str) -> int:
    n = len(input)
    if n <= 1:
        return True

    # dp[i][j] stores whether the palindrom starting from input[i] and
    # finishing at input[j] (both ends included) is a palindrom.
    dp = [[False for _ in range(n)] for _ in range(n)]
    # Values we track along the way:
    max_length = 0

    for length in range(1, n + 1):
        for i in range(n + 1 - length):
            j = i + length - 1
            if 1 == length:
                is_palindrome = True
            elif 2 == length:
                is_palindrome = True and input[i] == input[j]
            else:
                is_palindrome = True and input[i] == input[j] and dp[i + 1][j - 1]
            dp[i][j] = is_palindrome
            if is_palindrome:
                max_length = max(max_length, length)

    return max_length


def solution_dp_bottom_up(input: str) -> bool:
    n = len(input)
    return n == solution_longest_palindromic_length(input)


def solution_stack(input: str) -> bool:
    n = len(input)
    if n <= 1:
        return True
    stack = []

    midpoint_end = n // 2
    midpoint_start = (n + 1) // 2
    stack.extend(input[:midpoint_end])
    for i in input[midpoint_start:]:
        item = stack.pop()
        if item != i:
            return False
    return True


def solution_straightforward(input: str) -> bool:
    left, right = 0, len(input) - 1
    while left < right:
        if input[left] != input[right]:
            return False
        left += 1
        right -= 1
    return True


def main(args):
    return solution_straightforward(args.input)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Neetcode 2024, two pointers, problem 1 valid palindrom."
    )
    parser.add_argument(
        "--input",
        "-i",
        type=str,
        required=True,
        help="The input string: `abc`.",
    )

    # https://kislyuk.github.io/argcomplete/#installation
    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    print(main(args))
    exit(0)
