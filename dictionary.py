# a dictionary is acollection which is unordered,changeable and in____. in python dictionaries are expressed with {}.
#dictionary have unique key and can contain similar values.
d1={'name':'atulan','surname':'gupta','roll':120,'age':29}
print(d1['age'])
d2={'name':'x',10:10,10.5:10.5, True:True, (2,3):5}
print(d2)
print(d2[2,3])
d3=d2.copy()#copy dictionary
print(d3)
length=len(d2)#show length of dic
print(length)
d2['versity']='CUET'#add a new item to the dictionary
print(d2)
d2.pop('versity') # delete item from dic
print(d2)
d2.clear()
print(d2)
#del d2#delete the whole dictionary
# print(d2)
d4={1:'study mart',2:'Data Science',3:'python'}
print(d4[1])
print(d4.get(2))
print(d4.items())
print(d4.keys())
