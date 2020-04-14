from heapq import heappop, heappush

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# To store the minimum path weight of the path from (0, 0) to (i, j).
weight = [[float("inf")] * N for _ in range(N)]
# The number of cells from (i, j) to the lower right cell (N-1, N-1) is used as the heuristic.
heuristic = [[(2 * (N - 1) + 1 - i - j) for j in range(N)] for i in range(N)]
# Since the minimum path to (0, 0) from itself is it's cell value.
weight[0][0] = grid[0][0]
# The keys of the openList is kept in a Min heap data structure.
# Keys are a tuples of the f value of (i, j) cell and a unique integer to keep the keys unique for all f values.
# f(i, j) = weight(i, j) + heuristic(i, j)
keys = [(weight[0][0] + heuristic[0][0], 0)]
# openList contains all the cells that have been processed and the cell that's currently processing.
openList = {(weight[0][0] + heuristic[0][0], 0): (0, 0)}
# If cell (i, j) is still processing, closedList[i][j] = 1,
# If cell (i, j) is finished processing, closedList[i][j] = 2,
# If cell (i, j) isn't processed yet, closedList[i][j] = 0 (Initially).
closedList = [[0] * N for _ in range(N)]

adjacentDirections = [(-1, 0), (0, -1), (1, 0), (0, 1)]

a = 0
while keys:
    key = heappop(keys)
    # The cell indices that has the minimum f value is extracted.
    i, j = openList[key]
    closedList[i][j] = 2
    for dx, dy in adjacentDirections:
        a += 1
        x, y = i + dx, j + dy
        if N > x >= 0 and N > y >= 0 and closedList[x][y] < 2:
            if weight[x][y] > weight[i][j] + grid[x][y]:
                weight[x][y] = weight[i][j] + grid[x][y]
                heappush(keys, (weight[x][y] + heuristic[x][y], a))
                openList[(weight[x][y] + heuristic[x][y], a)] = (x, y)
                closedList[x][y] = 1
print(weight[N - 1][N - 1])
