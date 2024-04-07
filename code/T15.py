from linearTable import *
list1 = sortedLinkListNode()
list1.from_list([1, 3, 5])

list2 = sortedLinkListNode()
list2.from_list([2, 4, 6, 9])

merged_list = list1.merge(list2)

curr = merged_list.head
while curr:
    print(curr.data, end=' ')  # 输出: 1 2 3 4 5 6 9
    curr = curr.next