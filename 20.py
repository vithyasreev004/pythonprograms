	class Pattern:
    def patterns(self):
        num = 1
        for i in range(1, 5):
            print('\n')
            for j in range(1, i+1):
                print(num,end="\t")
                num += 1 

            
obj=Pattern()
obj.patterns()
