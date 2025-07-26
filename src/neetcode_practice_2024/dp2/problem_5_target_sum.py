#!/usr/bin/env python

import argparse
import argcomplete

from typing import List
import functools


def solution(nums: List[int], target: int) -> int:

    @functools.cache
    def dfs(i, current):

        if len(nums) == i:
            if target == current:
                return 1
            else:
                return 0
        if len(nums) < i:
            return 0

        # Instead of using a list as a memoisation key, let's splice it in the space exploration strategy.
        return dfs(i + 1, current + nums[i]) + dfs(i + 1, current - nums[i])

    return dfs(0, 0)


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
