#Uses python3

import sys

sys.setrecursionlimit(200000)
visited = []
v_dict = {}
clock = 0

def explore(G,x):
    global visited
    visited.append(x)
    for v in G[x]:
        if v not in visited:
            explore(G, v)


def explore_dfs(G, x):
    global v_dict
    global clock
    v_dict[x] = clock
    clock += 1
    for v in G[x]:
        if v not in v_dict:
            explore_dfs(G, v)
    v_dict[x] = clock
    clock += 1


def dfs(G):
    global v_dict
    for v in range(len(G)):
        if not v in v_dict:
            explore_dfs(G, v)


def number_of_strongly_connected_components(adj):
    global visited
    result = 0
    dfs(adjR)
    order_form = [(key, v_dict[key]) for key in v_dict]
    order_form.sort(reverse=True, key=lambda x: x[1])
    for v in order_form:
        if not v[0] in visited:
            result += 1
            explore(adj, v[0])
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    adjR = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adjR[b - 1].append(a - 1)
    print(number_of_strongly_connected_components(adj))
