def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

value = int(input("please enter a number:"))
print("The factorial of {} is {}".format(value,fact(value)))
