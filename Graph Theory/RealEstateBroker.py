'''
    Copyright (C) 2020, Sathira Silva.
    
    Problem Statement:    You are a real estate broker in ancient Knossos. You have m unsold houses, and each house j has an area, xj, 
    and a minimum price, yj. You also have n clients, and each client i wants a house with an area greater than ai and a price less 
    than or equal to pi.

    Each client can buy at most one house, and each house can have at most one owner. What is the maximum number of houses you can sell?
'''

from sys import stdin, stdout
from collections import defaultdict

def bfs(graph, matched, distance):
    queue = []
    for client in range(1, len(matched[0])):
        if matched[0][client] == 0:
            distance[client] = 0
            queue.append(client)
        else:
            distance[client] = float("inf")
    distance[0] = float("inf")

    while queue:
        u = queue.pop()
        if distance[u] < distance[0]:
            for v in graph[u]:
                if distance[matched[1][v]] == float("inf"):
                    distance[matched[1][v]] = distance[u] + 1
                    queue.append(matched[1][v])
    return distance[0] != float("inf")

def dfs(graph, u, matched, distance):
    if u != 0:
        for v in graph[u]:
            if distance[matched[1][v]] == distance[u] + 1:
                if dfs(graph, matched[1][v], matched, distance):
                    matched[0][u] = v
                    matched[1][v] = u
                    return True
        distance[u] = float("inf")
        return False
    return True

def realEstateBroker(clients, houses):
    bipartiteGraph = defaultdict(list)
    for i, [a, p] in enumerate(clients, start=1):
        for j, [x, y] in enumerate(houses, start=1):
            if a < x and p >= y:
                bipartiteGraph[i].append(j)
    matched = [[0] * (len(clients) + 1), [0] * (len(houses) + 1)]
    distance = [0] * (len(clients) + 1)
    maxMatches = 0
    while bfs(bipartiteGraph, matched, distance):
        for client in range(1, len(clients) + 1):
            if matched[0][client] == 0 and dfs(bipartiteGraph, client, matched, distance):
                maxMatches += 1
    return maxMatches

if __name__ == '__main__':
    n, m = map(int, stdin.readline().split())
    clients = []
    for _ in range(n):
        clients.append(list(map(int, stdin.readline().rstrip().split())))
    houses = []
    for _ in range(m):
        houses.append(list(map(int, stdin.readline().rstrip().split())))
    result = realEstateBroker(clients, houses)
    stdout.write(str(result) + '\n')
