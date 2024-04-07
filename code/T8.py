from linearTable import *
list1 = linkListNode()
list1.from_list([1, 3, 5])

list2 = linkListNode()
list2.from_list([2, 4, 6, 7, 8, 9])

list1.interLeaving(list2)
merged_list = to_list(list1)
print(merged_list)  # 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9]