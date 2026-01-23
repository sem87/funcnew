import random


def decor(func):
    def wran(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in wran.baze:
            print(f"Достал из базы {wran.baze[key]}")
            return wran.baze[key]
        res = func(*args, **kwargs)
        wran.baze[key] = res
        return res
    # Декоратор
    wran.baze = {}
    return wran

@decor
def arif(s, k, c):
    return s * k * c


if __name__ == "__main__":
    # arif(a=37572, b=4555.5552)
    # arif(a=37572, b=4555.5552)
    # arif(a=37572, b=45)
    for i in range(1, 100, 1):
        s = random.randint(1,10000)
        arif(s=s, k=4, c=5)
    print(f"Размер кэша - {len(arif.baze)}")
    print(arif.baze)
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    for i in range(1, 100, 1):
        s = random.randint(1,10000)
        arif(s=s, k=4, c=5)
    print(f"Размер кэша - {len(arif.baze)}")
    print(arif.baze)
    # for i in range(1, 100, 1):
    #     s = random.randint(1,10)
    #     arif1(s=s, k=4, c=5)
    # print(f"Размер кэша 2 - {len(arif1.baze)}")
    # print(arif1.baze)

