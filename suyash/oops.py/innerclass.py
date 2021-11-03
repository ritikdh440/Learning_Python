class car:
    def __init__(self,name,year):
        self.name=name
        self.year=year
    class engine:
        def __init__(self,no):
            self.no=no
        def display(self):
            print("engine started")
c=car("bmw",2017)
e=c.engine(56656)
e.display()
            