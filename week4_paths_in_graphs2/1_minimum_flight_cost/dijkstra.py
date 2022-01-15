#Uses python3

import sys
import queue
import math as ma


def distance(adj, s, t):
    dist, prev = [ma.inf]*n, [None]*n
    dist[s] = 0
    rem_vertices = {i: dist[i] for i in range(n)}
    while rem_vertices:
        u = min(rem_vertices, key=rem_vertices.get)
        rem_vertices.pop(u)
        for v, w in adj[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
                rem_vertices[v] = dist[v]

    if dist[t] == ma.inf:
        return -1
    else:
        return dist[t]

def distance_fast(adj, s, t):
    dist, prev = [ma.inf]*n, [None]*n
    dist[s] = 0
    rem_vertices = {s: 0}
    while rem_vertices:
        u = min(rem_vertices, key=rem_vertices.get)
        rem_vertices.pop(u)
        for v, w in adj[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
                rem_vertices[v] = dist[v]

    if dist[t] == ma.inf:
        return -1
    else:
        return dist[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append((b - 1,w))
        #cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    #print(adj)
    print(distance_fast(adj, s, t))
