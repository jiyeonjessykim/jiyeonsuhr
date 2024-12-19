

def future_value(p, i, t):
    f = p * (1+i)**t
    return f

def main():
    p = float(input("Enter current bank balance:"))
    i = float(input("Enter interest rate:"))
    t = float(input("Enter the amount of time that passes:"))
    print(future_value(p, i, t))


main()
