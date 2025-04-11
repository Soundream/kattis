import sys
inputs = sys.stdin.read().split("\n")

# Solution:
# Bellman through all paths becuase the absence of enemies acts like a negative weight
# build a 3-dimension array to store titan, shaman and distance

import heapq
from collections import defaultdict

# have N nodes and M edges
# solving X to Y
N,M,X,Y = map(int, inputs[0].split())

# build adjacency list
adjacency_list = [[] for _ in range(N+1)] # skip 0
for edge in inputs[1:M+1]:
    # u, v, distance, monster type
    u,v,d,s = map(int, edge.split())

    # direction, titan(2), shaman(1), distance
    adjacency_list[u].append((v, int(s==2), int(s==1), d))
    adjacency_list[v].append((u, int(s==2), int(s==1), d))


def BellmanFord(graph, start, end):
    # Initialize distances and predecessor map
    distances = defaultdict(lambda: (float('inf'), float('inf'), float('inf')))  # (titan, shaman, distance)
    distances[start] = (0, 0, 0) 

    predecessors = {start: None}

    for _ in range(N): 
        for node in range(1, N+1):
            for neighbor, t_weight, s_weight, d_weight in graph[node]:
                curr_titan, curr_shaman, curr_distance = distances[node]
                new_titan = curr_titan + t_weight
                new_shaman = curr_shaman + s_weight
                new_distance = curr_distance + d_weight

                if (new_titan, new_shaman, new_distance) < distances[neighbor]:
                    distances[neighbor] = (new_titan, new_shaman, new_distance)
                    predecessors[neighbor] = node

    return distances[end]


result = BellmanFord(adjacency_list, X, Y)
if result[0] == float('inf') and result[1] == float('inf') and result[2] == float('inf'):
    print("IMPOSSIBLE")
else:
    titan, shaman, distance = BellmanFord(adjacency_list, X, Y)
    print(" ".join(map(str, [distance, shaman, titan])))

