#由先根遍历和中根遍历生成二叉树
#思路：由先根确定根节点
#      由中根分割成左右子树
#      递归以上两步
################################
#输入：先根和中根的列表表示
#输出：嵌套表形式的二叉树
#首先定义两个辅助函数：构造嵌套函数、数据查找函数
#构造嵌套函数
def make_nested_BinaryTree_list(data,left,right):
    return [data,left,right]
#查找函数
def find_data(order,data):
    for i in range(len(order)):
        if order[i] == data:
            return i
    raise NotMatchError('the preorder is not match midorder!')
#定义一个不匹配错误类：
class NotMatchError(Exception):
    pass
#递归的方法
def preorder_midorder_to_binarytree(preorder,midorder):
    pre_len = len(preorder)
    mid_len = len(midorder)
    if pre_len == 0 and mid_len == 0:
        return None

    elif pre_len >0 and mid_len >0:
        index = find_data(midorder, preorder[0])
        data = preorder[0]
        left = preorder_midorder_to_binarytree(preorder[1:(index+1)],midorder[0:index])
        right = preorder_midorder_to_binarytree(preorder[(1+index):],midorder[(index+1):])
        node = make_nested_BinaryTree_list(data,left,right)
        return node
    else:
        raise NotMatchError('the preorder is not match midorder!')
'''
#非递归的方法
from Stack_linear import sstack
def prepreorder_midorder_to_binarytree_not_recursive(preorder,midorder):
    s = ss

#没想出来
'''
#测试
preorder =[1,2,4,3]
midorder = [4,2,1,3]
node = preorder_midorder_to_binarytree(preorder,midorder)
print(node)
