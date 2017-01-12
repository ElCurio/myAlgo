import random

def fibonacci(n):
    result = []
    iden = ["st", "nd", "rd"]
    count = 1
    f1 = 0
    f2 = 1
    next = 0
    while count <= n:
        if count == 1:
            result.append(0)
        elif count == 2:
            result.append(1)
        else:
            f1, f2 = f2, f2 + f1
            result.append(f2)
        count += 1
    if n < 1 or type(n) != int:
        print "Invalid input. Positive integer required"
        return 
    elif n < 4:
        print "The " + str(n) + iden[n-1] + " number in the fibonacci sequence is " + str(result[n-1]) 
    else:
        print "The " + str(n) + "th number in the fibonacci sequence is " + str(result[n-1])
    print "The sequence is " , result
    
    
count = 0
shown = []
while count < 3:
    num = int(random.random()*10) + 1
    if num in shown:
        pass
    else:
        count += 1
        shown.append(num)
        fibonacci(num)
       
