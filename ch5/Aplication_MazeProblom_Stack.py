####################################################
#迷宫解法——基于栈的回溯法
####################################################
#四个可能的方向
dir = [[0,-1],[0,1],[-1,0],[1,0]]
#搜索过程辅助标记函数
def mark(maze,pos):
     maze[pos[0]][pos[1]] = 2
def passable(maze,pos):
    return maze[pos[0]][pos[1]] == 0
#回溯法核心算法
def find_path(maze,pos,End):
    #检查是否是出口
    if pos == End:
        print(pos,end = ' ')
        return
    mark(maze,pos)
    st = lstack()
    st.push((pos,0))
    while not st.is_empty():
        pos,nex = st.pop()
        #print(pos)
        for i in range(nex,4):  #判断是否存在未探索的方向，是，则找出所有方向并入栈，否就进入外循环的下一个循环
            nextp = [pos[0] + dir[i][0],pos[1] + dir[i][1]]
            #print(nextp)
            if nextp == End:
                print_path(nextp,pos,st)
                return
            if passable(maze,nextp):
                st.push((pos,i+1))
                mark(maze,nextp)
                st.push((nextp,0))
                break
    print('no path!')
def print_path(nextp,pos,st):
    print(nextp,pos,end = ' ')
    while st:
        pos,nex = st.pop()
        print(pos,end = ' ')
'''
#测试
maze = [[1,1,1,1,1,1],
       [1,0,0,1,0,1],
       [1,0,1,0,1,1],
       [1,0,1,1,0,1],
       [1,0,0,0,0,1],
       [1,1,1,1,1,1]]
pos = [1,1]
end = [4,4]
try:
    find_path(maze,pos,end)   
except stackUnderflow as e:
    print('\nFind over!')
'''