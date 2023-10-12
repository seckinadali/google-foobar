# Reference: https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm

import collections

def bfs(graph, s, t, parent):
    '''
    Performs breadth-first search on residual graph
    to check if there is a path from s (source) to t (sink),
    and stores the path in parent
    '''
    # Mark all vertices as not visited
    visited = [False] * len(graph)

    # Create a queue for breadth-first search
    # for paths in residual graph
    queue = collections.deque([])

    # Start with source node
    queue.append(s)
    visited[s] = True

    # Breadth-first search on paths
    while queue:
        u = queue.popleft()

        # Go through adjacent nodes of u
        for node, capacity in enumerate(graph[u]):
            if visited[node] == False and capacity > 0:
                queue.append(node)
                visited[node] = True
                parent[node] = u
    
    # Return True if t (sink) has been visited, otherwise False
    return visited[t]

def edmonds_karp(graph, s, t):
    '''
    Returns the max flow from s (source) to t (sink) in graph
    using Edmonds-Karp algorithm
    '''
    parent = [-1] * len(graph)
    max_flow = 0

    # Augment the flow while there is a path from s to t
    while bfs(graph, s, t, parent):
        # Find min residual capacity of the edges
        # along the path bfs finds
        path_flow = float('Inf')
        node = t
        while node != s:
            path_flow = min(path_flow, graph[parent[node]][node])
            node = parent[node]
        
        # Add path flow to total flow
        max_flow += path_flow

        # Update residual capacities of the edges,
        # and reverse edges along the path
        node = t
        while node != s:
            graph[parent[node]][node] -= path_flow
            graph[node][parent[node]] += path_flow
            node = parent[node]
    
    return max_flow

def solution(entrances, exits, path):
    '''
    Generalizes the edmonds_karp function above
    to a scenario with several sources and sinks
    
    Returns the max flow from entrances to exits
    '''
    max_flow = 0
    for s in entrances:
        for t in exits:
            max_flow += edmonds_karp(path, s, t)
    
    return max_flow