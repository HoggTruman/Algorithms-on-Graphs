#Uses python3
import sys
import math as m

#GOAL IS TO MAXIMISE THE MINIMUM DISTANCE BETWEEN TWO POINTS IN DIFFERENT SETS

def dist_calc(p1, p2):
    return m.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def clustering(points, k):
    num_sets = n
    set_dict = {i:i for i in range(len(points))}
    used_points = set()

    edges = []
    for i in range(n):
        for j in range(i+1, n):
            edges.append((i, j, dist_calc(points[i], points[j])))
    edges.sort(key=lambda x: x[2])

    for x, y, d in edges:
        if num_sets > k:
            if set_dict[x] != set_dict[y]:
                for key in set_dict:
                    if set_dict[key] == set_dict[x] and key != x:
                        set_dict[key] = set_dict[y]
                set_dict[x] = set_dict[y]
                num_sets -= 1
                used_points.add(x)
                used_points.add(y)
        else:
            break


    for x,y,d in edges:
        if set_dict[x] != set_dict[y]:
            return d
    return d


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    k = data[-1]
    data = data[1:]
    points = []
    for i in range(n):
        points.append((data[2*i], data[2*i+1]))

    print("{0:.9f}".format(clustering(points, k)))
