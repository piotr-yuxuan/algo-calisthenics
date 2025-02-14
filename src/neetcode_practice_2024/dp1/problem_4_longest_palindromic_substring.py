#!/usr/bin/env python

import argparse
import argcomplete

from typing import Callable, List, Optional, Protocol, TypeVar
import collections
import functools


def _is_palindrome(s: str) -> bool:
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False

    return True


def solution_brute_force(input: str) -> str:
    n = len(input)

    # Keep track of these values
    max_length: int = 0
    some_string_max_length: str = ""

    for i in range(n):
        for j in range(i + 1, n + 1):
            if _is_palindrome(input[i:j]):
                length = j - i
                max_length = max(max_length, length)
                if max_length <= length:
                    some_string_max_length = input[i:j]

    return some_string_max_length


# Inclusive start, exclusive end.
def _is_palindrome_index(input, start: int, stop: int) -> bool:
    for i in range((stop - start) // 2):
        # Somehow I thought I could remove `start` from `start + i`
        # but it turns out not to be possible.
        if input[start + i] != input[stop - 1 - i]:
            return False

    return True


def solution_brute_force_space_optimised(input: str) -> str:
    n = len(input)

    # Keep track of these values
    max_length: int = 0
    max_start: int = 0
    max_stop: int = 0

    def is_palindrome(start, stop):
        """Define outside of this scope so it can be tested. If we
        were to optimise the callstack, then we would not include a
        pointer to `input` on every call.

        """
        return _is_palindrome_index(input, start, stop)

    for start in range(n):
        for stop in range(start + 1, n + 1):
            if is_palindrome(start, stop):
                length = stop - start
                max_length = max(max_length, length)
                if max_length <= length:
                    max_start = start
                    max_stop = stop

    return input[max_start:max_stop]


def solution_two_pointers(input: str) -> str:
    n = len(input)

    # Keep track of these values
    max_length: int = 0
    max_start: int = 0
    max_stop: int = 0

    def expand_bounds_while_palindrom(l: int, r: int):
        nonlocal max_length, max_start, max_stop

        while 0 <= l and r < n and input[l] == input[r]:
            length = r - l + 1
            max_length = max(max_length, length)
            if max_length <= length:
                max_start = l
                max_stop = r

            l -= 1
            r += 1

    for i in range(n):
        # Case of a palindrom centered on `i`.
        expand_bounds_while_palindrom(l=i, r=i)

        # Case of a palindrom centered between `i` and `i+1`.
        expand_bounds_while_palindrom(l=i, r=i + 1)

    return input[max_start : max_start + max_length]


def solution(input):
    return True


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


def solution_neet_code(s: str) -> str:
    def manacher(s):
        t = "#" + "#".join(s) + "#"
        n = len(t)
        p = [0] * n
        l, r = 0, 0
        for i in range(n):
            p[i] = min(r - i, p[l + (r - i)]) if i < r else 0
            while (
                i + p[i] + 1 < n
                and i - p[i] - 1 >= 0
                and t[i + p[i] + 1] == t[i - p[i] - 1]
            ):
                p[i] += 1
            if i + p[i] > r:
                l, r = i - p[i], i + p[i]
        return p

    p = manacher(s)
    resLen, center_idx = max((v, i) for i, v in enumerate(p))
    resIdx = (center_idx - resLen) // 2
    return s[resIdx : resIdx + resLen]
