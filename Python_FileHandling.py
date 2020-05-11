# -*- coding: utf-8 -*-
"""
Created on Sat May  9 21:34:08 2020

@author: sanjay Pani
"""


fh = open("Hello.txt", "w")
print(fh)

fh.write("This is lien number 1\n")
fh.write("This is lien number 2\n")
fh.write("This is lien number 3\n")

fh.close()

fh = open("Hello.txt", "a")
fh.write("This is line numner 4")

fh = open("Hello.txt", "r")
#print(fh.read())

#Iterate over the file lines
for line in fh:
    print(line)


#with statement file will be closed automatically
    
with open("Hello.txt") as fh:
    for line in fh:
        print(line)
        

with open("Sample.txt", "r") as el:
    for line in el:
        if line != "\n":
            val = int(line[-2])
            if val % 2 == 0:
                print(line)
            


# print(fh.tell())
# print(fh.read(1))
#print(fh.tell())
#print(fh.readline())
#address = fh.readlines()

#print(address[1])

# fh.seek(-6,2)
# print(fh.read(4))