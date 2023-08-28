# Modul bilangan Fibonacci
def fib(n):    
    # tulis deret Fibonacci hingga n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   
    # mengembalikan deret Fibonacci hingga n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
import fibo
fibo.fib(1000) # output : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
print(fibo.fib2(100)) # output : [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(fibo.__name__) # output : fibo
fib = fibo.fib
fib(500) # output :0 1 1 2 3 5 8 13 21 34 55 89 144 233 377


##..More on Modules##
print("---------------")
from fibo import fib, fib2
fib(500) # output : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
from fibo import *
fib(500) # output : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
# import fibo as fib
# fib.fib(500) 
# from fibo import fib as fibonacci
# fibonacci(500) 

##..Executing modules as scripts##
print("---------------")
fibo.fib(50) # output : 0 1 1 2 3 5 8 13 21 34
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))









    


