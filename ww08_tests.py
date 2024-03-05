def f_to_c(fahrenheitTemp):
    celsuisTemp = (fahrenheitTemp - 32) * (5/9)
    return celsuisTemp

def test_1(f, expected, i):
    x = f(i) == expected
    return x

print(test_1(f_to_c, 0, 32))

def distance (x1, x0, y1, y0):
    d = (x1 - x0)**2
    d = d + (y1 - y0)**2
    return d**0.5

def test_4(f, expected, i0, i1, i2, i3):
    y = f(i0, i1, i2, i3) == expected
    return y
print(test_4(distance, 5.0, 3, 0, 0, 4))



d0 = distance(3, 0, 0, 4)
d1 = distance(1, 0, 2, 0)
d2= distance(0, 0, 8, 15)
print("n/is distance tests: ")
print(d0, "expected: 5.0")
print(d1, "expected: 1.0")
print(d2, "expected: 17.0")

y0 = eval_quadratic(1, 0, 3, 1)
y1 = eval_quadratic(1, 2, 3, 1)
y2 = eval_quadratic(1, 0, 3, 2)
print("\neval_quadratic tests:")
print(y0, "expected: 4")
print(y1, "expected: 6")
print(y2, "expected: 7")