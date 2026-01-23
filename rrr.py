# Декоратор
baze = {}


def decor(func):
    def wran(*args, **kwargs):
        if args:
            print(f"args - {args}")
        if kwargs:
            print(f"kwargs - {kwargs}")
            for key, value in kwargs.items():
                if hash(key) in baze.keys():
                    print(f"Значение из словаря {baze.items()}")
                else:
                    baze[hash(key)] = value
                    print(f"Значение добавляем {hash(key)}:{value}")
        res = func(*args, **kwargs)
        if hash(res) in baze.keys():
            print(f"Значение из словаря {baze.items()}")
        else:
            baze[hash(res)] = res
            print(f"Значение res добавляем {hash(res)}:{res}")
        print(f"Результат {res}")
        return res

    return wran


@decor
def arif(a, b):
    return a * b


@decor
def arif1(s, k, c):
    return s * k * c


if __name__ == "__main__":
    arif(a=37572, b=4555.5552)
    arif(a=37572, b=4555.5552)
    arif(a=37572, b=4555.5552)
    arif1(s=572, k=452,c=565.225)
    arif1(s=572, k=452, c=565.225)
    print(f"СЛОВАРЬ{baze}")
