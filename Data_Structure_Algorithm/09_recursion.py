def printFunction(test):
    print('Test ', test)
    if (test<1):
        return
    else:
        print(test,end=' ')
        print("-------")
        printFunction(test-1)
        print('xxxxxx')
        print(test,end=' ')
        return

test=3
# printFunction(test)

def factorial(num):
    if num==1:
        return num
    else:
        return num*factorial(num-1)

# print(factorial(5))

def fibonacci(num):
    if num<=1:
        return num
    else:
        return (fibonacci(num-1)+fibonacci(num-2))
    
for i in range(10):
    print(fibonacci(i))