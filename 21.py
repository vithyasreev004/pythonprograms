def main():
    n = int(input("Enter the array limit: "))
    array = []
    print("Enter the values of the array:")
    for i in range(n):
        value = int(input())
        array.append(value)
    result_array = []
    for i in range(n - 1):
        result_array.append(array[i] * array[i + 1])
    print("Output:")
    print(result_array)
main()
