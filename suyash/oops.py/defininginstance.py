class suyash:
    def __init__(self,name,h):
        self.name=name
        self.h=h
    def avg(self):
        n=len(self.h)
        r=sum(self.h)/n
        print(r)
    def display(self):
        print(self.name)
        print(self.h)
a=suyash("suyash barwal",[1,2,3,4,5])
a.avg()
a.display()
