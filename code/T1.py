# 导入linearTable.py中的linkListNode和to_list函数
from linearTable import linkListNode, to_list

# 创建一个linkListNode对象
my_list = linkListNode()

# 测试元素插入功能
print("插入元素测试:")
my_list.headInsert(3)
my_list.tailInsert(5)
my_list.insert(4, 2)  # 在第2个位置插入4
my_list.headInsert(2)
my_list.tailInsert(6)
print(to_list(my_list))  # 输出: [2, 3, 4, 5, 6]

# 测试元素删除功能
print("\n删除元素测试:")
my_list.remove(1)  # 删除第1个元素
my_list.remove(3)  # 删除第3个元素
print(to_list(my_list))  # 输出: [3, 5, 6]

# 测试查找功能
print("\n查找元素测试:")
idx = my_list.head
while idx:
    if idx.data == 5:
        print("找到元素5")
    idx = idx.next