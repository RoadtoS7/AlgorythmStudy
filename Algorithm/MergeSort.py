import collections
import sys

v = collections.deque([int(input()) for i in range(int(input()))])

def merge(left, right):
    v = collections.deque()
    i = 0;
    j = 0
    while (i < len(left) and j < len(right)):
        if left[i] <= right[j]:
            v.append(left[i])
            i += 1
        else:
            v.append(right[j])
            j += 1
    if i == len(left): v = v + right[j:len(right)]
    if j == len(right): v = v + left[i:len(left)]
    return v


def merge_sort(v):
    if len(v) <= 1: return v
    m = len(v) // 2
    left = merge_sort(v[0:m])
    right = merge_sort(v[m:len(v)])
    return merge(left, right)


m = merge_sort(v)
print(*m, sep="\n")


