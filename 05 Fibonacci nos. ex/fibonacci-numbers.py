import sys

def fib(number):
	a,b = 0,1
	for i in range(number):
		yield a 
		a,b = b,a+b

for x in fib(int(sys.argv[1])):
	print(x)
