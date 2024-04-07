# 数据结构链表上机实验-python-
数据结构上机报告（链表）

实验目的
掌握链表数据结构的基本概念和操作
熟悉链表的插入、删除、查找、反转等基本操作的实现
了解链表在实际应用中的场景
实验内容
以下实验的所有代码均在linearTable.py中实现，每项实验的测试样例均会import该文件中的对应类，测试该方法的正确性。

1.链表节点头插入、节点插入、节点删除
先定义一个节点类class Node，含有两个参数，data存储节点值，next存储节点下一个指向的目标。
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
再定义一个链表类linkListNode，先将头节点设置为None，即链表初始化为空链表。
class linkListNode:
    def __init__(self):
        self.head = None

然后定义headInsert头插函数，将节点插入，将head节点指向该新插入的节点，时间复杂度为O(1)
def headInsert(self, data):
    new = Node(data)
    new.next = self.head
    self.head = new
定义tailInsert尾插函数，将节点插入到最后一个节点的后面，由于链表只能顺序访问，时间复杂度为O(n)
def tailInsert(self, data):
    new = Node(data)
    if self.head is None:
        self.head = new
    else:
        idx = self.head
        while idx.next:
            idx = idx.next
        idx.next = new
再定义普通的insert插入函数，将节点插入到第k个节点后，平均时间复杂度也为O(n)
def insert(self, data, k):
    new = Node(data)
    idx = self.head
    while idx.next and k > 1:
        k -= 1
        idx = idx.next
    if idx:
        new.next = idx.next
        idx.next = new
要删除链表中第k个节点，定义remove函数，传入参数k
def remove(self, k):
    if k == 1:
        if self.head:
            self.head = self.head.next
    else:
        idx = self.head
        while idx.next and k > 1:
            k -= 1
            idx = idx.next
        if idx and idx.next:
            idx.next = idx.next.next
下面是测试代码，测试了插入、删除、查找功能：
## 导入linearTable.py中的linkListNode和to_list函数
from linearTable import linkListNode, to_list

## 创建一个linkListNode对象
my_list = linkListNode()

## 测试元素插入功能
print("插入元素测试:")
my_list.headInsert(3)
my_list.tailInsert(5)
my_list.insert(4, 2)  # 在第2个位置插入4
my_list.headInsert(2)
my_list.tailInsert(6)
print(to_list(my_list))  # 输出: [2, 3, 4, 5, 6]

## 测试元素删除功能
print("\n删除元素测试:")
my_list.remove(1)  # 删除第1个元素
my_list.remove(3)  # 删除第3个元素
print(to_list(my_list))  # 输出: [3, 5, 6]

## 测试查找功能
print("\n查找元素测试:")
idx = my_list.head
while idx:
    if idx.data == 5:
        print("找到元素5")
    idx = idx.next
输出结果如下：

2.链表反转功能的实现
定义reverse函数，采用迭代的方式来反转链表,而不是递归的方式。具体实现过程如下：
·初始化一个指针 p 为 None。这个指针将用于记录反转后链表的最后一个节点。
·进入 while 循环,循环条件是 self.head 不为空。这个循环将遍历整个链表。
·在循环体内部,首先定义一个指针 q 指向当前链表的头节点 self.head。
·将 self.head 指向下一个节点,即 q.next。这一步是为了在反转链表时不丢失下一个节点的引用。
·将当前节点 q 的 next 指针指向之前反转的链表的最后一个节点,也就是 p。这一步是关键步骤,它实现了节点的反转。
·将 p 指向当前节点 q。这一步是为了在下一次循环时,p 指向正确的反转链表的最后一个节点。
·循环结束后,self.head 指向了原链表的最后一个节点,而 p 指向了反转后链表的第一个节点。
·将 self.head 指向 p,即反转后链表的第一个节点。
def reverse(self):
    p = None
    while self.head:
        q = self.head
        self.head = q.next
        q.next = p
        p = q
    self.head = p
测试代码如下，将链表设为2->4->9->6->10->7：
from linearTable import *
list = linkListNode()
list.from_list([2, 4, 9, 6, 10, 7])
list.reverse()
idx = list.head
while idx:
    print(idx.data, end=' ')
    idx = idx.next
输出结果如下：

