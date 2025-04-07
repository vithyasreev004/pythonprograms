import re
pattern = r'ab+'

def match_string(strs):
    if re.match(pattern, strs):
        return True
    else:
        return False
input_string = input("Enter a string: ")
if match_string(input_string):
    print("The string matches the pattern.")
else:
    print("The string does not match the pattern.")
