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