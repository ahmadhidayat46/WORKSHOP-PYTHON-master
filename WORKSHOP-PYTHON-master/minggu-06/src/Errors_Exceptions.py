### Syntax Errors ##
# while True print('Hello world')
#   File "<stdin>", line 1
#     while True print('Hello world')
# # output => SyntaxError: invalid syntax

###Exceptions##
# 10 * (1/0)
# output => ZeroDivisionError: division by zero
# 4 + spam*3
# output => NameError: name 'spam' is not defined
# '2' + 2
#output => TypeError: can only concatenate str (not "int") to str

##Handling Exceptions##
while True:
    try:
        #input yang dapat dikonversi menjadi bilangan bulat, 
        #'x' akan berisi nilai tersebut 
        x = int(input("Please enter a number: "))#contoh => Please enter a number: 2
        break #menghentikan loop.
    except ValueError:
        #input yang tidak dapat dikonversi menjadi bilangan bula,akan menampilkan "Oops!  That was no valid number.  Try again..."
        print("Oops!  That was no valid number.  Try again...")#contoh =>Please enter a number: 2.0

#jika inputan sesuai dan tidak sesuai maka outputan tergantung dengan inputan yang diberikan 
#jika benar menampilkan B,C,D 
#jika salah "Oops!  That was no valid number.  Try again..."
    except (RuntimeError, TypeError, NameError):
        pass
class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
# contoh => Please enter a number: 2.0
# Oops! That was not a valid number. Try again...
# Please enter a number: C
# Oops! That was not a valid number. Try again...
# Please enter a number: D
# Oops! That was not a valid number. Try again...
# Please enter a number: B
# Oops! That was not a valid number. Try again...
# Please enter a number: 1
# B
# C
# D
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # jenis pengecualian
    print(inst.args)     # argumen disimpan di .args
    print(inst)          # __str__ memungkinkan args untuk dicetak secara langsung,
                         # tetapi dapat diganti dalam subkelas pengecualian
    x, y = inst.args     # membongkar arg
    print('x =', x)
    print('y =', y)
#contoh => Please enter a number: 2.3
# Oops!  That was no valid number.  Try again...
# Please enter a number: 1
# B
# C
# D
# <class 'Exception'>
# ('spam', 'eggs')
# ('spam', 'eggs')
# x = spam
# y = eggs

import sys
#output=> Could not convert data to an integer.
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

#output => Handling run-time error: division by zero
def this_fails():
    x = 1/0
try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

##Raising Exceptions##
raise NameError('HiThere')
        # output => Traceback (most recent call last):
        #   File "d:\SEMESTER 6\WORKSHOP PYTHON\minggu-06\src\Errors_Exceptions.py", line 111, in <module>
        #     raise NameError('HiThere')
        # NameError: HiThere
raise ValueError  # shorthand for 'raise ValueError()'
        # output valueError
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
# output => NameError: HiThere

##Exception Chaining##
try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error")
def func():
    raise ConnectionError
try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc
try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None

##Defining Clean-up Actions##
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')
    #output => KeyboardInterrupt

def bool_return():
    try:
        return True
    finally:
        return False
result = bool_return()
print(result)
# fungsi bool_return() yang mengembalikan True di dalam blok try, tetapi kemudian mengembalikan False di dalam blok finally. Saat fungsi dipanggil dan nilainya ditetapkan ke result, maka output yang dihasilkan adalah False.

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
divide(2, 1)
divide(2, 0)
divide("2", "1")
# fungsi divide(x, y) yang mencoba membagi x dengan y. Jika terjadi ZeroDivisionError, maka akan mencetak pesan "division by zero!". Jika tidak ada error, maka akan mencetak pesan "result is" diikuti dengan hasil pembagian. Setelah itu, selalu akan menjalankan blok finally yang mencetak "executing finally clause". Pemanggilan fungsi divide() dilakukan tiga kali dengan argumen yang berbeda.

##Predefined Clean-up Actions##
for line in open("myfile.txt"):
    print(line, end="")
#output =>10,1, 12,r 
#for digunakan untuk mengiterasi setiap baris dalam file tersebut. Setiap baris kemudian dicetak menggunakan print(), dengan argumen end=""

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
# output => 10,1, 12,r
#"with" untuk memastikan bahwa file akan ditutup setelah selesai,File diwakili oleh variabel f

##Raising and Handling Multiple Unrelated Exceptions##
def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)
f()
try:
    f()
except Exception as e:
    print(f'caught {type(e)}: e')
def f():
    raise ExceptionGroup("group1",
                         [OSError(1),
                          SystemError(2),
                          ExceptionGroup("group2",
                                         [OSError(3), RecursionError(4)])])

try:
    f()
except OSError as e:
    print("There were OSErrors")
except SystemError as e:
    print("There were SystemErrors")
excs = []
for test in tests:
    try:
        test.run()
    except Exception as e:
        excs.append(e)
if excs:
   raise ExceptionGroup("Test Failures", excs)

#Enriching Exceptions with Notes##
try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Add some information')
    e.add_note('Add some more information')
    raise
#output =>  e.add_note('Add some information')
def f():
    raise OSError('operation failed')
excs = []
for i in range(3):
    try:
        f()
    except Exception as e:
        e.add_note(f'Happened in Iteration {i+1}')
        excs.append(e)
raise ExceptionGroup('We have some problems', excs)
