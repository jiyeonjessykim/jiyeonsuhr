
def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
        
    return True

def main():
    test = int(input("Enter an integer:"))
    if is_prime(test) == True:
        print(True)
    else:
        print(False)

main()
