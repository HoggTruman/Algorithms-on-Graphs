#Uses python3

import sys


def bad_acyclic_test(adj):
    adj = {i:adj[i] for i in range(len(adj))}
    while adj:
        if not [] in adj.values():
            return 1
        for key in adj:
            if not adj[key]:
                del adj[key]
                for rem_key in adj:
                    if key in adj[rem_key]:
                        adj[rem_key].remove(key)
                break

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(bad_acyclic_test(adj))
