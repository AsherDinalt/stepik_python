import random

l = ['Тула', 'Казань', 'Смоленск', 'Семипалатинск', 'Уфа', 'Москва', 'Самара']
#print(random.choice(l))

# lst_in = ['1 2 3 4','5 6 7 8','9 8 6 7']
# random.seed(1)
# lst2D = [list(map(int, line.split())) for line in lst_in]
# z = zip(*lst2D)
# ls = list(z)
# random.shuffle(ls)
# z2 = list(zip(*ls))
# for i in z2:
#     print(*i)
#
#
# lst_in = ['Петров', 'Иванов', 'Сидоров', 'Балакирев', 'Фридман']
# ll = random.sample(lst_in, 3)
# for l in ll:
#     print(l, end = ' ')

N = 10
P = [[0] * N for i in range(N)]
k = 0
points = []

while k < 10:
    i = random.randint(0,N-1)
    j = random.randint(0,N-1)
    if ([i-1,j-1] in points
        or [i-1,j] in points
        or [i - 1, j+1] in points
        or [i - 1, j] in points
        or [i, j-1] in points
        or [i, j] in points
        or [i, j + 1] in points
        or [i+1, j - 1] in points
        or [i+1, j] in points
        or [i+1, j + 1] in points):
        continue
    else:
        points.append([i, j])
        k += 1


for point in points:
    P[point[0]][point[1]] = 1

for PP in P:
    print(PP)

