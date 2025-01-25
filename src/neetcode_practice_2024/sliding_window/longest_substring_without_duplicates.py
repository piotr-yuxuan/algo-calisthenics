#!/usr/bin/env python

import argparse
import argcomplete


def solution_brute_force(input: str) -> int:
    n = len(input)

    def is_without_duplicate(s: str):
        return len(s) == len(set(s))

    # Keep track of these values:
    max_length = 0

    for left_bound in range(n):
        for right_bound in range(left_bound + 1, n + 1):
            substring = input[left_bound:right_bound]
            if is_without_duplicate(substring):
                max_length = max(max_length, len(substring))

    return max_length


def solution_intuitive(input: str, debug=False) -> int:
    n = len(input)

    if n < 2:
        return n

    # Keep track of these values:
    max_length = 0
    known_positions = dict({})

    left_bound, right_bound = 0, 0
    while right_bound < n:
        head_character = input[right_bound]
        if (
            head_character in known_positions
            and left_bound <= known_positions[head_character]
        ):
            left_bound = known_positions[head_character] + 1

        # This needs to happen regardless of the `left_bound` update.
        known_positions[head_character] = right_bound

        length = right_bound - left_bound + 1
        max_length = max(max_length, length)
        right_bound += 1

    return max_length


def solution(input: str) -> int:
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
