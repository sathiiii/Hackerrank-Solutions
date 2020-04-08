from collections import defaultdict
from heapq import heappop, heappush

def shortestReach(n, edges, s):
    graph = defaultdict(list)
    for (u, v), w in edges.items():
        graph[u].append((w, v))
        graph[v].append((w, u))
    
    visited = [False for _ in range(n + 1)]
    distance = [float("inf") for _ in range(n + 1)]
    distance[s] = 0
    minHeap = [(distance[s], s)]
    
    while minHeap:
        d, u = heappop(minHeap)
        if visited[u]:
            continue
        visited[u] = True
        for w, v in graph[u]:
            if not visited[v] and distance[v] > d + w:
                distance[v] = d + w
                heappush(minHeap, (distance[v], v))
    del distance[s]
    del distance[0]
    return [-1 if d == float("inf") else d for d in distance]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    
    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = defaultdict(int)

        for _ in range(m):
            u, v, w = map(int, input().rstrip().split())
            if (u, v) in edges:
                edges[(u, v)] = min(edges[(u, v)], w)
            elif (v, u) in edges:
                edges[(v, u)] = min(edges[(v, u)], w)
            else:
                edges[(u, v)] = w

        print(edges)

        s = int(input())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
