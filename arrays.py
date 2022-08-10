from array import *
salary=array('i',[3990,12223,23344,2345])
print(salary)
print(salary[0])
for i in range(4):
    print(salary[i])
print(salary.buffer_info())#1st number is array address, 2nd number is array length.
print(salary.append(40000))
print(salary)
print(salary.remove(2345))
print(salary)
print(salary.reverse())
print(salary)
#salary1= array('I',[1112,222222,-333333,4444])
#print(salary1)
#the upper code will generate a error msg as I cannot print negetive value.
#salary2= array('i',[1112,222222,-0.5,4444])
#print(salary1)
#the upper code will generate a error msg as i cannot print float value
salary3= array('f',[1112,222222,-0.5,4444])
print(salary3)#using f we can print both float and negetive values

