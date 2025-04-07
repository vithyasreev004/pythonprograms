def replace_char(chars):
    first_char = chars[0]
    a = first_char
    for i in range(1, len(chars)):
        if chars[i] == first_char:
            a += '$'
        else:
            a += chars[i]
    print("Modified string:", a)

chars = input('Enter a string: ')
replace_char(chars)
