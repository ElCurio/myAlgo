def palindrome():
    found = False
    number = 9
    while not found:
        for i in range(1, int( number ** 0.5) + 1):
            if number % i == 0:
                x = str(number)
                y = str(bin(number))[2:]
                if (x[:len(x)/2] == x[len(x):len(x)/2:-1]) and (y[:len(y)/2] == y[len(y):len(y)/2:-1]):
                    found = True
                    return number
            number += 1

a = palindrome()
print a
