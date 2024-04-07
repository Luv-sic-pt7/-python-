from linearTable import *
list = linkListNode()
list.from_list([2, 4, 9, 6, 10, 7])
list.reverse()
idx = list.head
while idx:
    print(idx.data, end=' ')
    idx = idx.next