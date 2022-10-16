collection = [7, 11, 3, 15, 22, 6, 8, 1, 20]
sum = 0
for i in range(1, len(collection), 2):
       sum += collection[i]
print(f'Сумма элементов заданного списка c нечетными позициями = {sum}')