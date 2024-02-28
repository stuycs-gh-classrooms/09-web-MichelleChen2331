def distance (x1, x0, y1, y0):
    d = (x1 - x0)**2
    d = d + (y1 - y0)**2
    return d**0.5

print(distance(3, 0, 0, 4))
print(distance(1, 0, 2, 0))
print(distance(0, 0, 8, 15))


def f_to_c(fahrenheitTemp):
    celsuisTemp = (fahrenheitTemp - 32) * (5/9)
    return celsuisTemp

print(f_to_c(32.0))
print(f_to_c(212.0))
print(f_to_c(-40))

def eval_quadratic(a, b, c, x):
    y = ((a*x)** 2) + (b*x) + c
    return y

print(eval_quadratic(1, 0, 3, 1))
print(eval_quadratic(1, 2, 3, 1))
print(eval_quadratic(1, 0, 3, 2))

def is_even(n):
    if n%2==0:
        print(True)
    else:
        print(False)
    

is_even(12)
is_even(11)
is_even(0)