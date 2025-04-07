num = int(input("Enter the size of arrays: "))
elements = input(f"Enter the values of Array  separated by commas: ")
a=list(map(int,elements.split(',')))
while(num!=len(a)):
    print("enter correct number of elements:")
    num = int(input("Enter the size of arrays: "))
    elements = input(f"Enter the values of Array  separated by commas: ")
    break
print(a);
count=0;
for i in range(len(a)):
    if(a[i]%2==0):
        count+=1
print(count)
        
    
