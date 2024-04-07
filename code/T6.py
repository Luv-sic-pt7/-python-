from linearTable import *
def op(idx):
    idx.data += 1
    print(idx.data, end=' ')
list = linkListNode()
list.from_list([2, 5, 7, 1, 3, 7])
## 检测操作结果
list.rev_visit(op)
print()
## 验证没有破坏链表原结构
idx = list.head
while idx:
    print(idx.data, end=' ')
    idx = idx.next