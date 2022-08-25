def is_string(lst):
    return all([type(ll) == str for ll in lst])

#
# s = '3 3 3 2 3 3'
# res = any([True if ll < 3 else False for ll in list(map(int, s.split()))])
# if res:
#     print('отчислен')
# else:
#     print('учится')






