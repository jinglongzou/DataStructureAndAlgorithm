# 邻接矩阵实现图
"""
    通过嵌套的二维list来表示邻接矩阵
    一个图的组成元素：顶点、邻接矩阵表示的边、顶点数、无关联的特殊值表示，还可以添加其他需要的数据域
    同样边还可以通过其他形式表示，比如链表可以大大减小空间的使用
    然后,基于图的抽象数据类型实现图类
"""

class GraghError(Exception):
    pass
class Gragh:
    def __init__(self,mat,unconn = 0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum: #检测是否为方阵
                raise ValueError("Argument for 'Gragh'")
        self._mat = [mat[i][:] for i in range(vnum)] #做拷贝
        self._unconn = unconn
        self._vnum = vnum
    def vertex_num(self):
        return self._vnum
    def _invalid(self,v):
        return 0 > v or v >= self._vnum
    def add_vertex(self,v):
        raise GraghError('Adj-Matrix is not support "add vertex". ')
    def add_edge(self,vi,vj,val = 1):
        if self._invalid(vi) or self._invalid(vj):
            raise GraghError(str(vi) + ' or ' + str(vj) +' is not valid vertex' )
        self._mat[vi][vj] = val
    def get_edges(self,vi,vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraghError(str(vi) + ' or ' + str(vj) +' is not valid vertex' )
        return self._mat[vi][vj]
    #出边
    def out_edges(self,vi):
        if self._invalid(vi):
            raise GraghError(str(vi)+' is not valid vertex' )
        return self._out_edges(self._mat[vi],self._unconn)
    def degree(self,vi):
        if self._invalid(vi):
            raise GraghError(str(vi) + ' is not valid vertex' )
        vi_degree = 0
        for i in range(self._vnum):
            if self._mat[vi][i] != self._unconn:
                vi_degree +=1
        return vi_degree
    @staticmethod
    def _out_edges(row,unconn):
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i,row[i]))
        return edges
    #定义一个转换为字符串的形式。
    def __str__(self):
        return "[\n" + ",\n".join(map(str,self._mat)) + "\n]" + "\nunconnexted: " + str(self._unconn)
'''
#测试
mat = [[0,1,1,1],
      [1,0,1,0],
      [0,1,0,1],
      [1,0,1,0]]
G = Gragh(mat)
print(G)
G.degree(2)
'''


