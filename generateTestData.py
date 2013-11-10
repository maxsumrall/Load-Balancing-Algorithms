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


file = open('pareto-1.txt','w')
for i in range(1000):
    file.write(str(int((random.paretovariate(1))*100))+"\n")
file.close()


file = open('pareto-2.txt','w')
for i in range(1000):
    file.write(str(int((random.paretovariate(2))*100))+"\n")
file.close()



file = open('pareto-3.txt','w')
for i in range(1000):
    file.write(str(int((random.paretovariate(3))*100))+"\n")
file.close()


file = open('pareto-4.txt','w')
for i in range(1000):
    file.write(str(int((random.paretovariate(4))*100))+"\n")
file.close()



file = open('biNormal-100-300--30.txt','w')
for i in range(1000):
    if random.random() > 0.5:
        file.write(str(int((random.normalvariate(100,30))+1))+"\n")
    else:
        file.write(str(int((random.normalvariate(300,30))+1))+"\n")
file.close()


file = open('biNormal-100-300--10.txt','w')
for i in range(1000):
    if random.random() > 0.5:
        file.write(str(int((random.normalvariate(100,10))+1))+"\n")
    else:
        file.write(str(int((random.normalvariate(300,10))+1))+"\n")
file.close()
