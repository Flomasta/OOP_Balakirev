import time


def number():
    for a in range(2, 151):
        for b in range(2, 151):
            for c in range(2, 151):
                for d in range(2, 151):
                    yield a ** 5 + b ** 5 + c ** 5 + d ** 5, a, b, c, d


start_time = time.time()
for amount, a, b, c, d in number():
    e = int(amount ** (1 / 5))
    if amount == e ** 5:
        print(a, b, c, d, e)
        print(a + b + c + d + e)
        print(time.time() - start_time)
        break
