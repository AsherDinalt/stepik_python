# s = '-2 -1 8 11 4 5 '
# lst = list(map(int, s.split()))
# lst.sort()
# tp_lst = tuple(lst)
# print(tp_lst)
#
# d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
#
# def get_sort(d):
#     l = list(map(lambda dd : d.get(dd), sorted(d, reverse=True)))
#     return l
lst_in = ['смартфон:120000', 'яблоко:2', 'сумка:560',
          'брюки:2500', ' линейка:10', 'бумага:500']
d = dict()
for l in lst_in:
    d[int(l.split(':')[1])] = l.split(':')[0]
d_out = sorted(d)
for i in range(0, 3):
    print(d.get(d_out[i]), end=' ')

#for dd in sorted(d, reverse=True):






