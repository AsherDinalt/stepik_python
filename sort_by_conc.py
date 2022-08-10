def add_lst(l1,l2):
    i = 0
    j = 0
    res = []
    while True:
        a = l1[i]
        b = l2[j]
        if a < b:
            res.append(a)
            if i < len(l1)-1:
                i+=1
            else:
                res = res +l2[j:len(l2)]
                break
        else:
            res.append(b)
            if j < len(l2)-1:
                j+=1
            else:
                res = res + l1[i:len(l1)]
                break
    return res

#print(add_lst([2,15,18,33,45],[4,11]))
#print(add_lst([12,18],[-6]))

l = [8, 11, -6, 3, 0, 1, 1]
#l = [11,8, -6]

def sort_conc(l):
    if len(l) == 1:
        return l
    if len(l) == 2:
        if l[0] < l[1]:
            return l
        else:
            return [l[1], l[0]]

    k = int(len(l) / 2)
    return add_lst(sort_conc(l[0:k]),sort_conc(l[k:len(l)]))

print(sort_conc(l))