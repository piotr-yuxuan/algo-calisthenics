#!/usr/bin/env python

import argparse
import argcomplete

from typing import List


def solution_perfect(input: List[int]) -> bool:
    total = sum(input)
    if total & 1:
        return False

    target = total >> 1

    bits = 1  # bitmask: bits[i] == 1 means sum 'i' is possible
    for x in input:
        bits |= bits << x
        if (bits >> target) & 1:
            return True
    return False


def solution_legible(input: List[int]) -> bool:
    target = sum(input) / 2
    if int(target) != target:
        return False

    known_sums = set({})
    for x in input:
        known_sums = known_sums.union({x + y for y in known_sums})
        known_sums.add(x)
        if target in known_sums:
            return True
    return False


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
