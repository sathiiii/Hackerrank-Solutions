import sys
sys.setrecursionlimit(2000)


def dfs(astronaut, visited):
    global graph
    global count
    visited[astronaut] = True
    count += 1
    for a in graph[astronaut]:
        if not visited[a]:
            visited[a] = True
            dfs(a, visited)


def journeyToMoon(n, astronauts):
    global graph
    global count
    for a1, a2 in astronauts:
        graph[a1].append(a2)
        graph[a2].append(a1)
    
    visited = [False for _ in range(n)]
    countries = []

    for i in range(n):
        if not visited[i]:
            count = 0
            dfs(i, visited)
            countries.append(count)
    
    totalPairs = n * (n - 1) // 2
    sameCountryPairs = 0

    for i in range(len(countries)):
        sameCountryPairs += countries[i] * (countries[i] - 1) // 2

    return totalPairs - sameCountryPairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    np = input().split()

    n = int(np[0])

    p = int(np[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    graph = defaultdict(list)
    for i in range(n):
        graph[i] = []

    count = 0
    
    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
