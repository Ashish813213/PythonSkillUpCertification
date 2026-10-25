# Return the smallest result of a+b, a-b, a*b and a//b.
# Division by zero is caught and that result is left out.

def find_minimum(a, b):
    vals = [a + b, a - b, a * b]
    try:
        vals.append(a // b)
    except ZeroDivisionError:
        pass
    return min(vals)
