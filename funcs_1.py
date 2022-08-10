def calc_list(ls):
    print(f'Min = {min(ls)}, max = {max(ls)}, sum = {sum(ls)}')

def is_url(st):
    if st.count('@') != 1:
        print('НЕТ')
    elif st.count('.') != 1:
        print('НЕТ')
    else:
        isURL = True
        for s in st:
            if not ('a' <= s <= 'z' or
                    'A' <= s <= 'Z' or
                    '0' <= s <= '9' or
                    s in '_@.'):
                isURL = False
                break
        if isURL:
            print('ДА')
        else:
            print('НЕТ')

def ret_d(s):
    return s, len(s)

#st = input().split()
st = 'Воронеж Лондон Тверь Омск Уфа'.split()
#s1 = ret_d('Воронеж')[0]
d = {ret_d(s)[0] : ret_d(s)[1] for s in st}
#d = {a:b = ret_d(s) for s in st}

#print(d)

a = sorted(d, key=lambda x: d[x])
print(*a)



