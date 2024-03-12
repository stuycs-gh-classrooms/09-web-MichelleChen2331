def upcase(c):
    value = ord(c)
    if (value > 96 and value < 123):
        new = value - 32
        return chr(new)
    else: return c
        
        
print(upcase('a'))
print(upcase('E'))
print(upcase('1'))

def upstring(word):
    output_string = ""
    for char in word:
        if 'a' <= char <= 'z':
            output_string += chr(ord(char) - 32)
        else:
            output_string += char
    return output_string

print(upstring("Hello World"))