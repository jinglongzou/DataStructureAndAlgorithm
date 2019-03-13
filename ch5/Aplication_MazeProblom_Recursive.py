#通过递归算法来实现：
#思想：从起点开始，对每一个点都先标记，然后判断是不是终点，是就结束，
#不是就对其可能的方向，先判断是不是通路，是就递归调用函数

#四个可能的方向
dir = [[0,-1],[0,1],[-1,0],[1,0]]
#搜索过程辅助标记函数
def mark(maze,pos):
     maze[pos[0]][pos[1]] = 2
def passable(maze,pos):
    return maze[pos[0]][pos[1]] == 0
#递归的核心循环
def find_path(maze,pos,end):
    #print(pos,end)
    mark(maze,pos)
    if pos == end:
        print(pos, end = ' ')
        return True
    for i in range(4):
        nextp = [pos[0] + dir[i][0],pos[1] + dir[i][1]]
        if passable(maze,nextp):
            if find_path(maze,nextp,end):
                print(pos,end = ' ')
                return True
#测试
maze = [[1,1,1,1,1,1],
       [1,0,0,1,0,1],
       [1,0,1,0,1,1],
       [1,0,1,1,0,1],
       [1,0,0,0,0,1],
       [1,1,1,1,1,1]]
pos = [1,1]
end = [4,4]
find_path(maze,pos,end)