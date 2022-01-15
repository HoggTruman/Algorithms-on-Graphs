#Uses python3
import sys

v_dict = {}
clock = 0


def explore(adj,x):
    global v_dict
    global clock
    clock += 1
    for v in adj[x]:
        if v not in v_dict:
            explore(adj, v)
    v_dict[x] = clock
    clock += 1


def dfs(adj):
    global v_dict
    for v in range(len(adj)):
        if not v in v_dict:
            explore(adj, v)


def toposort(adj):
    order = []
    for v in reversed(list(v_dict.keys())):
        order.append(v)
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    dfs(adj)
    #print(v_dict)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

