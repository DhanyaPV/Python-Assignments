def has_unique_chars(s):
    s = s.lower().replace(" ", "")
    return len(s) == len(set(s))

input_str = input("Enter a string: ")
print(has_unique_chars(input_str))