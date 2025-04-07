def get_matrix(size):
    matrix = []
    print("Enter the values of array:")
    for i in range(size):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def add_matrices(matrix1, matrix2, size):
    result = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def main():
    size = int(input("Enter the size of arrays: "))
    print("Enter the values of array 1:")
    matrix1 = get_matrix(size)
    print("Enter the values of array 2:")
    matrix2 = get_matrix(size)

    result = add_matrices(matrix1, matrix2, size)

    print("Sum of 2 arrays is:")
    print_matrix(result)

if __name__ == "__main__":
    main()