3.链表排序功能的实现
定义函数sort，用冒泡排序的方式实现链表排序。
通过两层嵌套循环执行冒泡排序的逻辑。外层循环控制需要排序的趟数,内层循环控制每一趟比较和交换的过程。在内层循环中,使用了三个指针 curr、prev 和 next_node。curr 指向当前待比较的节点,prev 指向其前一个节点,next_node 指向后一个节点。
def sort(self):
    if not self.head or not self.head.next:
        return self.head

    # 获取链表长度
    length = 0
    curr = self.head
    while curr:
        length += 1
        curr = curr.next

    # 执行冒泡排序
    for i in range(length - 1):
        curr = self.head
        prev = None
        for j in range(length - 1 - i):
            next_node = curr.next
            if curr.data > next_node.data:
                # 交换当前节点和下一个节点
                if prev:
                    prev.next = next_node
                else:
                    self.head = next_node
                temp = next_node.next
                next_node.next = curr
                curr.next = temp
            prev = curr
            curr = next_node

    return self.head
测试代码如下:
from linearTable import *
# 创建一个无序链表
unsorted_list = linkListNode()
unsorted_list.from_list([5, 3, 7, 1, 9])

# 对链表进行排序
unsorted_list.sort()

# 将排序后的链表转换为列表
sorted_list = to_list(unsorted_list)
print(sorted_list)  # 输出: [1, 3, 5, 7, 9]
输出结果如下：


4.顺序表和链表的相互构造
在链表类中定义将顺序表转换到链表的方法from_list，传入顺序表ls作为参数，按序遍历并逐个头插，最后将链表反转。 
如果采用尾插法，每次插入都需要O(n),总复杂度为O(n^2)。
如果采用头插法，每次插入需要O(1)时间，反向便利链表需要O(n)时间。这里采用头插法，虽然没有尾插方便，但是相对效率更高。
def from_list(self, ls):
    self.head = None
    for x in ls:
        self.headInsert(x)
    self.reverse()
在整个linearTable文件中定义函数to_list，将链表存入到顺序表中，逐个顺序遍历链表存入：
def to_list(linkLs):
    ls = []
    idx = linkLs.head
    while idx:
        ls.append(idx.data)
        idx = idx.next
    return ls
测试代码如下：
from linearTable import *
ll = linkListNode()
ls0 = list(map(int, input().split()))
ll.from_list(ls0)
print(to_list(ll))
输出结果如下：

5.反向遍历操作链表
定义方法rev_visit，传入参数op，其中op为自定义的函数方法，且该方法不会改变链表本身的顺序结构。
首先定义了三个指针 pre、idx 和 ne。pre 用于记录反转后链表的最后一个节点,idx 用于遍历原链表,ne 用于临时保存下一个节点的引用。
通过一个 while 循环,将原链表进行反转。反转的过程就是将每个节点的 next 指针指向前一个节点。反转后,pre 指向了原链表的最后一个节点。
将反转后的链表头节点赋值给 self.head,然后定义 idx = pre,从尾部开始遍历反转后的链表。在遍历过程中,对每个节点执行自定义操作 op(idx)。
遍历结束后,原链表的 next 指针结构已经被破坏。因此需要将链表再次反转,以恢复原始结构。反转的过程与第 2 步相同,只是这次 pre 最终指向了原链表的头节点。将反转后的链表头节点赋值回 self.head,即完成了原链表结构的恢复。

def rev_visit(self, op):
    pre = None
    idx = self.head
    while idx:
        ne = idx.next
        idx.next = pre
        pre = idx
        idx = ne
    ## 最后pre指向原链表中最后一个元素
    ## 此时原链表中的next结构已经被破坏反转
    ## 将链表尾端元素变为head
    self.head = pre
    idx = pre
    while idx:
        op(idx)
        idx = idx.next
    ## 将破坏的next结构还原
    pre = None
    idx = self.head
    while idx:
        ne = idx.next
        idx.next = pre
        pre = idx
        idx = ne
    ## 将head变回原来的head
    self.head = pre
测试的代码如下，定义函数op，将节点存储的数据加一：
from linearTable import *
def op(idx):
    idx.data += 1
    print(idx.data, end=' ')
list = linkListNode()
list.from_list([2, 5, 7, 1, 3, 7])
## 检测操作结果
list.rev_visit(op)
print()
输出结果如下：

