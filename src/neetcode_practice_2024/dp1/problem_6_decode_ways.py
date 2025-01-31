#!/usr/bin/env python

import argparse
import argcomplete

from typing import Callable, List, Optional, Protocol, TypeVar
import collections
import functools


def solution_top_down(input: str) -> int:
    n = len(input)

    valid_one = {str(i) for i in range(1, 10)}
    valid_two = {str(i) for i in range(10, 27)}

    def dfs(i) -> int:
        if n <= i:
            return 1

        code_one = dfs(i + 1) if input[i : i + 1] in valid_one else 0
        code_two = dfs(i + 2) if input[i : i + 2] in valid_two else 0
        return code_one + code_two

    return dfs(0)




def main(args):
    return solution_top_down(args.input)


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


def solution_from_neet_code(input: str) -> int:
    dp = dp2 = 0
    dp1 = 1
    for i in range(len(input) - 1, -1, -1):
        if input[i] == "0":
            dp = 0
        else:
            dp = dp1

        if i + 1 < len(input) and (
            input[i] == "1" or input[i] == "2" and input[i + 1] in "0123456"
        ):
            dp += dp2
        dp, dp1, dp2 = 0, dp, dp1
    return dp1
