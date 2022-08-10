def get_rec_sum(l, f=[]):
    if len(l) == 1:
        return l[0]
    else:
        s = l[0]
        l.pop(0)
        return s + get_rec_sum(l)

def fib_rec(n, f=[]):
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]

    return fib_rec(n-1) + [fib_rec(n-1)[-1]+fib_rec(n-1)[-2]]

def fact_rec(n):
    def fc(n, m):
        if n == m:
            return n
        if abs(m-n) == 1:
            return n * m
        k = int((m - n) /2)
        return fc(n, n + k) * fc(n + k + 1,m)
    if n == 0: return 1
    if n == 1: return 1
    return fc(2,n)

d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]

def  get_line_list(d, se=[]):
    for de in d:
        if type(de) == list:
            get_line_list(de, se)
        else:
            se.append(de)
    return se

def get_path(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return get_path(n-1) + get_path(n-2)

