#return days of the week using switch cases
num=int(input("Enter the day of the week in number:"));
print("The day you have chosen is:");
match num:
    case 1:
        print("Sunday");
    case 2:
        print("Monday");
    case 3:
        print("Tuesday");
    case 4:
        print("Wednesday");
    case 5:
        print("Thursday");
    case 6:
        print("Friday");
    case 7:
        print("saturday");
    case _:
        print("enter correct number");
    