第一行代表每次处理后的data结果，证明了链表确实是在进行反向遍历。第二行按顺序重新输出链表，验证了链表的结构已经还原。
6.两链表元素交替插入
定义函数interLeaving，将链表another交叉合并如self链表中。	定义两个指针 idx1 和 idx2 分别指向两个原始链表的头节点。定义一个布尔变量 flag,用于控制下一个插入节点应该来自哪个链表。初始化为 True,表示先从第一个链表插入。
使用 while 循环遍历两个链表,循环条件是 idx1 和 idx2 均不为空。在循环体内部,先临时保存 idx1 和 idx2 的下一个节点,分别为 ne1 和 ne2。根据 flag 的值,决定从哪个链表插入节点:
如果 flag 为 True,则将 idx2 插入到 idx1 之后,即 idx1.next = idx2。然后 idx1 移动到下一个节点 ne1。
如果 flag 为 False,则将 idx1 插入到 idx2 之后,即 idx2.next = idx1。然后 idx2 移动到下一个节点 ne2。
每次插入操作后,将 flag 取反,即 flag = not flag。这样可以在两个链表之间交替插入节点。
循环结束后,有两种情况:
如果一个链表较长,那么该链表的剩余节点将直接插入到新链表的尾部。如果另一个链表较长,由于交替插入的特性,新链表的尾节点已经指向了该链表中的下一个节点,因此无需额外操作。
def interLeaving(self, another):
    idx1 = self.head
    idx2 = another.head
    ## 控制下一个应该插入哪个链表的元素
    flag = True
    while idx1 and idx2:
        ne1 = idx1.next
        ne2 = idx2.next
        if flag:
            idx1.next = idx2
            idx1 = ne1
        else:
            idx2.next = idx1
            idx2 = ne2
        flag = not flag
    ## 原链表较长的情况，此时idx2指向空，不需要对list1进行改变
    ## 插入链表较长的情况，此时idx1指向空，而原链表的tail元素已经指向了another中对应的下一个元素
    ## 继续执行to_list操作，仍然会在another表中继续遍历至空
测试代码如下：
from linearTable import *
list1 = linkListNode()
list1.from_list([1, 3, 5])

list2 = linkListNode()
list2.from_list([2, 4, 6, 7, 8, 9])

list1.interLeaving(list2)
merged_list = to_list(list1)
print(merged_list)  # 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9]
将list2插入到list1中，其中list2更长，输出结果如下：



7.单链表剖分函数的实现
定义partition函数，传入参数pred表示谓词判断，pred是一个自定义的函数，返回布尔类型值。
创建两个新的链表头节点 true_head 和 false_head，分别用于存放满足谓词条件和不满足条件的节点。同时定义两个指针 idx1 和 idx2 分别指向两个链表的尾部。
定义指针 idx 指向原始链表的头节点,开始遍历。在遍历过程中,先保存当前节点的下一个节点为 ne。遍历结束后,将真链表和假链表的尾节点的 next 指针指向 None。
创建两个新的链表对象 true_list 和 false_list,分别将它们的头节点指向真链表和假链表的头节点。
def partition(self, pred):
    true_head = Node(None)  # 创建真链表的头节点
    idx1 = true_head
    false_head = Node(None)  # 创建假链表的头节点
    idx2 = false_head

    idx = self.head
    while idx:
        ne = idx.next  # 保存下一个节点
        if pred(idx.data):  # 如果当前节点满足谓词条件
            idx1.next = idx  # 将当前节点添加到真链表尾部
            idx1 = idx
        else:  # 如果当前节点不满足谓词条件
            idx2.next = idx  # 将当前节点添加到假链表尾部
            idx2 = idx
        idx = ne  # 移动到下一个节点

    idx1.next = None  # 真链表的尾节点指向None
    idx2.next = None  # 假链表的尾节点指向None

    true_list = linkListNode()
    true_list.head = true_head.next  # 真链表的头节点
    false_list = linkListNode()
    false_list.head = false_head.next  # 假链表的头节点

    return true_list, false_list
测试代码中，定义is_odd函数判断是否为偶数：
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
输出结果如下：

8.排序单链表类的定义
定义一个排序单链表类：
class sortedLinkListNode:
    def __init__(self):
        self.head = None
