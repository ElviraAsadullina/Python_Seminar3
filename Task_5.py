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
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        lst = fibonacci(n-1)
        lst.append(lst[-1] + lst[-2])
        return lst
def full_fibonacci(n, fib_list):
    negative_fib = []
    for i in range(len(fib_list)):
        if i % 2 == 0 and i != 0:
            negative_fib.append(fib_list[i] * -1)
        if i % 2 != 0:
            negative_fib.append(fib_list[i])
    negative_fib.reverse()
    full_fibonacci = negative_fib + fib_list
    return full_fibonacci
number = check_for_input_error()
positive_fib = fibonacci(number)
print(f'Последовательность Фибоначчи (включая негафибоначчи) для данного числа: {full_fibonacci(number, positive_fib)}')