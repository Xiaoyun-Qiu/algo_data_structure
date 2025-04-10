def BFS(Adj,s):
    seen = {s}
    Q = [s]
    output = dict()
    for u in Adj.keys():
        output[u] = None
    output[s] = 0
    while Q:
        u = Q.pop(0)
        for v in Adj[u]:
            if v not in seen:
                seen.add(v)
                output[v] = output[u] + 1
                Q.append(v)
    return output

if __name__ == '__main__':
    Adj = dict()
    Adj[1] = [2,4]
    Adj[2] = [5]
    Adj[3] = [6,5]
    Adj[4] = [2]
    Adj[5] = [4]
    Adj[6] = [6]
    print(BFS(Adj,1))