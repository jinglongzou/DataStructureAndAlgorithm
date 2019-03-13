'''
路径长度和顶点距离:在网路或者带权有向图中
   从顶点到v到v'的一条路径上各条边的长度之和称为该路径的长度
   而其中长度最短的一条路径就是最短路径，最短路径的长度称为从v到v'的距离，记为dis(v,v')

最短路径问题：
    单源点最短路径：从一个顶点v0到其他所有顶点的最短路径
    Dijkstra算法
    个人理解：类似于prim算法，将顶点集分为两个集合，一个是属于最短路径的顶点的集合U，一个不属于最短路径的集合V-U；
              在寻找最短路径的过程中，逐步扩充最短路径的顶点集合。扩充的方法：每次从V-U中选择到顶点v0的距离最短的点
              到最短路径的顶点集合中。而新加入的点，可能改变原来最短路径集合中的其它点到顶点v0的最短路径，要注意维护。
    而实现的思路：
                为了便于比较其它点到顶点v0的最短距离，因此需要一个列表记录其它每个点到顶点v0的距离(这个表随着寻找最短路径
                的过程是变化的），需要一个记录其它每个点到顶点v0的最短路径的前驱(即其它点v到v0的最短路径上，v的前一个顶点u)
                二者可以用一个列表整合在一起来作为搜索路径过程中的辅助列表的元素
                通过优先队列来选择V-U中下一个到顶点v0距离最短的顶点，因为优先队列会用新加入点的邻边和原来队列中的边一起排序，
                从而保证加入集合U的顶点是V-U中到v0路径最短的点。

    多源点最短路径：所有顶点之间的最短路径

'''
from Gragh_AdjList import GraghAL
from PriorityQueue_heaps import PrioQueue
#单源点最短路径问题
def dijkstra_shortest_paths(gragh,v0):
    vnum = gragh.vertex_num()
    assert v0>=0 and v0<vnum
    paths = [None] * vnum
    counts = 0
    qu = PrioQueue([(0,v0,v0)])
    while counts < vnum and not qu.is_empty():
        plen,u,vmin = qu.dequeue()  #每次弹出的是到v0路径长度最短的顶点，弹出了就一定会修改paths路径
        if paths[vmin]:
            continue
        paths[vmin] = (plen,u)
        for v,w in gragh.out_edges(vmin):
            if not paths[v]:  #如果v点不在集合U中，就更新由v0经vmin到v的路径长度，并入队
                qu.enqueue((plen+w,vmin,v)) #关键这是维护最短路径的重要过程
        counts +=1
    return paths
#复杂度分析：
#时间复杂度：
#           创建paths需要O(V),创建优先队列需要O(V)
#           主循环中出入队最多边的条数E,每次出入队操作需要O(logE)，因此主循环的时间复杂度为O(ElongE)
#空间复杂度：
#           paths需要存V个元素，队列存储的元素最多边的条数E,因此空间复杂度为max(O(E),O(V))
########################################################################################################################
#改进的Dijkstra算法
#采用减权堆来实现，类比于优化的prim算法
#    优化的prim算法中使用了起始点到所有顶点的权来初始化一个序列，并转化为减权堆来筛选最短边
#    同样的对于优化的dijkstra算大，也需要一个初始化话序列，只不过权值变成累积的了
from DecPrioHeap_For_Prim import DecPrioHeap
def Optimized_Dijkstra_Shortest_paths(gragh,v0):
    vnum = gragh.vertex_num()
    wv_seq = [[gragh.get_edges(0, v), 0, v] for v in range(vnum)]  # 初始化起点到所有顶点的权
    connects = DecPrioHeap(wv_seq)  # 将初始化的序列构造为减权堆，类似于优先队列，其与有优先队列的主要区别就是修改元素值
    # 每次弹出一条连接两个集合的最短边
    paths = [None] * vnum
    while not connects.is_empty():
        plen, vi, vj = connects.dequeue()
        if  paths[vj]:
            continue
        paths[vj] = (plen,vi)
        for v, w in gragh.out_edges(vj):
            if not paths[v] and plen+ w < connects.weight(v):
                connects.dec_weight(plen + w, vj, v)
    return paths
#多源点最短路径
#       各顶点到自身的距离为0，其余元素为权值，无边的情况下为无穷
#基本思想：
#       如果有边(v,v')属于E,那么它就是顶点v到v'的路径，长度为其权值。
#       但是边(v,v')未必是从v到v'的最短路径，有可能经过其它点到v'可能更短
#        算法采用一种系统化的思想，检查和比较冲v到v'的可能经过的任何顶点的所有路径，从中找出最短路径
inf = float('inf')
def Floyd(gragh):
    vnum = gragh.vertex_num()
    a = [[gragh.get_edges(i,j) for i in range(vnum)] for j in range(vnum)] #create a copy
    nvertex = [[-1 if a[i][i] == inf else j for j in range(vnum)] for i in range(vnum)]
    for k in range(vnum):
        for i in range(vnum):
            for j in range(vnum):
                if a[i][j] > a[i][k] + a[k][j]:
                    a[i][j] = a[i][k] + a[k][j]
                    nvertex[i][j] = nvertex[i][k]
    return (a,nvertex)

#测试
mat = [[0,1,4,5,0,0,0],
      [1,0,1,0,2,0,0],
      [4,1,0,1,0,2,0],
      [5,0,1,0,0,0,2],
      [0,2,0,0,0,2,0],
      [0,0,0,0,2,0,2],
      [0,0,0,2,0,2,0]]
G = GraghAL(mat)
#print(G)
#print(dijkstra_shortest_paths(G,0))
print(Optimized_Dijkstra_Shortest_paths(G,0))
print(Floyd(G))
