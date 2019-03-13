def heap_sort(elems):
    def siftdown(elems, e, begin, end):
        i, j = begin, begin * 2 + 1
        while (j < end):
            if j + 1 < end and elems[j + 1] < elems[j]:  # 修改最后一个小于符号为大于符号就可变为大顶堆
                j = j + 1
            if e < elems[j]:  # 修改最后一个小于符号为大于符号就可变为大顶堆
                break
            elems[i] = elems[j]
            i, j = j, 2 * j + 1
        elems[i] = e

    end = len(elems)
    for i in range(end // 2, -1, -1):
        siftdown(elems, elems[i], i, end)
    for i in range((end - 1), 0, -1):
        e = elems[i]
        elems[i] = elems[0]
        siftdown(elems, e, 0, i)
    return elems


# 测试
elems = [2, 1, 4, 7, 5, 3]
heap_sort(elems)

