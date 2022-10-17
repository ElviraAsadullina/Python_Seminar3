def check_for_input_error():
    while True:
        try:
            a = int(input('Введите любое натуральное число: '))
        except ValueError:
            print('Ошибка - необходимо ввести натуральное число!')
            continue
        if  a < 0:
            print('Ошибка - число должно быть положительным!')
            continue
        break
    return a
def fibonacci(n):
    if (n <= 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
def full_fibonacci(n):
    positive_fib = []
    negative_fib = []
    for i in range(number):
        positive_fib.append(fibonacci(i))
    for i in range(len(positive_fib)):
        if i % 2 == 0 and i != 0:
            negative_fib.append(positive_fib[i] * -1)
        if i % 2 != 0:
            negative_fib.append(positive_fib[i])
    negative_fib.reverse()
    full_fibonacci = negative_fib + positive_fib
    return full_fibonacci
number = check_for_input_error()
print(f'Последовательность Фибоначчи (включая негафибоначчи) для данного числа: {full_fibonacci(number)}')