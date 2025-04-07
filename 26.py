class Exceptionhandling:
    def __init__(self):
        self.num=num
    
    try:
        num = int(input("Enter the number: "))
        print(f'You entered: {num}')
    except ValueError:
        print("That's not a valid number. Please enter an integer.")

        
        
            
