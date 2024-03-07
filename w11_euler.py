def sum_of_multiples():
    total = 0
    num = 1
    while (num < 1000):
        if (num % 3 == 0 or num % 5 == 0):
            total += num
            num += 1
    
print(sum_of_multiples)

def prob_6():
    n = 100
    sum_of_squares = (n * (n + 1) * (2 * n + 1)) // 6
    square_of_sum = ((n * (n + 1)) // 2) ** 2
    difference = square_of_sum - sum_of_squares
    print(difference)
prob_6
def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_lcm(a, b):
    return a * b // calculate_gcd(a, b)

def smallest_multiple(limit):
    result = 1
    i = 1
    while i <= limit:
        result = calculate_lcm(result, i)
        i += 1
    return result

print(smallest_multiple)