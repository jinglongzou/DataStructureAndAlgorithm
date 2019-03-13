#非递归宽度优先遍历
from Queue_SequenseList import squeue
from Gragh_AdjList import GraghAL
def BFS_gragh(gragh,v0):
    vnum = gragh.vertex_num()
    qu = squeue() #创建队列
    visited = [0] * vnum
    visited[v0] = 1
    BFS_seq = [v0]
    qu.enqueue(v0)  #入队第一个元素
    while not qu.is_empty():
        edges = gragh.out_edges(qu.dequeue())
        for v,w in edges:
            if visited[v] == 0:
                BFS_seq.append(v)
                visited[v] = 1
                qu.enqueue(v)  #依次入队‘第一个’元素的所有邻接顶点
    return BFS_seq
'''
#递归宽度优先遍历
def BFS_gragh_recursive(gragh,v0):
    vnum = gragh.vertex_num()
    visited = [0] * vnum
    visited[v0] = 1
    BFS_seq = [v0]
    def BDS_recursive(gragh,v0):
        edges = gragh.out_edges(v0)
        for v,w in edges:
            if visited[v] == 0:
                visited[v] = 1
                BFS_seq.append(v)
            BDS_recursive(gragh,v)
        for v,w in edges:
            BDS_recursive(gragh,v)

    BDS_recursive(gragh, v0)
    return BFS_seq
'''
"""
时间复杂度分析
创建BFS_seq和visited需要时间复杂的O(V)
算法出入队的操作次数等于图中的边数，总开销是O(E)
边表：对邻接矩阵来说，是构建邻接表，因此需要O(V^2)；对邻接表来说，由于初始已经创建了边表，因此只需读取所以的边，总的需要O(E)
所以对邻接矩阵的图来说：遍历的时间复杂度为O(V^2)；对邻接表的图来说，遍历的时间复杂度为：max(O(V),O(E))

空间复杂度分析：
visited、BFS_seq都需要O(V)的空间，队列的深度也不会超过顶点的个数，因此算法的空间复杂度为O(V)
"""

#测试
mat = [[0,1,1,1],
      [1,0,1,0],
      [0,1,0,1],
      [1,0,1,0]]
G = GraghAL(mat)
print(G)
print(G.degree(2))
print(BFS_gragh(G,0))
print(BFS_gragh_recursive(G,0))