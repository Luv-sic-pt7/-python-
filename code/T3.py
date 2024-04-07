from linearTable import *
# 创建一个无序链表
unsorted_list = linkListNode()
unsorted_list.from_list([5, 3, 7, 1, 9])

# 对链表进行排序
unsorted_list.sort()

# 将排序后的链表转换为列表
sorted_list = to_list(unsorted_list)
print(sorted_list)  # 输出: [1, 3, 5, 7, 9]from linearTable import *