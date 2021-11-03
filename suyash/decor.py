def decor(fun):
    def inner():
        a=fun()
        return a+2
    return inner
@decor#now we dont assign our input fxn seperately to decor
def num():
    return 5

print(num())