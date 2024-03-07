def fizz_buzz(limit):
    a = 1
    while (a <= limit):
        if (a % 3 == 0 and a % 5 == 0):
            print(a, "fizzbuzz!")
        elif (a % 3 == 0):
            print(a, "fizz")
        elif (a % 5 == 0):
            print(a, "buzz")
        a += 1
fizz_buzz(20)
    

def fizz_what(limit, fizz_num, buzz_num):
    num = 1
    while (num <= limit):
        if (num % fizz_num == 0 and num % buzz_num == 0):
            print(n, "fizzbuzz!")
        elif
        
        num += 1

fizz_what(20, 2, 4)

def sum_digits(n):
    total_sum = 0
    while (n != 0):
    dig = n % 10
    sum+= dig
    n = n // 10
    return total_sum   

n = 12345
result = sum_digits(n)
print(result)