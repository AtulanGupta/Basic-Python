# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 01:38:32 2022

@author: Atulan
"""

# Creating a new file
f= open("G:\\study\\code basic\\funny.txt","w")
f.write("I love python.")
f.write("\nI am learning it.")
f.close()
f= open("G:\\study\\code basic\\funny.txt","a")
f.write(" I need to spend more times.")
f.close()
f= open("G:\\study\\code basic\\funny.txt","r")
print(f.read())
f.close()
f= open("G:\\study\\code basic\\funny.txt","r")
for line in f:
    print(line)
    
f.close() 
f= open("G:\\study\\code basic\\funny.txt","r")
f_out=open("G:\\study\\code basic\\funny_wc.txt","w")

for line in f:
    tokens= line.split(' ')
    f_out.write("\n"+line+"wordcount:"+str(len(tokens)))
    #print(str(tokens))
    #print(len(tokens))
f.close() 
f_out.close()
'''
f= open("G:\\study\\code basic\\funny.txt","r+") # r+- allows both reading and writing.
f_out=open("G:\\study\\code basic\\funny_wc.txt","w+") # w+- allows both reading and writing. also if the file
                                                         doesn't exist then it will create new one and if exists
                                                         then it will overwrite it.
                                                         
for line in f:
    tokens= line.split(' ')
    f_out.write("\n"+line+"wordcount:"+str(len(tokens)))
    #print(str(tokens))
    #print(len(tokens))
f.close() 
f_out.close()

'''
with open("C:\\.txt","r") as f:
    print(f.read())
print(f.closed)



























