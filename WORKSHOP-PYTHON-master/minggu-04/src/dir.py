##..The dir() Function##
import fibo, sys_1
dir(fibo)
dir(sys_1)  
#output : 
    # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 
    # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    # fibo
    # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
    # ---------------
    # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
    # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
    # ---------------
    # 0 1 1 2 3 5 8 13 21 34
    # Yuck!
# 'a', mengimpor modul fibo, menetapkan fungsi 'fib' dari modul 'fibo' ke variabel 'fib', dan kemudian mencetak daftar nama-nama simbol yang saat ini didefinisikan dalam lingkungan saat ini dengan menggunakan fungsi dir().
a = [1, 2, 3, 4, 5]
import fibo
fib = fibo.fib
dir()

import builtins
dir(builtins)  