###########################################################################################################
#由图生产树需要考虑的问题：
#1、如何遍历图
#2、如何存储树节点的关系，由于图中顶点的邻接顶点数目不定，因此树的子结点索引的数目难以确定；
#   又因为每个节点,在树中只有一个前驱节点，因此采用父节点索引的方式存储树的节点，这样每个
#   树中每个顶点只需存储一个前驱节点的索引
###########################################################################################################
#导入类
from Gragh_AdjList import GraghAL
from Stack_linear import sstack #非递归的深度优先遍历生成树使用
from Queue_SequenseList import squeue #非递归的宽度度优先遍历生成树使用
###########################################################################################################
#基于深度优先遍历的生成树
##递归的深度优先遍历生成树
#基本思路：
#   1、通过一个列表来存储树，其元素是(preV,w)，也就是前驱(父节点索引)和权，
#   每个顶点都有唯一的前驱，除了根节点的前驱为它本身外.
#   2、在深度优先遍历过程中，对每个顶点赋予前驱。
#   3、根据前一顶点的关系可以追溯出所有的路径
def DFS_span_forest_recursive(gragh):
    vnum = gragh.vertex_num()
    span_forest = [None] * vnum
    def dfs(gragh,v):
        nonlocal span_forest
        for u,w in gragh.out_edges(v):
            if span_forest[u] is None:
                span_forest[u] = (v,w)  #关键这一步，将u顶点的前驱和该前驱到u的权入栈
                dfs(gragh,u)
    for v in range(vnum): #保证非联通图，构造出森林
        if span_forest[v] == None:
            span_forest[v] = (v,0) #根节点入栈
            dfs(gragh,v)
    return span_forest
##非递归的深度优先遍历生成树
#首先将根节点入栈
def DFS_span_forest(gragh):
    vnum = gragh.vertex_num()
    span_forest = [None] * vnum
    s = sstack()
    for v in range(vnum):
        if span_forest[v] == None:
            span_forest[v] = (v,0)
            s.push((0,v,gragh.out_edges(v)))
            while not s.is_empty():
                i,v,edges = s.pop()
                if i < len(edges):
                    u,w = edges[i]
                    s.push((i+1,v,edges))
                    if span_forest[u] == None:
                        span_forest[u] = (v,w)
                        s.push((0,u,gragh.out_edges(u)))

    return span_forest



#########################################################################################################
#基于宽度优先遍历的生成树
##非递归的宽度优先遍历生成树
#基本思路：
#   1、通过一个列表来存储树，其元素是(preV,w)，也就是前驱(父节点索引)和权，
#   每个顶点都有唯一的前驱，除了根节点的前驱为它本身外.
#   2、在跨度优先遍历过程中，对每个顶点赋予前驱。
#   3、根据前一顶点的关系可以追溯出所有的路径
def BFS_span_forest(gragh):
    vnum = gragh.vertex_num()
    span_forest = [None] * vnum
    qu = squeue()
    for v in range(vnum):
        if span_forest[v] == None:
            span_forest[v] = (v,0)
            qu.enqueue(v)
            while not qu.is_empty():
                v = qu.dequeue()
                edges = gragh.out_edges(v)
                for u,w in edges:
                    if span_forest[u] == None:
                        span_forest[u] = (v,w)
                        qu.enqueue(u)

    return span_forest








########################################################################################################
#测试
#测试
mat = [[0,1,1,1],
      [1,0,1,0],
      [0,1,0,1],
      [1,0,1,0]]
G = GraghAL(mat)
print(G)
print(DFS_span_forest(G))
print(DFS_span_forest_recursive(G))
print(BFS_span_forest(G))
