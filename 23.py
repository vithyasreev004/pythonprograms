class Arrays:
    def __init__(self):
        self.array = []

    def getarray(self):
        self.size = int(input('Enter the size of the array: '))
        for i in range(self.size):
            val = input(f'Enter the values for row {i}, separated by commas: ')
            row = list(map(int, val.split(',')))
            while len(row) != self.size:
                print('Enter the correct number of values !!')
                val = input(f'Enter the values for row {i}, separated by commas: ')
                row = list(map(int, val.split(',')))
            self.array.append(row)

    def displayarray(self):
        print('The array is:')
        for row in self.array:
            print('\t'.join(map(str, row)))

def main():
    arr = Arrays()
    arr.getarray()
    arr.displayarray()

main()
