#!/usr/bin/python3

# ASCII value of 'a'
start = ord('a')

# ASCII value of 'z'
end = ord('z')

# Iterate over ASCII values and print corresponding characters
for ascii_value in range(start, end + 1):
    print("{}".format(chr(ascii_value)), end="")

# Output will be the lowercase ASCII alphabet printed without a newline
