#creating a nested key
student={1:{'name':'atulan', 'age':29,'sex':'male'},2:{'name':'ananya', 'age':20,'sex':'female'}}
#1,2- main key; name,age,sex-nested key
print(student)
print(student[1])
print(student[1]['sex'])
print(student[2]['sex'])
student[3]={}#very important to create an empty dictionary before entering item
student[3]['name']= 'shapla'
student[3]['age'] = 46
student[3]['sex'] ='female'
print(student)
