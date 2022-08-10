# d = {"river": "река", 'road': 'Дорога', 'one': 1}
# d = {}
# s = 'one=1 two=2 three=3'
# l1 = ['one=1','two=2','three=3']
# l2 = [l1[i].split("=") for i in range(len(l1))]
# print(l2)
# s = '+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890'
# l1 = list(map(str, s.split()))
# d = dict()
# for i in range(len(l1)):
#     if d.get(l1[i][:2]) != None:
#         d.get(l1[i][:2]).append(l1[i])
#     else:
#         d.update({l1[i][:2]: [l1[i]]})

#
#d1 = {"river": "река", 'road': 'Дорога', 'one': 1}
# d2 = d1
# d1["river"] = '======'
# print(d1)
# print(d2)
#print(d1.pop('www', '----'))
# print(d1.values())
# print(d1.keys())
# d3 = {**d1, **d2} d3 = d1 | d2
# for k, v in d1.items():
#     print(k, v)
s = 'Сергей Балакирев'
chars = {"А": ".-", "Б": "-...", "В": ".--","Г": "--.",
         "Д": "-..", "Е": ".", "Ж": "...-", "З": "--..",
         "И": "..", "Й": ".---", "К": "-.-", "Л": ".-..",
         "М": "--", "Н": "-.", "О": "---", "П": ".--.",
         "Р": ".-.", "С": "...", "Т": "-", "У": "..-",
         "Ф": "..-.", "Х": "....", "Ц": "-.-.", "Ч": "---.",
         "Ш": "----", "Щ": "--.-", "Ъ": "--.--", "Ы": "-.--",
         "Ь": "-..-", "Э": "..-..", "Ю": "..--", "Я": ".-.-",
         " ": "-...-"}
# sout=''
# for c in s.upper():
#     sout += chars.get(c)
#     sout += ' '
# print(sout.strip())

# ls = '.-- ... . -...- .-- . .-. -. ---'.upper().split()
# rev = {v:k for k,v in chars.items()}
# sout=''
# for c in ls:
#      sout += rev.get(c)
# #     sout += ' '
# print(sout.strip())

things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
s_t = sorted(things, key = things.get, reverse=True)
s_w = []
for w in s_t:
    s_w.append(things.get(w))

#print(s_w)
# s_things={}
# for w in s_t:
#     s_things[w]= things[w]

n = 10 * 1000
for i in range(len(s_w)):
    if n >= s_w[i]:
        print(s_t[i], end = " ")
        n -= s_w[i]
        if n <= 0:
            break


