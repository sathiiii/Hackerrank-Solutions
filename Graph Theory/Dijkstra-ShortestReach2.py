from collections import defaultdict
from heapq import heappop, heappush

def shortestReach(n, edges, s):
    # Build the undirected graph using the set of edges
    graph = defaultdict(list)
    for (u, v), w in edges.items():
        graph[u].append((w, v))
        graph[v].append((w, u))
    
    visited = [False for _ in range(n + 1)] # Keeps track of already visited nodes in the BFS traversal
    distance = [float("inf") for _ in range(n + 1)] # d[x] = distance from vertex s to x. (initially all the distances will be assigned to infinity)
    distance[s] = 0 # Distance from s to s is 0 (Base case)
    minHeap = [(distance[s], s)]    # Push vertex s with distance[s] as it's priority into the priority queue
    
    # Iterate while the priority queue isn't empty
    while minHeap:
        d, u = heappop(minHeap) # Extract the vertex with the minimum distance to the source vertex s
        if visited[u]:  # If the extracted vertex is already visited, it has attained it's minimum distance value. Therefore, continue to the next vertex
            continue
        visited[u] = True   # Otherwise, mark the vertex as visited
        # Iterate through all neighbour vertices of u
        for w, v in graph[u]:
            if not visited[v] and distance[v] > d + w:  # Relax v
                distance[v] = d + w
                heappush(minHeap, (distance[v], v)) # Push v to the priority queue with it's updated distance value as the priority value
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
            # If {u, v} is a duplicate edge, add the edge having the lightest weight to the set of edges
            if (u, v) in edges:
                edges[(u, v)] = min(edges[(u, v)], w)
            elif (v, u) in edges:
                edges[(v, u)] = min(edges[(v, u)], w)
            else:
                edges[(u, v)] = w

        s = int(input())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
