class Incometax:
    def __init__(self):
        self.ai=float(input("ENTER YOUR ANNUAL INCOME:"))
        self.tax=0
    def calc(self):
        if(self.ai<=250000):
            print("you have no income tax!!")
        elif(self.ai>=250000 and self.ai<=500000):
            self.tax=self.ai*(5/100)
            print("Your tax amount is:",self.tax)
        elif(self.ai>=500000 and self.ai<=1000000):
            self.tax=self.ai*(20/100)
            print("Your tax amount is:",self.tax)
        elif(self.ai>=1000000 and self.ai<=5000000):
            self.tax=self.ai*(30/100)
            print("Your tax amount is:",self.tax)
            
obj=Incometax()
obj.calc()
    
