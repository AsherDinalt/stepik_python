from functools import wraps

import math


def def_decorator(dx=0.01):
    def func_der(func):
        @wraps(func)
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res
        #wrapper.__name__ = func.__name__
        #wrapper.__doc__ = func.__doc__
        return wrapper

    return func_der


@def_decorator(dx=0.0001)
def sin_df(x):
    """ Функция для вычисления синуса, декоратор - для вычисления производной"""
    return math.sin(x)


def cos_df(x):
    return math.cos(x)


cos_df = def_decorator(dx=0.0001)(cos_df)

s = '5 6 3 6 -4 6 -1'

def sum_start(start = 0):
    def decor(func):
        def wrapper(s):
            return start + func(s)
        return wrapper
    return decor

@sum_start(start = 5)
def s_sum(s):
    res = 0
    for l in list(map(int, s.split())):
        res += l
    return res

s = 'Декораторы - это классно!'

def s_tag(tag = 'h1'):
    def decor(func):
        def wrapper(s):
            return '<'+tag+'>'+func(s)+'</' + tag+ '>'
        return wrapper
    return decor


@s_tag(tag='div')
def s_low(s):
    return s.lower()


t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

def s_res(chars=' !?'):
    def del_def(func):
      def inner(s):
            res = ''
            for st in func(s):
                if not st in chars:
                    res += st
                else:
                    res +='-'
            isDef = False
            res1=''
            for st in res:
                if st != '-':
                    res1 += st
                    isDef = False
                elif not isDef:
                    res1 += st
                    isDef = True
            return res1
      return inner
    return del_def






@s_res(chars='?!:;,. ')
def con_str(st):
    res = ''
    for s in st:
        if t.get(s) != None:
            res += t.get(s)
        else:
            res += s
    return res

s = 'Python - это круто!'.lower()

s = '1 2 3 55 -2 3 -18'
def sum_l(func):
    @wraps(func)
    def wrapper(s):
        res = 0
        for l in func(s):
            res += l
        return res
    return wrapper

@sum_l
def get_list(s):
    """Функция для формирования списка целых значений"""
    return list(map(int, s.split()))

print(get_list(s))