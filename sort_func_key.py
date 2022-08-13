# s = 'Лена Енисей Волга Дон'.split()
# st = sorted(s, key = lambda x : - len(x))
# print(st)
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# # здесь продолжайте программу (используйте список строк lst_in)
# t_sorted = ()
# mask = [3, 0, 2, 1]
#
# t_sorted = [x.split(";") for x in lst_in]
# for i in range(0, len(t_sorted)):
#     for j in range(0, len(t_sorted[i])):
#         if t_sorted[i][j].isdigit():
#             t_sorted[i][j] = int(t_sorted[i][j])
#
# t_sorted = tuple(tuple(x) for x in [sorted(x, key=lambda i: mask[x.index(i)]) for x in t_sorted])
# print(t_sorted)

lst_in = ['Атос=лейтенант',
          'Портос=прапорщик',
          'д"Артаньян=капитан',
          'Арамис=лейтенант',
          'Балакирев=рядовой']
d={'рядовой':1, 'сержант':2, 'старшина':3,
   'прапорщик':4, 'лейтенант':5, 'капитан':6,
   'майор':7, 'подполковник':8, 'полковник':9}

lst = []
for l in lst_in:
    lst.append(list(map(str, l.split('='))))
lst.sort(key = lambda x : d[x[1]])

