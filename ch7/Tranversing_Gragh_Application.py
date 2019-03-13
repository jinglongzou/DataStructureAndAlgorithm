###########################################################
# 应用1：
#判断从顶点u到v是否有简单路径
#基本思想：
#通过深度遍历的方法来实现，依次遍历，直到找到v，退出遍历，并输出路径和路径长度
from Gragh_AdjList import GraghAL
#递归深度优先方法，判断是否存在路径的方法
def exist_path_DFS_recursive(gragh,u,v):
    vnum = gragh.vertex_num()
    visited = [0] * vnum
    def existpath(gragh,u,v):
        visited[u] = 1
        flag = False
        if u == v:
            flag = True
            return flag
        edges = gragh.out_edges(u)
        for adj_v, w in edges:  #邻接点
            if visited[adj_v] == 0:
                flag = existpath(gragh, adj_v, v)
                # 必须要有这个判断和break，否则无法返回flag，因为不中止的话，
                # 找到了v,也会继续循环直到没有点还没访问
                if flag == True:
                    break
        return flag
    flag = existpath(gragh,u,v)
    return flag
############################################
#这里遇到一个问题，flag更改了但是没返回出来
############################################
#非递归的深度优先方法判断是否存在路径
from Stack_linear import sstack
def exist_path_DFS(gragh,u,v):
    flag = False #初始化为不存在路径
    vnum = gragh.vertex_num()
    visited = [0] * vnum
    visited[u] = 1
    if u == v:
        flag = True
        return flag
    s = sstack()
    s.push(u)
    while not s.is_empty():
        edges = gragh.out_edges(s.pop())
        for adj_v,w in edges:
            if visited[adj_v] == 0:
                visited[adj_v] = 1
                if adj_v == v:
                    flag = True
                    return flag
                s.push(adj_v)
    return  flag
##################################################################################
#应用2：
#这下面的寻找路径算法是有问题的，因为它无法去除搜索过程中访问过的多余顶点
#找到一条路径
#基本思想是：用一个列表来存储路径。利用深度优先遍历的方法，逐个访问顶点，当找到路径时就结束，输出路径
from Gragh_AdjList import GraghAL
#递归深度优先方法，判断是否存在路径的方法
def find_a_path_DFS_recursive(gragh,u,v):
    vnum = gragh.vertex_num()
    visited = [0] * vnum
    # path 存储路径
    path = []
    def findapath(gragh,u,v,path):
        visited[u] = 1
        path.append(u)
        flag = False
        if u == v:
            flag = True
            return flag
        edges = gragh.out_edges(u)
        for adj_v, w in edges:  #邻接点
            if visited[adj_v] == 0:
                flag = findapath(gragh, adj_v, v,path)
                # 必须要有这个判断和break，否则无法返回flag，因为不中止的话，
                # 找到了v,也会继续循环直到没有点还没访问
                if flag == True:
                    break
        return flag
    flag = findapath(gragh,u,v,path)
    if flag == True:
        return path
    else:
        return  None
############################################
#这里遇到一个问题，flag更改了但是没返回出来
############################################
#非递归的深度优先方法判断是否存在路径
from Stack_linear import sstack
def find_a_path_DFS(gragh,u,v):
    flag = False #初始化为不存在路径
    vnum = gragh.vertex_num()
    visited = [0] * vnum
    visited[u] = 1
    path = []
    s = sstack()
    s.push(u)
    if u == v:
        while not s.is_empty():
            path.append(s.pop())
        return path

    while not s.is_empty():
        edges = gragh.out_edges(s.pop())
        for adj_v,w in edges:
            if visited[adj_v] == 0:
                visited[adj_v] = 1
                s.push(adj_v)
                if adj_v == v:
                    while not s.is_empty():
                        path.append(s.pop())
                    return path
    return  path





#测试
'''
mat = [[0,1,1,1],
      [1,0,1,0],
      [0,1,0,1],
      [1,0,1,0]]
'''
mat = [[0,1,0,0],
      [1,0,1,1],
      [0,1,0,0],
      [0,1,0,0]]

G = GraghAL(mat)
#print(G)
#print(G.degree(2))
#print(G.DFS_gragh_recursive(0))
#print(G.BFS_gragh(0))
print(exist_path_DFS_recursive(G,0,3))
#print(exist_path_DFS(G,0,2))
#print(find_a_path_DFS_recursive(G,0,3))
#print(find_a_path_DFS(G,0,3))