class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkListNode:
    def __init__(self):
        self.head = None
    ##定义头插法
    def headInsert(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    ##定义尾插法
    def tailInsert(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            idx = self.head
            while idx.next:
                idx = idx.next
            idx.next = new

    ## 在第k个节点后插入data
    def insert(self, data, k):
        new = Node(data)
        idx = self.head
        while idx.next and k > 1:
            k -= 1
            idx = idx.next
        if idx:
            new.next = idx.next
            idx.next = new

    ##定义删除节点方法,删除第k个节点
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

    ## 定义链表反转方法
    def reverse(self):
        p = None
        while self.head:
            q = self.head
            self.head = q.next
            q.next = p
            p = q
        self.head = p

    ## 定义链表排序方法(从小到大),采用冒泡方法排序
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

    ## 定义反向遍历方法
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

    ## 输入顺序表ls，得到链表
    ## 如果采用尾插法，每次插入都需要O(n),总复杂度为O(n^2)
    ## 如果采用头插法，每次插入需要O(1)时间，反向便利链表需要O(n)时间
    ## 这里采用头插法，虽然没有尾插方便，但是相对效率更高
    def from_list(self, ls):
        self.head = None
        for x in ls:
            self.headInsert(x)
        self.reverse()

    ## 定义交错插入链表合并方法
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

    ## 定义单链表剖分函数
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

## 定义排序单链表类
class sortedLinkListNode:
    def __init__(self):
        self.head = None

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

    def from_list(self, ls):
        self.head = None
        for x in ls:
            self.headInsert(x)
        self.reverse()

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def headInsert(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

## 将链表转化到列表中
def to_list(linkLs):
    ls = []
    idx = linkLs.head
    while idx:
        ls.append(idx.data)
        idx = idx.next
    return ls


## 新定义一个链表类，节点有三个参数，存储的数data，下一个数的下标next，所在的表下标index
class ValueIndexNode:
    def __init__(self, data):
        self.data = data
        self.index = None
        self.next = None

class ValueIndexList:
    def __init__(self, index):
        self.head = None
        self.index = index

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
