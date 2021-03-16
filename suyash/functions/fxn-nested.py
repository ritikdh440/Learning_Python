def display(nam):
    def msg():
        return("Hey")
    return(nam+msg())

a=input("name=")
print(display(a))