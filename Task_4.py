def check_for_input_error():
    while True:
        try:
            a = int(input('Введите число в десятичном формате: '))
        except ValueError:
            print('Ошибка - введено не числовое значение!')
            continue
        return a
def get_binary(n):
    binary_output = ''
    while n != 0:
        binary_output = str(n % 2) + binary_output
        n //= 2
    return binary_output
number = check_for_input_error()
print(f'Введенное число в двоичном формате: {get_binary(number)}')