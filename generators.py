from string import ascii_lowercase, ascii_uppercase
import random
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"

l = []
for a in ascii_lowercase:
    for b in ascii_lowercase:
        l.append(a+b)
gen = (a for a in l)

# for i in range(0,2):
#     print(next(gen), end=' ')

def get_lst():
    for x in [1,2,3,4]:
        yield x

# for a in get_lst():
#     print(a)

chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
ll = len(chars)
n = 10
random.seed(1)
def gen_password(n):
    while True:
        s = ''
        for i in range(1,n):
            indx = random.randint(0, ll-1)
            s += chars[indx]
        yield s

# for i in range(0,5):
#     print(next(gen_password(n)))

def isSimple(n):
    res = True
    for i in range(2, n):
        if n % i == 0:
            res = False
            break
    return res


def isSimple_gen():
    i = 1
    while True:
        i += 1
        if isSimple(i):
            yield i


i = 0
for ff in isSimple_gen():
    if i < 20:
        print(ff, end = ' ')
        i +=1
    else:
        break

