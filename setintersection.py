s1={1,2,3}
s2={2,3,4}
s3={3,4,5}
s4=s1.intersection(s2)
print(s1,s2,s3,s4)
s5=s1.intersection(s2,s3)
print(s1,s2,s3,s4,s5)
s6=s1.difference(s2)
print(s6)
s7=s1.difference(s3)
print(s7)
result=s1.union(s2,s3)
print(result)
print(s1|s2|s3)#also executes union operation

