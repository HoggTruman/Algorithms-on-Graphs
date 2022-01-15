#Uses python3

import sys
import queue

def distance(adj, s, t):
    dist = [-1]*n
    queue = []
    queue.append(s)
    dist[s] = 0
    while queue:
        for v in adj[queue[0]]:
            if dist[v] == -1:
                dist[v] = dist[queue[0]]+1
                queue.append(v)
        queue.pop(0)

    return dist[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(adj)
    print(distance(adj, s, t))
