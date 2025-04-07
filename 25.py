class Details:
    pass  

students = []

for i in range(1, 4):  
    obj = Details()  
    obj.name = input("Enter a student name: ")
    obj.age = int(input("Enter a student age: "))
    students.append(obj)  
    
for i in range(len(students)):
    print(f'Student{i+1}: Name: {students[i].name}, Age: {students[i].age}')

    
    
