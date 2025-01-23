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
                triplet = tuple(
                    sorted(
                        (
                            input[i],
                            input[j],
                            target_sum,
                        )
                    )
                )
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
                results.add(
                    tuple(
                        sorted(
                            (
                                input[i],
                                input[j],
                                target_sum,
                            )
                        )
                    )
                )
    return results


def solution_two_pointers(input_unsorted: List[int]) -> Set[Tuple[int]]:
    input = sorted(input_unsorted)
    n = len(input)
    target_sum = 0
    results = list()

    for i in range(n - 2):
        if 0 < i and input[i - 1] == input[i]:
            continue
        u = input[i]
        l, r = i + 1, n - 1
        while l < r:
            v, w = input[l], input[r]
            current_sum = u + v + w
            if current_sum < target_sum:
                l += 1
            elif target_sum < current_sum:
                r -= 1
            else:
                results.append(tuple(sorted((u, v, w))))
                l += 1
                r -= 1
                # The last clause is to avoid out-of-bound pointer.
                while input[l - 1] == input[l] and l <= n - 2:
                    l += 1

    # As all other implementations return a set, we must return one
    # here to let the tests pass on happy cases. However, a set hides
    # duplicates created by the algorithm. We return an obviously
    # false but not empty result when the result array contains
    # duplicates.
    if len(results) == len(set(results)):
        return set(results)
    else:
        return results


def main(args):
    return solution_two_pointers(args.input)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Neetcode 2024, two pointers, problem 2 three sum."
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
