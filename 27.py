arr=[]
size=int(input('Enter a range of values to find cube and sqr'))
for i in range(size):
    arr.append(i)
for i in range(len(arr)):
    square = list(map(lambda x: x**2, arr))
    cube = list(map(lambda x: x**3, arr))
print(f'Squares: {square}')
print(f'Cubes: {cube}')
    


