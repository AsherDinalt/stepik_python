s = lambda a,b : a + b
lst = [0, -1, 45, 2, 24, -82, 11]

def get_filter(a, filter = None):
    if filter is None:
        return a
    res = []
    for x in a:
        if filter(x):
            res.append(x)
    return res

f = lambda a : a % 2 == 0

get_div = lambda a,b : a /b if b != 0 else None

ls = [5, 4, -3, 4, 5, -24, -6, 9, 0]

def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res

f1 = lambda x : True if x < 0 else False
f2 = lambda x : True if x >= 0 else False
f3 = lambda x : True if 3 <= x <= 5 else False


print(filter_lst(ls))
print(filter_lst(ls, f1))
print(filter_lst(ls, f2))
print(filter_lst(ls, f3))