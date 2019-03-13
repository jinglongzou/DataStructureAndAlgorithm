# 背包问题 应用栈来解决
#背包可以装确定的重量weights，现有n件物品，每件的重量是s0,s1,....,s(n-1);可以将问题递归的分为两类问题：每件物品可以放入或者不放入背包；
#当不放入时，问题就变为n-1个物品能否装满背包；当放入时，问题就变为n-1件物品能否构成重量weights - s(n-1)
#最终wei
#输入：
#       背包能装的重量：weights
#       物品件数： n
#       每件商品重量的组成的列表：wlist
#输出：
#       能否装满背包，返回逻辑值

def knap_rec(weights,n,wlist):
    if weights == 0:
        return True
    elif weights < 0 or (weights > 0 and n < 1):
        return False
    elif knap_rec(weights - wlist[n-1],n-1,wlist):
        print('Item ' + str(n) + ': ', wlist[n-1])
        return True
    elif knap_rec(weights,n-1,wlist):
        return True
    else:
        return False
# 测试
weights = 10
n = 5
wlist = [1,2,4,3,5]
rec = knap_rec(weights,n,wlist)