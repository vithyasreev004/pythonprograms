n=int(input("ENTER THE SIZE OF ARRAYS:"))
n1=input("ENTER ARRAY1 VALUES(comma separated values):")
a1=list(map(int,n1.split(',')))
while(len(a1)!=n):
    print("please enter correct number of values")
    n1=input("ENTER ARRAY1 VALUES(comma separated values):")
    a1=list(map(int,n1.split(',')))
    break

n2=input("ENTER ARRAY2 VALUES(comma separated values):")
a2=list(map(int,n2.split(',')))
while(len(a2)!=n):
    print("please enter correct number of values")
    n2=input("ENTER ARRAY2 VALUES(comma separated values):")
    a2=list(map(int,n2.split(',')))
a1,a2=a2,a1
print('array 1:',a1)
print('array 2:',a2)
