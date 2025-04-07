array1 = []
array2 = []
adds = []

def getarray():
    global array1, array2
    array1 = []
    array2 = []
    size = int(input("Enter the size of the arrays: "))
    for i in range(1, 3):
        for j in range(size):
            values = input(f"Enter row {j} values: ")
            if i == 1:
                a = list(map(int, values.split(',')))
                array1.append(a)
            else:
                b = list(map(int, values.split(',')))
                array2.append(b)
    print('Array before added')
    print('Array 1:', array1)
    print('Array 2:', array2)

def addarray():
    global adds
    getarray()
    adds = list(map(lambda x, y: [i + j for i, j in zip(x, y)], array1, array2))
    displayarray()

def displayarray():
    print('The addition of two arrays is:', adds)

addarray()
