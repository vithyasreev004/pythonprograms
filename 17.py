def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "The number should not be divided by zero"
    else:
        return a / b

class Calculator:
    def calc(self):
        print("----MENU------\n1. ADDITION\n2. SUBTRACTION\n3. MULTIPLICATION\n4. DIVISION\n5. EXIT")
        choice = int(input("Enter the choice you want to choose: "))

        if choice == 5:
            print("EXIT")
            return

        n1 = int(input("ENTER THE VALUE 1: "))
        n2 = int(input("ENTER THE VALUE 2: "))

        match choice:
            case 1:
                print("Result:", addition(n1, n2))
            case 2:
                print("Result:", subtraction(n1, n2))
            case 3:
                print("Result:", multiplication(n1, n2))
            case 4:
                print("Result:", division(n1, n2))
            case _:
                print("Invalid choice")

        
obj = Calculator()
obj.calc()
