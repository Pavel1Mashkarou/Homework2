N = int(input('Введите число N'))
Array = []
for i in range(N):
    Array.append(i+1)
print(*Array)
X = int(input('Введите число X для поиска'))
j = 0
for i in range(N):
    if Array[i] == X:
        j = j + 1
print(f'->{j}')