def fizz_buzz(limit):
    a = 1
    while (a <= limit):
        if (a % 3 == 0 and a % 5 == 0):
            print(f"{a} fizzbuzz!")
        elif (a % 3 == 0):
            print(f"{a} fizz")
        elif (a % 5 == 0):
            print(f"{a} buzz")
        a += 1
fizz_buzz(20)
    

def fizz_what(limit, fizz_num, buzz_num):
    num = 1
    while num <= limit:
        output = ""
        if num % fizz_num == 0:
            output += "fizz"
        if num % buzz_num == 0:
            output += "buzz"
        
        if output:
            print(f"{num} {output}")
        
        num += 1

fizz_what(20, 2, 4)

def sum_digits(n):
    total_sum = 0
    while n > 0:
        total_sum += n % 10
        n //= 10
    return total_sum   

n = 12345
result = sum_digits(n)
print(result)