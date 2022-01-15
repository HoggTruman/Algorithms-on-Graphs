#Uses python3

import sys

visited = []
found = 0

def reach(adj, x, y):
    global visited
    global found
    visited.append(x)
    if found == 0 and y in visited:
        found = 1
        return found
    for v in adj[x]:
        if found == 0 and not v in visited:
            reach(adj, v, y)

    return found

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
