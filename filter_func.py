from string import ascii_lowercase, ascii_uppercase

# s1 = '1 5 2 7 10 25 50 100'
# s2 = '5 2 3 7 10 25 55'
# l1 = list(map(int, s1.split()))
# l2 = list(map(int, s2.split()))
#
# l = sorted(list(filter(lambda l : l in l1 and l % 2 == 0, l2)))
#
# for ll in l:
#     print(ll, end = ' ')



s ='abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com'

def is_norm(s):
    if s.count('@') == 0:
        return False
    if s.count('.') == 0:
        return False
    if s.find('.', s.find('@')) < 1 :
        return False
    for st in s:
        if not (st in ascii_lowercase or st in '_@.1234567890'):
            return False
    return True

ll = list(filter(is_norm, s.split()))
for l in ll:
    print(l, end = ' ')






