class student:
    major="ece"
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
    def dispaly(self):
        print(self.name)
        print(self.rno)
        
s1=student("kuns",33)
print(s1.major)
s1.dispaly()