def fibo(n):
    if (n==0 or n==1):
        return n
    elif (n==2):
        print("2")
        return 1
    else:
        print(n)
        return n+fibo(n-1)

value = int(input("please enter an index:"))
print(fibo(value))