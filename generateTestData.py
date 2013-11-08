__author__ = 'max'
import random

file = open('normal-3-1.txt','w')
for i in range(1000):
    file.write(str(int((random.normalvariate(3,1)+1)))+"\n")
file.close()


file = open('normal-6-2.txt','w')
for i in range(1000):
    file.write(str(int((random.normalvariate(6,2)+1)))+"\n")
file.close()


file = open('normal-100-30.txt','w')
for i in range(1000):
    file.write(str(int((random.normalvariate(100,30)+1)))+"\n")
file.close()