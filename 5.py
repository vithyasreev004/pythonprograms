#student grade details
total_marks=float(input("Enter your total marks"));
if(total_marks>=90):
    print("GRADE A");
elif(total_marks>80 and total_marks<=89):
    print("GRADE B");
elif(total_marks>70 and total_marks<=79):
    print("GRADE C");
elif(total_marks>60 and total_marks<=69):
    print("GRADE D");
elif(total_marks>50 and total_marks<=59):
    print("GRADE E");
else:
    print("OOPS! YOU FAILED!!");
    
    
