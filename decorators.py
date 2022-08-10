import time

def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        en = time.time()
        dt = en - st
        print(f'Working time = {dt}')
        return res
    return wrapper

def some_func():
    print('== some_func ==')

@test_time
def get_nod(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

@test_time
def get_nod_fast(a,b):
    if a < b:
        a,b = b, a
    while b:
        a,b = b, a % b
    return a

# get_nod = test_time(get_nod)
# get_nod_fast = test_time(get_nod_fast)
# print(get_nod(2, 1000000))
# print(get_nod_fast(2, 1000000))

s1 = 'house river tree car'
s2 = 'дом река дерево машина'
def two_lists(func):
    def inner(s1,s2):
        l1, l2 = func(s1,s2)
        d = {}
        for i in range(len(l1)):
            d[l1[i]] = l2[i]
        return d
    return inner

@two_lists
def two_lines(s1,s2):
    return list(map(str, s1.split())), list(map(str, s2.split()))

#print(two_lines(s1,s2))
#print(*sorted(two_lines(s1,s2).items()))

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

# здесь продолжайте программу
def del_def(func):
    def inner(s):
        st = func(s)
        isDef = False
        res =''
        for s in st:
            if s != '-':
                res += s
                isDef = False
            elif not isDef:
                res += '-'
                isDef = True
        return res
    return inner

@del_def
def con_str(st):
    res = ''
    for s in st:
        if t.get(s) != None:
            res += t.get(s)
        elif s in ': ;.,_':
            res += '-'
        else:
            res += s
    return res

s = 'Python - это круто!'.lower()
print(con_str(s))