#!/usr/bin/env python

import argparse
import argcomplete

from typing import List, Set, Tuple
import collections


def solution_three_loops(input: List[int]) -> Set[Tuple[int]]:
    n = len(input)
    results = set({})
    target_sum = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if target_sum == input[i] + input[j] + input[k]:
                    triplet = tuple(sorted((input[i], input[j], input[k])))
                    results.add(triplet)
    return results


def solution_two_loops(input: List[int]) -> Set[Tuple[int]]:
    n = len(input)
    values = collections.defaultdict(set)
    for i, k in enumerate(input):
        values[k].add(i)
    results = set({})
    for i in range(n - 1):
        for j in range(i + 1, n):
            target_sum = -(input[i] + input[j])
            if target_sum in values:
                min_count = 0
                if i in values[target_sum]:
                    min_count += 1
                if j in values[target_sum]:
                    min_count += 1
                if len(values[target_sum]) <= min_count:
                    continue
                triplet = tuple(sorted((input[i], input[j], target_sum)))
                results.add(triplet)
    return results


def solution_two_loops_sorted(input_unsorted: List[int]) -> Set[Tuple[int]]:
    input = sorted(input_unsorted)
    n = len(input)
    values = collections.defaultdict(set)
    max_value = max(input)
    for i, k in enumerate(input):
        values[k].add(i)
    results = set({})
    for i in range(n - 1):
        for j in range(i + 1, n):
            target_sum = -(input[i] + input[j])
            # Not even the highest value would satisfy the condition,
            # so exiting the inner loop and continuing the outer loop.
            if max_value + target_sum < 0:
                break
            if target_sum in values:
                min_count = 0
                if i in values[target_sum]:
                    min_count += 1
                if j in values[target_sum]:
                    min_count += 1
                if len(values[target_sum]) <= min_count:
                    continue
                triplet = tuple(sorted((input[i], input[j], target_sum)))
                results.add(triplet)
    return results


def main(args):
    return solution_three_loops(args.input)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Neetcode 2024, XXX, problem XXX.")
    parser.add_argument(
        "--input",
        "-i",
        type=str,
        required=True,
        help="XXX",
    )

    # https://kislyuk.github.io/argcomplete/#installation
    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    print(main(args))
    exit(0)
