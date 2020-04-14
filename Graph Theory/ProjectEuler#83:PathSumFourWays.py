from heapq import heappop, heappush

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

m = min(min(row) for row in grid)
weight = [[float("inf")] for _ in range(N)]
heuristic = [[m * (2 * (N - 1) + 1 + i - j) for j in range(N)] for i in range(N)]
weight[0][0] = grid[0][0]
openList = [(weight[0][0] + heuristic[0][0], 0, 0)]
closedList = [[0] * N for _ in range(N)]

adjacentDirections = [(-1, 0), (0, -1), (1, 0), (0, 1)]

while openList:
    potential, i, j = heappop(openList)
    closedList[i, j] = 2
    for dx, dy in adjacentDirections:
        