类似之前的链表类，该排序单链表类继承了其中的headInsert方法、reverse方法、from_list方法便于自定义链表。
为实现链表的有序合并，定义merge函数。
首先创建了一个哑节点(dummy node) dummy,用于辅助合并操作。哑节点的作用是避免在合并过程中需要特殊处理头节点的情况。通过使用哑节点,可以更加简洁地实现链表的合并。
定义了一个指针 curr 初始指向哑节点,它将用于遍历和构建新的有序链表。定义了两个指针 p1 和 p2 分别指向两个待合并链表的头节点。使用 while 循环遍历两个链表,循环条件是 p1 和 p2 至少有一个不为空。
在循环体内部,比较 p1 和 p2 指向节点的值,将较小的节点插入到新链表的尾部,即:
如果 p1 指向的节点值小于或等于 p2 指向的节点值,则将 p1 指向的节点插入到新链表尾部,即 curr.next = p1,然后 p1 移动到下一个节点。否则,将 p2 指向的节点插入到新链表尾部,即 curr.next = p2,然后 p2 移动到下一个节点。无论插入哪个节点,都需要将 curr 移动到新插入的节点,即 curr = curr.next。
循环结束后,可能还有一个链表中剩余未合并的节点。此时,将剩余的部分直接并入新链表的尾部,即:
如果 p1 不为空,则将 p1 剩余的部分并入新链表,即 curr.next = p1。如果 p2 不为空,则将 p2 剩余的部分并入新链表,即 curr.next = p2。
最后,创建一个新的有序链表对象 merged_list,将合并后的链表头节点赋值给它的 head 属性。返回新的有序链表对象 merged_list。

def merge(self, another):
    dummy = Node(0)  # 创建一个哑节点
    curr = dummy

    p1, p2 = self.head, another.head

    while p1 and p2:
        if p1.data <= p2.data:
            curr.next = p1
            p1 = p1.next
        else:
            curr.next = p2
            p2 = p2.next
        curr = curr.next

    # 将剩余未合并的部分直接并入
    if p1:
        curr.next = p1
    elif p2:
        curr.next = p2

    # 创建一个新的sortedLinkListNode对象,并将合并后的链表赋值给它的head属性
    merged_list = sortedLinkListNode()
    merged_list.head = dummy.next
    return merged_list
测试代码如下：
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

输出结果如下：

9.表指针单链表类的定义
重新定义表指针节点ValueIndexNode类：
class ValueIndexNode:
    def __init__(self, data):
        self.data = data
        self.index = None
        self.next = None

该类具有三个参数，index表示该节点所在的表的下标。
定义表指针单链表类ValueIndexList类：
def __init__(self, index):
    self.head = None
    self.index = index
初始化的时候需要传入表的index参数，即表下标。
以下为该类的各个方法：
def headInsert(self, data):
    new = ValueIndexNode(data)
    if self.head is None:
        self.head = new
        new.index = self.index
    else:
        new.next = self.head
        self.head = new
        new.index = self.index

def insert(self, data, k):
    new = Node(data)
    idx = self.head
    while idx.next and k > 1:
        k -= 1
        idx = idx.next
    if idx:
        new.next = idx.next
        idx.next = new
        new.index = self.index

def change(self, k, new_list):
    prev = None
    curr = self.head
    idx = 0
    while curr:
        if idx == k:
            # 从当前链表中删除节点
            if prev is None:
                self.head = curr.next
            else:
                prev.next = curr.next

            # 将节点插入到新链表的头部
            curr.next = new_list.head
            new_list.head = curr
            curr.index = new_list.index

            return

        prev = curr
        curr = curr.next
        idx += 1

def from_list(self, ls):
    self.head = None
    for x in ls:
        self.headInsert(x)
    self.reverse()

def reverse(self):
    p = None
    while self.head:
        q = self.head
        self.head = q.next
        q.next = p
        p = q
    self.head = p

def print_list(self):
    curr = self.head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()
相比之前的单链表类，在插入操作时，都需要加入语句new.index = self.index，初始化节点时节点的index为None，需要在插入时将节点的index赋值为单链表的index值。
在删除节点的时候，也需要将节点的index值重置为None。
新增了一个change函数，将链表中的第k个节点转移头插入新链表中，需要先进行remove操作，然后将节点头插入新链表并将节点的index值赋为新链表的index。
测试代码如下：
from linearTable import *
list1 = ValueIndexList(1)
list1.from_list([1, 2, 3, 4, 5])
list2 = ValueIndexList(2)
list2.from_list([6, 7, 8])
list1.reverse()
list1.print_list()
list1.change(4, list2)
list1.print_list()
list2.print_list()
输出结果如下：
