def mergesort(seq):
    if len(seq) <= 1:
        return seq
    mid = int(len(seq) / 2)
    left = mergesort(seq[:mid])
    right = mergesort(seq[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
#没看懂底下的result的作用是什么，上面的append方法为什么不是直接将所有的元素都添加到result中呢？
    result = result + left[i:]
    result = result + right[j:]
    return result

seq = [4, 5, 7, 6,2]
print(mergesort(seq))