class bmw:
    def __init__(self,make,model,yr):
        self.make=make
        self.model=model
        self.yr=yr
class parking:
    def __init__(self,slot,make,model,yr):
        bmw.__init__(self,make,model,yr)
        self.slot=slot
    
    