from math import lgamma 
import numpy as n
def psi(x):
	h=0.1e-5
	if str(type(x))=="<type 'numpy.ndarray'>":
		result=n.zeros(x.shape)
		for index,value in n.ndenumerate(x):
			result[index]=(lgamma(value+h/2)-lgamma(value-h/2))/h
		return result
	else:
		return (lgamma(x+h/2)-lgamma(x-h/2))/h
def gammaln(x):
	if str(type(x))=="<type 'numpy.ndarray'>":
		result=n.zeros(x.shape)
		for index,value in n.ndenumerate(x):
			result[index]=lgamma(value)
		return result
	elif str(type(x))=="<type 'numpy.float64'>" or str(type(x))=="<type 'float'>":
		return lgamma(x)



