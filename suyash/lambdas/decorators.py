#returning adding 2 to value of function
def decor(fun):
    def inner():
        a=fun()
        return a+2
    return inner
def num():
    return 5
s=decor(num)
print(s())