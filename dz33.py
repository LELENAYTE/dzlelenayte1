def fib(n):
    pred_value = 0
    value = 1
    if n < 1:
        return 0
    for i in range(n):
        hold = value
        value += pred_value
        pred_value = hold
    return value


n = int(input("введите n:\t"))
print(1, *(fib(n) for n in range(1, n)))
