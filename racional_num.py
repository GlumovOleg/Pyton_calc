from fractions import Fraction


def rac_nums(a, b, action):
    a = Fraction(a)
    b = Fraction(b)
    if action == '*':
        result = a * b
    elif action == '/':
        if b == 0:
            print('На 0 делить нельзя!')
            exit()
        result = float(a) / float(b)
    elif action == '+':
        result = a + b
    elif action == '-':
        result = a - b
    return result #== Fraction(a) / Fraction(b)
