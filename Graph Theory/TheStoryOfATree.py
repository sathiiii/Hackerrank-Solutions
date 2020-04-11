from collections import defaultdict
from math import gcd


def storyOfATree(n, edges, k, guesses):
    graph = defaultdict(list)
    count = 0
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    root = 1
    visited = [False] * (n + 1)
    visited[root] = True
    queue = [root]
    count = 0
    while queue:
        root = queue.pop()
        for v in graph[root]:
            if not visited[v]:
                visited[v] = True
                count += (root, v) in guesses
                queue.append(v)
    
    root = 1
    visited = [False] * (n + 1)
    visited[root] = True
    queue = [(root, count)]
    win = 0
    while queue:
        root, count = queue.pop()
        win += (count >= k)
        for v in graph[root]:
            if not visited[v]:
                visited[v] = True
                queue.append((v, count - ((root, v) in guesses) + ((v, root) in guesses)))
    g = gcd(win, n)
    return "{}/{}".format(win // g, n // g)
