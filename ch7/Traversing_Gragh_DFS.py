# 深度优先遍历
# 由于图中可能存在回路，避免重复访问，需要为每个顶点设置一个标记。
# 用一个与顶点数相同大小的表来存标记，未访问为0，已访问为1
# 非递归深度优先遍历
from Stack_linear import  sstack
from Gragh_AdjList import  GraghAL
def DFS_gragh(gragh, v0):
    vnum = gragh.vertex_num()
    visited = [0] * vnum
    visited[v0] = 1
    DFS_seq = [v0]
    s = sstack()
    s.push((0,gragh.out_edges(v0)))
    while not s.is_empty():
        i, edges = s.pop()
        if i < len(edges):
            v, e = edges[i]
            s.push((i+1,edges))
            if not visited[v]:
                DFS_seq.append(v)
                visited[v] = 1
                s.push((0,gragh.out_edges(v)))
    return  DFS_seq


# 递归深度优先遍历
def DFS_gragh_recursive(gragh,v0):
    vnum = gragh.vertex_num()
    DFS_seq = []
    visited = [0] * vnum
    def DFS_recursive(gragh,v0):
        DFS_seq.append(v0)
        visited[v0] = 1
        edges = gragh.out_edges(v0)
        for v,w in edges:
            if visited[v] == 0:
                DFS_recursive(gragh,v)

    DFS_recursive(gragh,v0)
    return DFS_seq



#测试
mat = [[0,1,1,1],
      [1,0,1,0],
      [0,1,0,1],
      [1,0,1,0]]
G = GraghAL(mat)
#print(G)
#print(DFS_gragh_recursive(G,0))
print(DFS_gragh(G,0))
