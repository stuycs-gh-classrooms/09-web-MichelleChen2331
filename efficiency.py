import time #needed for later


# Project euler problem 5 is:
#      2520 is the smallest number that can be divided by
#      each of the numbers from 1 to 10 without any remainder.
#      What is the smallest positive number that is evenly
#      divisible by all of the numbers from 1 to 20?
# (https://projecteuler.net/problem=5)

# Here is one way to solve the problem:
# 1.  guess that the answer is n
# 2a. Check if guess is divisible by 1.
# 2b. Check if guess is divisible by 2.
# 2... Keep checking for divisibility until reaching n
# 3a. If at any point guess is not divisble, increase guess
#     by 1, go back to step 2.a
# 3b. If guess is divisble up to n, return guess.

# The following function follows the above algorithm:
def euler5(n):
    t = time.time()
    guess = n
    max_divisor = 1
    while max_divisor <= n:
        if guess % max_divisor == 0:
            max_divisor+= 1
        else:
            guess+= 1
            max_divisor = 1
    return guess
answer = euler5(10)
print("euler5(10): ", answer)

#==================================================
# Problem 0

# We want to be able to discuss how long this function takes to run.
# We can measure this in time, or in number of loop iterations.
# Let us start with loop iterations

# Below is the euler5 function, modify it such that before it ends
# it prints out the total number of loops needed to get the answer.

def euler5_loop_count(n):
    t = time.time()
    guess = n
    max_divisor = 1
    loops = 0
    while max_divisor <= n:
        loops += 1
        if guess % max_divisor == 0:
            max_divisor+= 1
        else:
            guess+= 1
            max_divisor = 1

    return loops
    
# To test, use this, it should take 25 loops to get the answer
# which is 12
print("Testing loop count only:")
answer = euler5_loop_count(4)
print("loop count: ", answer)
print("euler5(4):", euler5(4))



# End Problem 0
#==================================================

#==================================================
# Problem 1

# We can also talk about how long a fucntion takes measured in seconds.
# time.time() will return the number of seconds since 1/1/1970. This is
# known as EPOCH time.

# Below are 2 calls to euler5_loop_count. Add code above and below
# each call to display the number of seconds taken to run each.

print("Timing slow version:")

#YOUR CODE HERE
answer = euler5_loop_count(10)
print("loop count:", answer)
print("euler5(10): ", euler5(10))
seconds = time.time() 
print("elapsed time: ", seconds)


print("Second slow version test:")
#YOUR CODE HERE

answer = euler5_loop_count(20)
#YOUR CODE HERE

print("loop count: ", answer)
seconds = time.time()
print("elapsed time: ", seconds)
print("answer euler5(20)", euler5(20))

# End Problem 1
#==================================================


#==================================================
# Problem 2

# Hopefully, you noticed that the loop count and time to
# get the answer for 20 were both quite large.

# Now we can look at the algorithm from the begining and
# ask ourselves: can we make it faster?

# Below is a copy of euler_5_loop_count, first, add
# the code to count and print the number of loops from
# Problem 0

# Then, try to decrease the number of loops run.
# Think about what you need to do each time to
# have to reset your guess. Can you make it better?

# An initial goal should be to get the loop count for
# 20 down to 416,181,955.

# But eventually, you should be able to get the loop count
# for 20 down to 51,473,642.
def euler5_better(n):
    t = time.time()
    guess = n
    max_divisor = 1
    loops = 0
    result = 1

    while max_divisor <= n:
        loops += 1
        if guess % max_divisor == 0:
            result = result * max_divisor // gcd(result, max_divisor)
            max_divisor += 1
        else:
            guess += 1
            max_divisor = 1

    return result

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print("\nBetter version:")
# Dont forget to include time code as well
count = euler5_better(20)
seconds = time.time()

answer = euler5(20)
print("loop count:", count)
print("elapsed time: ", seconds)
print("answer euler5(20): ", answer)


#==================================================
# An advanced approach

# Perhaps the number above is not good enough for you.
# Well, try this on for size!

# This function will find the least common multiple of
# 2 integers.
def lcm(max_divisor, guess):
    m = guess
    while m % max_divisor != 0:
        m+= guess
    return m

# Can you use this to make your solution for euler5
# even better?
# Write a new version, and test it, measuring
# both time and loop counts.
# To keep track of loop counts, you may need
# to consolodate the lcm function into your main
# euler5 function.


def euler5_best(limit):
    t = time.time()
    result = 1
    i = 1
    loops = 0
    while i <= limit:
        loops += 1
        result = lcm(result, i)
        i += 1
    return result, i, loops, t

a, b, c, d = euler5_best(20)
print("Best Verison:")
print("elapsed time:", d)
print("loop count:", c)
print("answer euler5(20):", a)

# End advanced approach
#==================================================
