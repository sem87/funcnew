# реализуем хэш декоратор для функции
import random
import time


def decorhash(func):
    hashdict = {}

    def initial(*args, **kwargs):
        hashdata = (args, tuple(sorted(kwargs.items())))
        if hashdata in hashdict:
            # print("из хэш словаря")
            return hashdict[hashdata]
        res = func(*args, **kwargs)
        hashdict[hashdata] = res
        return res

    return initial


def decortime(func):
    def initial(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(f"Время выполнения {round(time.time() - start, 3)}")
        return res

    return initial


# факториал
# @decortime при рекурсии это не работает
@decorhash
def fact(n: int = 2) -> int:
    if n >= 1:
        if n == 0 or n == 1:
            return 1
        return n * (fact(n - 1))
    print("числа должны быть >1")


if "__main__" == __name__:
    hhh = {}
    for i in range(1, 1000000, 1):
        n = random.randint(1, 9)
        hhh[n] = fact(n=n)
    print(hhh)
