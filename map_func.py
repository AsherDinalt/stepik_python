# lst_in = ['8 11 -5',
#     '3 4 10',
#     '-1 -2 3',
#     '-4 5 6']
#
# lst2D = []
# for l in lst_in:
#     lst2D.append(list(map(int, l.split())))
#
# s = 'house=дом car=машина men=человек tree=дерево'
# s_lst = s.split()
# tp = tuple()
# l = []
# for ss in s_lst:
#     tt = tuple((map(str, ss.split('='))))
#     l.append(tt)
#
# tp =tuple(l)

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
st_in = 'Привет Питон'.lower()


def c_conv(s):
    if t.get(s) != None:
        return t.get(s)
    else:
        return '-'

st_out = ''
for c in map(lambda st: c_conv(st), st_in):
    st_out += c

st_in = 'Москва Уфа Вологда Тула Владивосток Хабаровск'
l_out = list(map(lambda st : st if len(st) > 5 else '-', st_in.split()))
for l in l_out:
    print(l, end = ' ')

