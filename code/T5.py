from linearTable import *
ll = linkListNode()
ls0 = list(map(int, input().split()))
ll.from_list(ls0)
print(to_list(ll))