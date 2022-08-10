def calcV(a, b, c):
    print(a, b, c)


def check_password(psw, chars='$%!?@#'):
    if len(psw) < 8: return False
    for s in psw:
        if s in chars: return True
    return False


def cnv(st, sep='-'):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
         'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
         'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
         'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    res = ''
    for s in st:
        if s == ' ':
            res += sep
        elif t.get(s) != None:
            res += t.get(s)
        else:
            res += s
    return res


# print(cnv('Лучший курс по Python!'.lower(), sep = '+'))
def get_data_fig(*lengths, **kwars):
    p = 0
    for l in lengths:
        p += l
    t = tuple()
    t = t + (p,)
    if 'type' in kwars: t = t + (kwars['type'],)
    if 'color' in kwars: t = t + (kwars['color'],)
    if 'closed' in kwars: t = t + (kwars['closed'],)
    if 'width' in kwars: t = t + (kwars['width'],)
    return t


nn = [[1, 0, 0, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 1, 0, 1, 0],
      [0, 0, 0, 0, 0]]


def verify(nn):
    def verify_line(ln):
        for i in range(len(ln) - 1):
            if ln[i] + ln[i + 1] > 1:
                return False
        return True

    n = len(nn)
    for i in range(n):
        if not verify_line(nn[i]): return False
    for i in range(n-1):
        ll = []
        for j in range(n):
            ll.append(nn[i][j] + nn[i+1][j])
        if not verify_line(ll): return False
    return True

def str_min(s1,s2):
    if s1 < s2:
        return s1
    else:
        return s2

def str_min3(s1,s2, s3):
    return str_min(s3, str_min(s1,s2))

def str_min4(s1,s2, s3, s4):
    return str_min(s4, str_min3(s1,s2,s3))




print(str_min('01234567','123'))



