'''
    Copyright 2020, Sathira Silva.
    
    Problem Statement:    A tree of P nodes is an un-directed connected graph having P - 1 edges. Let us denote R as the root node. If A 
    is a node such that it is at a distance of L from R, and B is a node such that it is at at distance of L + 1 from R and A is 
    connected to B, then we call A as the parent of B.
    Similarly, if A is at a distance of L from R and B is at a distance of L + K from R and there is a path of length K from A to B, 
    then we call A as the Kth parent of B.
    Susan likes to play with graphs and Tree data structure is one of her favorites. She has designed a problem and wants to know if 
    anyone can solve it. Sometimes she adds or removes a leaf node. Your task is to figure out the Kth parent of a node at any instant.
    
    Approach:   This problem is a famous Graph Theory problem and is known as the "Level Ancestor Query problem". (Actually, this's a
                variant of the Level Ancestor Problem) First of all we have to know some definitions about Tree Data Structure. 
                
                What is a Tree? As the problem states, a Tree is an un-directed connected graph. Therefore, if the tree has P nodes,
                it has P - 1 edges. A rooted tree is a tree which has an arbitrary vertex as the root.
                
                Depth of a vertex:  The depth of a vertex u in a tree T is denoted as depth(u) and it's the level in which it's located,
                starting from depth(root) = 0 i.e. depth(u) = #edges on the shortest path from root to u.
                
                Example: Suppose node 1 is the root.
                                                  1             Node |  1  |  2  |  3  |  4  |  5  |  6  |
                                                /   \           Depth|  0  |  1  |  1  |  2  |  2  |  2  |  
                                               2     3
                                              / \    |
                                             5   6   4
                
                Descendant:   A descendant node of a node is any node in the path from that node to the leaf node (including the leaf 
                node). The immediate descendant of a node is the “child” node.
                
                Deepest descendant:   Let v be a descendant of the vertex u in a tree T and Pv the path from u to v (which is unique).
                Then v is the deepest descendant of u if and only if |Pv| >= |Px| for all descendants x of u.
                
                Height of a vertex:    The height of a vertex u in a tree T, denoted as height(u), is the number of levels we have to go 
                through, if we want to travel from u to one of its deepest descendants (which is a leaf). Note that here, the leaves 
                are defined to have height 1. i.e. height(u) = #vertices on the path from u to one of its deepest descendants
                
                Ancestor:   An ancestor node of a node is any node in the path from that node to the root node (including the root node).
                The immediate ancestor of a node is the "parent" node.
                
                
                The Level Ancestor Problem:   Let T = (V, E) be a rooted tree with |V| = n, |E| = n - 1. Pre-process the tree and
                answer the level ancestor queries (find the ancestor v of the query node u at depth K + depth(u) / Kth ancestor 
                / Kth parent).
                
                LA_T(u, K) = v, if v is the unique ancestor of u with depth(v) = depth(u) - K.
                LA_T(u, K) = 0, if such an ancestor doesn’t exist.
                
                NOTE:   LA_T (u, root) = u and LA_T (u, depth(u)) = root ∀u ∈ V.
                
                
                There're three different Algorithms to solve the Level Ancestor Problem:
                        (1). Table Algorithm
                        (2). Jump - Pointer Algorithm
                        (3). Ladder Algorithm
'''
