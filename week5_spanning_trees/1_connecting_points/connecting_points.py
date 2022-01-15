#Uses python3
import sys
import math as m


def dist_calc(p1, p2):
    return m.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def mst(points):
    result = 0.
    u = points[0]
    dist = {p: m.inf for p in points[1:]}
    while dist:
        for p in dist:
            x = dist_calc(u, p)
            if x < dist[p]:
                dist[p] = x
        u = min(dist, key=dist.get)
        result += dist.pop(u)
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    points = []
    for i in range(n):
        points.append((data[2*i], data[2*i+1]))
    print("{0:.9f}".format(mst(points)))
