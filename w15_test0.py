#pas
#Question 2
def ques2(num):
    if num > 99:
        answer = (num // 100) + (num % 10)
        return answer
print(ques2(231))
print(ques2(437))
print(ques2(44))

#Question 4

def no_a(s):
    n = 0
    result = ''
    while (n < len(s)):
        if (s[n] != 'a'):
            result += s[n]
            n += 1
        else:
            n += 1
    return result
print(no_a('apple'))
print(no_a('dog'))
    
        