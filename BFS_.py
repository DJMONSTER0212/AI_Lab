from queue import Queue
adj_list = {
    "A":['B','D'],
    'B':['A','C'],
    'C':['B'],
    'D':['A','E','F'],
    'E':['D','F','G'],
    'F':['D','E','H'],
    'G':['E','H'],
    'H':['G','F']
}

# BFS Code
visited = {}
level ={}
parent = {}
bfs_traversal_output =[]
queue = Queue()
for node in adj_list.keys():
    visited[node]= False
    parent[node]= None
    level[node] = 1
    # print(node)

# print(visited)
# print(parent)
# print(level)

S = "A"
visited[S] = True
level[S] = 0
queue.put(S)
# print(visited,level)
while not queue.empty():
    u = queue.get()
    bfs_traversal_output.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v]= u
            level[v]=level[u]+1
            queue.put(v)
            # print(visited)
            # print(parent)
            # print(level)
            

print(bfs_traversal_output)