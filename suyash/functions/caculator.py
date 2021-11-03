def calc(x,y):
    q=x+y
    w=x-y
    e=x*y
    r=x/y
    return q,w,e,r




a=int(input("enter your first no:"))
b=int(input("enter your second no:"))
tuppl=calc(a,b)
for i in tuppl:
    print(i)