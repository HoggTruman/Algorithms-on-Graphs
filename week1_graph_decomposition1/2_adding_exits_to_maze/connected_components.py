#Uses python3

import sys

visited = []

def explore(adj,x):
    global visited
    visited.append(x)
    for v in adj[x]:
        if v not in visited:
            explore(adj, v)

def number_of_components(adj):
    global visited
    cc = 0
    for v in range(len(adj)):
        if not v in visited:
            cc += 1
            explore(adj, v)
    return cc

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
    print(number_of_components(adj))
