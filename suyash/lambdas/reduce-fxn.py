from functools import reduce
l=[5,6,734,2]
f=reduce(lambda x,y:x+y,l)
print(f)