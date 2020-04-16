'''
    Copyright (C) 2020, Sathira Silva
    
    Problem Statement:  The kingdom of Zion has cities connected by bidirectional roads. There is a unique path between any pair of 
    cities. Morpheus has found out that the machines are planning to destroy the whole kingdom. If two machines can join forces, they 
    will attack. Neo has to destroy roads connecting cities with machines in order to stop them from joining forces. There must not be 
    any path connecting two machines.
    Each of the roads takes an amount of time to destroy, and only one can be worked on at a time. Given a list of edges and times, 
    determine the minimum time to stop the attack.
    
    Approach:   The idea is to traverse over the edges and partition the kingdom into disjoint subsets of cities which only contain 
                either one or no machine in each partitioned subset. Because, since their is an unique path between any pair of cities 
                any pair of machines can join forces. When we're trying to join a city into an existing disjoint subset of a kingdom, if
                both the city and the subset contain a machine we destroy the edge connecting that city to the subset. Since we need
                to find the minimum time to destroy the roads, we have to sort the edges (or roads) in decending order with respect
                to the time it takes to destroy each road. I've used Union-Find Algorithm for making the disjoint subsets. 
                
                First I mark the cities as 1 (or True) containing a machine using the defaultdictionary dp (default value is 0). Then,
                when each city is added to a disjoint subset, if the disjoint subset already contains a machine I mark the dp values to
                be 1 of those cities.
                
                Time Complexity: O(logn) - Due to the find operation. Union operation only takes O(1). 
'''

from collections import defaultdict

def minTime(roads, machines):
    parent = {} 
    dp = defaultdict(int)

    for machine in machines:
        dp[machine] = 1

    find = lambda node: node if parent.get(node, node) == node else find(parent[node])

    def union(u, v):
        x, y = find(u), find(v)
        if not dp[x] or not dp[y]:
            if u != x :
                x, y = y, x
            parent[x] = y
            dp[x] |= dp[y]
            dp[y] |= dp[x]
            return True

    return sum(time for u, v, time in sorted(roads, key = lambda x: -x[2]) if not union(u, v))
