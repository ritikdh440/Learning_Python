class counter:
    obc=0
    def __init__(self):
        counter.obc+=1
    @staticmethod
    def display():
        print(counter.obc)
a=counter()
b=counter()
c=counter()
counter.display()