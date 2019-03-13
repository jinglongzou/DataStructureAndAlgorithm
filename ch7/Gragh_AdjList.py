# 采用邻接表实现图
"""
 这里通过list中的元素为(v,w)，来作为一个顶点的邻接表，然后一个顶点的list又当做一个元素组成整个图的邻接表
也就是说是通过顺序存储的方式来实现邻接表，也可以通过链表的形式来实现图的邻接表
"""


# 这里没有存储顶点信息，如果需要存储顶点信息就可以添加一个数据域，如list来顺序存储顶点或者链表来存储
from Gragh_AdjMatrix import Gragh,GraghError
from Stack_linear import sstack  #非递归的深度优先遍历的辅助数据结构
from Queue_SequenseList import squeue
infinity = float('inf')
class GraghAL(Gragh):
    def __init__(self, mat=[], unconn= 0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum: #检测是否为方阵
                raise ValueError("Argument for 'Gragh'")
        # 注意：由于是使用可变对象作为参数，所以需要建立新拷贝，这里的内容就是拷贝
        self._mat = [self._out_edges(mat[i], unconn) for i in range(vnum)]
        self._vnum = vnum
        self._unconn = unconn

    def add_vertex(self):
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1  # 返回添加顶点的索引

    def add_edge(self, vi, vj, val):
        if self._vnum == 0:
            raise GraghError("cannot add edge to empty gragh")
        if self._invalid(vi) or self._invalid(vj):
            raise GraghError(str(vi) + ' or ' + str(vj) + ' is not valid vertex')
        row = self._mat[vi]
        i = 0
        while (i < len(row)):
            if row[i][0] == vj:
                self._mat[vi][i] == (vi, val)  # 修改边
                return
            if row[i][0] > vj:
                break  # 原来没有到vj的边，退出循环加入边
            i += 1
        self._mat[vi].insert(i, (vj, val))

    def get_edges(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraghError(str(vi) + ' or ' + str(vj) + ' is not valid vertex')
        if vi == vj:
            return 0
        for i, val in self._mat[vi]:
            if i == vj:
                return val
        return infinity

    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraghError(str(vi) + ' is not valid vertex')
        return self._mat[vi]

    def degree(self,vi):
        if self._invalid(vi):
            raise GraghError(str(vi) + ' is not valid vertex' )
        edges = self.out_edges(vi)
        vi_degree = len(edges)
        return vi_degree

    # 深度优先遍历
    # 由于图中可能存在回路，避免重复访问，需要为每个顶点设置一个标记。
    # 用一个与顶点数相同大小的表来存标记，未访问为0，已访问为1
    # 非递归深度优先遍历
    def DFS_gragh(self, v0):
        gragh = self
        vnum = gragh.vertex_num()
        visited = [0] * vnum
        visited[v0] = 1
        DFS_seq = [v0]
        s = sstack()
        s.push((0, gragh.out_edges(v0)))
        while not s.is_empty():
            i, edges = s.pop()
            if i < len(edges):
                v, e = edges[i]
                s.push((i + 1, edges))
                if not visited[v]:
                    DFS_seq.append(v)
                    visited[v] = 1
                    s.push((0, gragh.out_edges(v)))
        return DFS_seq

    # 递归深度优先遍历
    def DFS_gragh_recursive(self, v0):
        gragh = self
        vnum = gragh.vertex_num()
        DFS_seq = []
        visited = [0] * vnum

        def DFS_recursive(gragh, v0):
            DFS_seq.append(v0)
            visited[v0] = 1
            edges = gragh.out_edges(v0)
            for v, w in edges:
                if visited[v] == 0:
                    DFS_recursive(gragh, v)

        DFS_recursive(gragh, v0)
        return DFS_seq

    # 非递归宽度优先遍历
    def BFS_gragh(self, v0):
        gragh = self
        vnum = gragh.vertex_num()
        qu = squeue()  # 创建队列
        visited = [0] * vnum
        visited[v0] = 1
        BFS_seq = [v0]
        qu.enqueue(v0)  # 入队第一个元素
        while not qu.is_empty():
            edges = gragh.out_edges(qu.dequeue())
            for v, w in edges:
                if visited[v] == 0:
                    BFS_seq.append(v)
                    visited[v] = 1
                    qu.enqueue(v)  # 依次入队‘第一个’元素的所有邻接顶点
        return BFS_seq
"""
#测试
mat = [[0,1,1,1],
      [1,0,1,0],
      [0,1,0,1],
      [1,0,1,0]]
G = GraghAL(mat)
print(G)
print(G.degree(2))
print(G.DFS_gragh_recursive(0))
print(G.BFS_gragh(0))
"""
