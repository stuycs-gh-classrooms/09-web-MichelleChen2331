<<<<<<< HEAD
def splitName(string):
    first_name = "1"
    last_name = "2"
    
    return (first_nam break + last_name )

print(splitName("John Shaft"))
=======
def split_name(name):
    a = name.find(' ')
    first_name = name[:a]
    last_name = name[a + 1:]
    final = first_name + '\n' + last_name
    return final

print(split_name("John Shaft"))

def bondify(name):
    a = name.find(' ')
    last_name = name[a + 1:]
    bond = last_name + '...' + name
    return bond

print(bondify("James Bond"))

def find_last(word, character):
    index = word.find(character)
    if index == -1:
        return -1
    
    return index
    

a = find_last('hello', 'l')
b = find_last('hello', 'h')
c = find_last('hello', 'z')
print(a)
print(b)
print(c)
>>>>>>> a14d4b4bc3dd0e6dddec2f8b9d212ab6db1a5b7a
