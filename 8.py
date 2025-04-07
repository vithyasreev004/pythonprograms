n=int(input("Enter the number you want to sum up:"));
count=0;
for i in range(1,n):
    if(i%2!=0):
        count+=i;

print("The sum of odd numbers is :",count);
