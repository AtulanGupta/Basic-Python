# list is a collection which is ordered and changeable. List allows duplicate value. we represent list using []
list=[1,['atulan',5,34,60],10,4.5,6,20,22,'atulan']

print(list)
print(list[1])
print(list[1][3])#here [1] indicates nested list, [3] indicates 4th member of the nested list that is 60
#adding 2 list
List=list+[4,5,6,7,10]
print(List)
list.extend([1,5,6,7,8])
print(list)
list.remove(6)#this will remove the element from the list
print(list)
list.remove(list[5])#this will remove 6th element from the list. here 5 is the index number
print(list)
print(list.count('atulan'))
print(list.count(1))

