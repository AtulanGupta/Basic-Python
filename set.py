# although list and tuple allow duplicate values, set does not.
S1= set([1,2,3,4,5,1,2,3])#set does not show duplicate value
print(S1)
S1.add(6)
#S1.add(6,7)# generates a error msg
print(S1)
S1.update([6,7,8])
print(S1)
S2=[10,11,12]
S1.update([9,10],S2)
print(S1)
S1.remove(1)
print(S1)