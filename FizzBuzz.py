for x in range(1,101):
    string = ""
    if x % 3 == 0:
        string = string + "Fizz"
    if x % 5 == 0:
        string = string + "Buzz"
    if x % 3 != 0 and x % 5 != 0:
        string = string + str(x)
    print(x)
    
