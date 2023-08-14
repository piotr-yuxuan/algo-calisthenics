from fastapi import FastAPI

from .api.v1 import backtracking, binaryTrees, bits, datastructures, divideAndConquer, dynamic, graphs, greedy, \
    hashing, heaps, intervals, matrices, randomised, searching, slidingWindow, sorting, strings, trees, tries

routers = [
    backtracking.router,
    binaryTrees.router,
    bits.router,
    datastructures.router,
    divideAndConquer.router,
    dynamic.router,
    graphs.router,
    greedy.router,
    hashing.router,
    heaps.router,
    intervals.router,
    matrices.router,
    randomised.router,
    searching.router,
    slidingWindow.router,
    sorting.router,
    strings.router,
    trees.router,
    tries.router
]

app = FastAPI()
for router in routers:
    app.include_router(router)
