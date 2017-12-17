with open('input.txt') as f:
    lines = f.readlines()
    res = 0
    d = {}
    for s in lines:
        s = s.strip().split()
        n = len(s)
        if n>2:
            b = []
            for i in xrange(2,n-1):
                b.append(s[i][:-1])
            b.append(s[n-1])
            d[s[0]] = b
        else:
            d[s[0]] = []


    def dfs(graph, node, visited):
        if node not in visited:
            visited.append(node)
            for n in graph[node]:
                dfs(graph,n, visited)
        return visited

    count = 0
    list_key = d.keys()
    print len(list_key)
    while(len(list_key)!=0):
        visited = dfs(d,list_key[0],[])
        for j in visited:
            list_key.remove(j)
        count +=1
    print count 
