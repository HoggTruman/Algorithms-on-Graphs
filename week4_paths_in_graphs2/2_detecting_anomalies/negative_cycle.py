#Uses python3

import sys
import math as m


def bellman_ford(adj):
    global unvisited
    adj.append([(i, 0) for i in range(n)])
    dist = [m.inf] * (n+1)
    dist[n] = 0

    for iter in range(n):
        for i in range(n+1):
            for v, w in adj[i]:
                if dist[v] > dist[i] + w:
                    dist[v] = dist[i] + w

    for i in range(n+1):
        for v, w in adj[i]:
            if dist[v] > dist[i] + w:
                return 1

    return 0



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, M = data[0:2]

    unvisited = {i for i in range(n)}

    data = data[2:]
    edges = list(zip(zip(data[0:(3 * M):3], data[1:(3 * M):3]), data[2:(3 * M):3]))
    data = data[3 * M:]
    adj = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append((b - 1, w))

    print(bellman_ford(adj))

