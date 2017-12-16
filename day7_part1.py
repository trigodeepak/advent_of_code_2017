with open('input.txt') as f:
    lines = f.readlines()
    res = 0
    d = {}
    for s in lines:
        s = s.strip().split()
##        print s
        n = len(s)
        if n>2:
            b = []
            for i in xrange(3,n-1):
                b.append(s[i][:-1])
            b.append(s[n-1])
            d[s[0]] = b
        else:
            d[s[0]] = []

##    for i in d:
##        print i,d[i]

    def dfs(graph, node, visited):
        if node not in visited:
            visited.append(node)
            for n in graph[node]:
                dfs(graph,n, visited)
        return visited

    m = len(lines)
    for i in d:
        visited = dfs(d,i,[])
        if len(visited) == m:
            print i
            break
