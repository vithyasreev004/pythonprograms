people = [
    {'name': 'John', 'age': 10},
    {'name': 'Doe', 'age': 20},
    {'name': 'Michael', 'age': 15}
]

sorted_people = sorted(people, key=lambda x: x['age'])

print("Sorted list of dictionaries:")
for person in sorted_people:
    print(person)
