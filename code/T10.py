from linearTable import *
list = linkListNode()
list.from_list([1, 4, 2, 7, 3, 6, 5])

def is_odd(x):
    return x % 2 == 1

true_list, false_list = list.partition(is_odd)

print("True List:")
for item in to_list(true_list):
    print(item, end=" ")  # 输出: 1 7 3 5

print("\nFalse List:")
for item in to_list(false_list):
    print(item, end=" ")  # 输出: 4 2 6