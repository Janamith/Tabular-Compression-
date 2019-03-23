import collections
def MST(MImatrix):
    def getEdges(MImatrix):
        edges = []
        for i in range(MImatrix.shape[0]):
            for j in range(MImatrix.shape[1]):
                edges.append((i, j, MImatrix[i][j]))
        return edges

    sorted_edges = sorted(getEdges(MImatrix), key=lambda tup: tup[2], reverse = True)
    #print (sorted_edges)
    MST = collections.defaultdict(list)
    num_edges = 0
    for edge in sorted_edges:
        if num_edges == MImatrix.shape[0]-1:
            break
        if (edge[1] in MST.keys() or edge[0] == edge[1]):
            continue
        MST[edge[0]].append((edge[1], edge[2]))
        num_edges += 1

    return MST
