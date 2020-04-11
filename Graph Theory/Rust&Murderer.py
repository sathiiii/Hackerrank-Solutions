from collections import defaultdict

def rustMurderer(n, s, roads):
    mainRoads = defaultdict(set)
    for u, v in roads:
        mainRoads[u].add(v)
        mainRoads[v].add(u)

    distance = [1] * n
    notVisited = mainRoads[s]
    visited = set()
    currentDistance = 2
    while notVisited:
        for v in notVisited:
            diff = notVisited | mainRoads[v]
            if len(diff) < n:
                distance[v - 1] = currentDistance
                visited.add(v)
        notVisited -= visited
        visited = set()
        currentDistance += 1
    del distance[s - 1]
    return distance
