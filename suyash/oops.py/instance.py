class course:
    def __init__(self,name,ratings):
        self.name=name
        self.ratings=ratings
    def avg(self):
        n=len(self.ratings)
        average=sum(self.ratings)/n
        print("avg=",average)
c=course("python-basics",[4,3,4,5,2,3])
print(c.ratings)
print(c.name)
c.avg()