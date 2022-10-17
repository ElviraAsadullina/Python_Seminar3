def check_for_input_error():
    while True:
        try:
            a = list(map(float, input('Введите несколько вещественных чисел через пробел: ').split(' ')))
        except ValueError:
            print('Ошибка - введено не числовое значение!')
            continue
        return a
def find_diff_max_min(myList):
    max_element = min_element = myList[0]
    for i in myList:
        if i > max_element:
            max_element = i
        if i < min_element:
            min_element = i
    diff = max_element - min_element
    return diff
collection = check_for_input_error()
floor_collection = []
for i in collection:
    floor_collection.append(int((i % 1) *100) / 100)
print(f'Разница между максимальным и минимальным значениями дробной части элементов списка = {find_diff_max_min(floor_collection)}')
