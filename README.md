# Algorithms and data structures

I intend to use this repository as a practice playground
([kata](https://en.wikipedia.org/wiki/Kata_(programming))) as well as
a reminder of some common, simple, yet powerful algorithms. Where
elegant I will use Clojure transducers, which are great power tools to
process sequences. While this document might seem exhaustive, I intend
to use it as a list to which I can come back any time when I need to
study. I haven't implemented everything listed here.

# Study list

## Sorting algorithms

- Implement from scratch: Bubble Sort, Merge Sort, Quick Sort, Heap
  Sort.
- Given an array of integers, find the kth smallest element using
  Quick Select algorithm.
- Implement the Counting Sort algorithm to sort an array of integers
  with a known range of values.
- Solve the "Three-Way Partition" problem using Quick Sort to
  efficiently sort an array with duplicate values.

## Searching algorithms

- Implement from scratch: Binary Search (for a sorted array), Linear
  Search.
- Given a rotated sorted array, find the target element using modified
  Binary Search.

## Graph, tree, and algorithms of traversal thereof

- Implement from scratch: Breadth-First Search (BFS), Depth-First
  Search (DFS), Dijkstra's algorithm, Bellman-Ford algorithm.
- Implement different representations: adjacency matrix, adjacency
  list.
- Find the shortest path between two nodes in a weighted graph using
  Dijkstra's algorithm.
- Implement a binary search tree and perform basic operations like
  insertion, deletion, and search.
- Given a directed graph, check if there is a route between two nodes.
- Find the number of connected components in an undirected graph.
- Implement Topological Sorting for a Directed Acyclic Graph (DAG).
- Find the lowest common ancestor (LCA) of two nodes in a binary tree.
- Given a binary tree, check if it is a valid binary search tree
  (BST).
- Given a graph, find all the strongly connected components (SCCs)
  using Kosaraju's algorithm or Tarjan's algorithm.
- Implement the Floyd-Warshall algorithm to find the all-pairs
  shortest paths in a weighted graph.
- Given an n-ary tree, perform a level-order traversal or a
  depth-first traversal (e.g., pre-order, post-order).

## Dynamic programming

- Understanding the concept of breaking a problem into smaller
  overlapping subproblems and using memoization or tabulation.
- Solve the classic "Fibonacci" problem using both recursive and
  dynamic programming approaches.
- Given a set of items with weights and values, find the maximum value
  that can be obtained with a given maximum weight using 0-1 Knapsack
  problem.

## Greedy algorithms

- Understanding problems where making locally optimal choices leads to
  a globally optimal solution.
- Implement a solution for the "Activity Selection Problem" where you
  need to select the maximum number of activities that don't overlap.
- Given a set of coins with different denominations and an amount,
  find the minimum number of coins needed to make that amount using
  Greedy approach.

## Backtracking algorithms

- Solve the "N-Queens" problem to place N queens on an N×N chessboard
  without attacking each other.
- Implement a Sudoku solver to solve a partially filled Sudoku puzzle.

## String manipulation algorithms

- String matching
- String reversal
- Palindrome checks
- Given two strings, check if one is a permutation of the other.
- Implement the "Rabin-Karp" algorithm to find a pattern in a given
  text.

## Bit manipulation algorithms

- Bitwise operations, finding the single unique element in an array.
- Given an array where all numbers occur twice except for one number,
  find the single unique number.
- Implement a function to count the number of bits that are set to 1
  in an integer.

## Divide and conquer algorithms

- Binary search, Finding the maximum subarray sum.
- Implement the Karatsuba algorithm for fast multiplication of large
  integers.
- Find the closest pair of points among a set of points in 2D space
  using the Divide and Conquer approach.

## Randomized algorithms

- Shuffle an array randomly in-place.
- Implement the "Randomized Select" algorithm to find the kth smallest
  element in an array.

## Sliding Window Technique

- Given an array of integers, find the maximum sum of any contiguous
  subarray of size k.
- Find the longest substring with at most k distinct characters in a
  given string.

## Interval Problems

- Given a list of intervals, merge overlapping intervals.
- Find the minimum number of meeting rooms required to schedule a list
  of intervals.

## Tries

- Implement a trie data structure for efficient string search and
  retrieval.
- Given a list of words, find the longest common prefix using a trie.
- Implement an autocomplete feature using a trie for a given set of
  words.
- Given a list of words, find all word pairs such that the
  concatenation forms a palindrome.

## Hashing

- Implementing hash functions, collision resolution techniques, and
  use cases.
- Implement a hash table with collision resolution (e.g., chaining or
  open addressing).
- Find the first non-repeated character in a string using a hash map.
- Implement the Rabin-Karp algorithm for string matching with multiple
  patterns.
- Find the longest substring without repeating characters using a hash
  map for character frequency.

## Heaps

- Implementing min-heaps and max-heaps and their applications (e.g.,
  priority queues).
- Implement a min-heap or max-heap from scratch.
- Given an array of elements, find the kth largest element using a
  heap-based approach.

## Matrix Manipulation

- Given an m×n matrix, rotate it by 90 degrees in-place.
- Given a matrix of 0s and 1s, find the largest square of 1s (maximum
  size square sub-matrix) and return its area.

## Red-Black Trees or AVL Trees

- Implement insertion and deletion operations for a Red-Black Tree or
  an AVL Tree.
- Perform rotations to balance an unbalanced binary search tree.

## Data Structure implementations

- Arrays and Lists: Implementing arrays, linked lists, and their
  operations.
- Stacks and Queues: Implementing stack and queue data structures and
  their applications.
- Hash maps: Implementing hash maps and understanding their time
  complexity.

# Tools

Algorithms and data structures are exposed by a simple RESTful API for more
realistic setting and for more robust test:

- **Performance**

    - _API load_:
      [Gatling](https://github.com/gatling/gatling),
      [JMeter](https://jmeter.apache.org/),
      [Locust](https://github.com/locustio/locust);

    - _Micro benchmark_:
      [JMH](https://openjdk.java.net/projects/code-tools/jmh/),
      [criterium](https://github.com/hugoduncan/criterium);

    - _Resource_:
      [`htop`](https://hisham.hm/htop/),
      [`top`](https://man7.org/linux/man-pages/man1/top.1.html),
      [`vmstat`](https://linux.die.net/man/8/vmstat);

- **Behaviour**

    - _Tests_:
      [unittest](https://docs.python.org/3/library/unittest.html),
      [mockito](https://github.com/mockito/mockito),
	  generative or property-based testing,
	  standard testing library and practices;

    - _Memory leak_:
      [objgraph](https://mg.pov.lt/objgraph/);

    - _Static analysis_:
      [SonarQube](https://www.sonarqube.org/);

    - _Profiling_: frame graphs,
      [cProfile](https://docs.python.org/3/library/profile.html),
      [VisualVM](https://visualvm.github.io/),
      [Spring Boot Actuator](https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html),
      [jstack](https://docs.oracle.com/en/java/javase/11/tools/jstack.html);

- **Code style**

    - _Mutation testing_:
      [lein-mutant](https://github.com/circleci/lein-mutant),
      [Pitest](https://pitest.org/),
      [Cosmic Ray](https://github.com/sixty-north/cosmic-ray);

    - _Code coverage_:
      [cloverage](https://github.com/cloverage/cloverage),
      [coverage.py](https://github.com/nedbat/coveragepy),
      [JaCoCo](https://www.jacoco.org/jacoco/);

    - _Code metrics_:
      [Radon](https://github.com/rubik/radon),
      [Checkstyle](https://checkstyle.sourceforge.io/),
      [jQAssistant](https://jqassistant.org/);

- **Observability**:
  [Prometheus](https://prometheus.io/),
  [Grafana](https://grafana.com/);

_(tools listed here may be specific to some languages)_

# Writing style

Code here isn't shaped in the style I would use for professional coding. Every
team has some culture and opinions about code style and it's better to stick to
these common guidelines. Moreover code is written primarily to be read by other
people, or all of us would code in assembly for maximum performance if we were
to target only a machine readership. Code I write as part of a team is intended
to may have been written by anybody else in this team.

Code here is written in litterate programming thanks to Emacs and org-mode. It
means the code written in Clojure is derived from the text files explining the
reasoning behind it. I hope it makes it easier to read.
