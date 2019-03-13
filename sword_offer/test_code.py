#
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        n = number
        from math import floor
        if floor(n / 2) < n / 2:
            two = int(floor(n / 2))
            one = 1
        else:
            two = int(n / 2)
            one = 0
        count = 0

        for i in range(two, -1, -1):
            twice = i
            once = one + (two - twice) * 2
            # 总的次数
            sums = twice + once
            # 基于组合求解跳法，在sum次跳中，任选once个位置，来作为跳一阶的位置
            fenmu = 1
            fenzi = 1
            # 求分母：
            j = once
            while (j > 0):
                fenmu = fenmu * j
                j -= 1
            # 求分子
            k = sums
            while (k > (sums - once)):
                fenzi = fenzi * k
                k -= 1
            count = count + int(fenzi / fenmu)
        return count


s = Solution()
n = 4
print(s.jumpFloor(n))