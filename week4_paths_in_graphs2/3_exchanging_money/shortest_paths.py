#Uses python3

import sys
import queue
import math as m

def bellman_ford(adj,s):
    global dist
    dist[s] = 0

    for iter in range(n-1):
        for i in range(n):
            for v, w in adj[i]:
                if dist[v] > dist[i] + w:
                    dist[v] = dist[i] + w

    for i in range(n):
        for v, w in adj[i]:
            if dist[v] > dist[i] + w:
                if dist[v] != -m.inf:
                    dfs(adj, v)

    for i in dist:
        if i == m.inf:
            print("*")
        elif i == -m.inf:
            print("-")
        else:
            print(i)


def dfs(adj, s):
    global dist
    queue = [s]
    while queue:
        dist[queue[0]] = -m.inf
        for v, w in adj[queue.pop(0)]:
            if dist[v] != -m.inf:
                queue.append(v)





if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, M = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * M):3], data[1:(3 * M):3]), data[2:(3 * M):3]))
    data = data[3 * M:]
    adj = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append((b - 1, w))
    s = data[0]
    s -= 1

    dist = [m.inf] * n

    bellman_ford(adj,s)


