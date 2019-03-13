#################################################
#实现两个内容：
#   1、将二叉树输出为元组的嵌套形式：#输出：(1(2^(5^^))(3^^))
#   2、将字符串形式的二叉树的元组嵌套结构，读取并建立二叉树：#读取:'(1(2^(5^^))(3^^))'

#二叉树链节点
class BinTNode:
    def __init__(self,data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
#二叉树类
class BTree:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
# 二叉树易读形式的输出二叉树函数
def print_BinTNode(t):
    if t is None:
        print('^',end = '')
        return
    print('(' + str(t.data), end = '')
    print_BinTNode(t.left)
    print_BinTNode(t.right)
    print(')',end = '')


#############################################
#现在要定义一个函数来读入这种形式的二叉树
#输入：一个字符串exp
#输出：一个二叉树
#因此需要一个字符串拆分函数，能够进行迭代字符，一个二叉树生成的递归函数
#实现思路：
#   字符迭代器
#   采用递归的读取这种字符
#   由于需要将左右子树赋给根节点，因此根节点需要通过栈存起来
###########################################

def token(exp):
    delimiter = '()^'
    i,exp_len = 0,len(exp)
    while(i < exp_len):
        while i < exp_len and exp[i].isspace():
            i +=1
        if i >= exp_len:
            break
        #读取'()^'
        if exp[i] in delimiter:
            yield exp[i]
            i +=1
            continue
        #读取数据
        j = i + 1
        while (j < exp_len and exp[j] not in delimiter):
            if ((exp[j]=='e' or exp[j] == 'E') and j + 1 < exp_len and exp[j + 1] == '-'):
                j +=1
            j +=1
        yield exp[i:j]
        i = j
from Stack_linear import  sstack
def build_BinTree(exp,tree):
    s = sstack()
    exp_elem = token(exp)
    for x in exp_elem:
        if x == '(':
            data = next(exp_elem)
            #print(data)
            node = BinTNode(data)
            if tree.is_empty():
                tree.head = node
                s.push([node, 0])  # 第二个元素是标记node节点的左子树是否被赋值
            else:
                if s.top()[0].left is None and s.top()[1] == 0 :
                    s.top()[0].left = node
                    s.top()[1] = 1
                    s.push([node,0])   #要先链接到它的根节点，才能入栈
                else:
                    s.top()[0].right = node
                    s.push([node,0])   #要先链接到它的根节点，才能入栈
        if x == '^':
            if s.top()[0].left is None and s.top()[1] == 0:
                s.top()[0].left = None
                s.top()[1] = 1
            else:
                s.top()[0].right = None
        if x == ")":
            s.pop()
    while(not s.is_empty()):
        raise Exception('miss ")"!')
    return tree

# 测试
#节点创建
t = BinTNode(1,BinTNode(2,BinTNode(5)),BinTNode(3))
#输出
print_BinTNode(t)  #输出：(1(2^(5^^))(3^^))
print('\n')
#读取
tree = BTree()
exp = '(1(2^(5^^))(3^^))'

tree = build_BinTree(exp,tree)
print_BinTNode(tree.head)

