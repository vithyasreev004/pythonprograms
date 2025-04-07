def main():
    def getarray():
        a=input("enter a values separated by comma:")
        b=list(a.split(','))
        return b
    def displayarray(x):
        print(x)
        print("values displayed successfully")
    x=getarray()
    displayarray(x)
main()
    
    
    
