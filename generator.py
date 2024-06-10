def fib(number):
    a = 0
    b = 1
    for i in  range(number):
        yield a
        item = a
        a = b
        b = item + b
for x in fib(21):
    print(x)

