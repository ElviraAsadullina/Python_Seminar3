def get_mult(myList):
    size = len(myList)
    mults = []
    if size % 2 == 0:
        for i in range(int(size / 2)):
            mults.append(myList[i] * myList[len(myList) - i - 1])
    else:
        for i in range(int(size / 2 + 1)):
            mults.append(myList[i] * myList[len(myList) - i - 1])
    return mults
collection = [7, 11, 3, 15, 22, 6, 8, 1, 20]
# mult_collection = get_mult(collection)
print(f'Список произведений крайних пар чисел заданного списка: {get_mult(collection)}')