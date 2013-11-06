import random

__author__ = 'Nina'


def getPareto(num,alpha=1.1):
	ret=[]
	for i in range(0,num):
		ret=ret+[int(random.paretovariate(alpha))]

	return ret

def getGauss(num,mu=0,sigma=1):
	ret=[]
	for i in range(0,num):
		ret=ret+[int(random.gauss(mu,sigma))]

	return ret

#print(getPareto(40))
#print(getGauss(40,5))