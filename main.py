import random

negr = [-15, -4, -2, -7, 0, 3, 5, 12, 7] #создаем список
rows = random.randint(4, 8) #рандом целых чисел от 4 до 8
cols = random.randint(4, 8) #рандом целых чисел от 4 до 8

matrix = [] #пустой список
for _ in range(rows): 
 row = random.choices(negr, k=cols) #выбираем роандом число из списка negr b кол во благодарпя cols
 matrix.append(row) #создаем матрицу

for i in matrix: 
 print(*i) #выводим матрицу

sum = 0
for i in matrix: 
    for num in row:  # Перебираем числа в каждой строке
     if num % 2!= 0: 
        sum = sum + num
print( "сумма элементов нечетных элементов", num) 
