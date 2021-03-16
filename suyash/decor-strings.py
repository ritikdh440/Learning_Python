def decor(fun):
    def inner(n):
        s= hello()
        return s
    return inner
    
        
    return inner
@decor
def hello(name):
    return "hello"+name
print(hello("suyash"))