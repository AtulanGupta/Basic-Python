# tuple is a collection which is organised but unchangeable(immutable). tuple is expressed using ().
# main difference between tuple and list is- lists are homogeneous , tuples are heterogeneous.

import sys
tuple=(2,3,4,5,6,7,8)
print(tuple)
#tuple[0]=10#this creates error msg as tuple does not support item assignment.
print(tuple)
list=[2,3,4,5,6,7,8]
print(list)
print('tuple',sys.getsizeof(tuple))# it is clear that list require greater memory than tuple
print('list',sys.getsizeof(list))
#tuple.remove(tuple[5])#this generates a error msg.
del tuple
print(tuple)