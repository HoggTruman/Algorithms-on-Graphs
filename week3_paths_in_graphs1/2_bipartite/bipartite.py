#Uses python3

import sys
import queue

def bipartite(adj):
    colour = [0] * n
    queue = []
    rem_v = {i for i in range(n)}

    while rem_v:
        vertex = rem_v.pop()
        queue.append(vertex)
        colour[vertex] = 1
        while queue:
            for v in adj[queue[0]]:
                if colour[v] == colour[queue[0]]:
                    return 0
                if colour[v] == 0:
                    colour[v] = colour[queue[0]]*-1
                    queue.append(v)
                    rem_v.remove(v)
            queue.pop(0)
    return 1


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
    print(bipartite(adj))
