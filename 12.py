n=int(input("ENTER THE SIZE OF AN ARRAY:"))
n1=input("ENTER THE VALUES OF THE ARRAY:")
a=list(map(int,n1.split(',')))
while(len(a)!=n):
    print("please enter correct number of values")
    n1=input("ENTER THE VALUES OF AN ARRAY:")
    a=list(map(int,n1.split(',')))
    break
print("normal array",a)

for i in range(len(a)):
    pos=i
    for j in range(i+1,n):
      if(a[j]>a[pos]):
        pos=j
    temp=a[i] 
    a[i]=a[pos]
    a[pos]=temp
print("sorted array:",a)

