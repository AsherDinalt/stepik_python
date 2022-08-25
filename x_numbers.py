
# key=123
# m = n ^ key
# k = m ^ key
#
# s = 'ѩкю[щюлцхZ'
# st = ''
# for stt in s:
#     st += chr(ord(stt) ^ key)
#
# print(st)

n = 106
mask = 0b001001000
print(bin(n))
print(bin(mask))
print('ДА' if n&mask >0 else 'НЕТ')