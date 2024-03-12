def upcase(c):
    value = ord(c)
    if (value > 96 and value < 123):
        new = value - 32
        return chr(new)
    else: return c
        
        
print(upcase('a'))