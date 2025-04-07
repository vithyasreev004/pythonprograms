def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)

filename = "C:\\pythonprogram\\file1.txt.txt"
num_lines = count_lines(filename)
print(f"The number of lines in the file '{filename}' is {num_lines}.")
