# Input
integer = eval(input("Enter a decimal integer: "))

hex_characters = "0123456789ABCDEF"
value = ""
# Convert to hexadecimal and print
if (integer == 0):
    value = "0"
elif (integer != 0):
    while integer > 0:
        mod = integer % 16
        value += hex_characters[mod]
        integer //= 16

# Print
print(f"{integer} ------ Hexadecimal -----> {value[::-1]} ")
