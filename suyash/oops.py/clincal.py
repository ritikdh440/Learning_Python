class biodata:
    def __init__(self,name,dob):
        self.name=name
        self.dob=dob
    class clinic:
        def __init__(self,bp,hb,ht,wt):
            self.bp=bp
            self.hb=hb
            self.ht=ht
            self.wt=wt
        def display(self):
            print(self.bp)
            print(self.hb)
            print(self.ht)
            print(self.wt)
a=biodata("suyash","5-5-2002")
e=a.clinic(80,6,6,67)
e.display()