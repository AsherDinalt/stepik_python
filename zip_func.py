# s1 = '-7 8 11 -1 3'
# s2 = '1 2 3 4 5 6 7 8 9 10'
#
# l1 = map(int, s1.split())
# l2 = map(int, s2.split())
#
# z = map(lambda x: x[0] * x [1], zip(l1,l2))
#
# for i in range(0,3):
#     print(next(z), end = ' ')

# s = 'Москва Уфа Тула Самара Омск Воронеж Владивосток Лондон Калининград Севастополь'
# st_iter = iter(s.split())
# ls = list(zip(st_iter, st_iter, st_iter))
# print(ls)
#
# st_iter = iter(s.split())
# ls = list(zip(*[st_iter]*3))


# x = iter([1,2,3,4,5,6,7,8,9,10])
# print(list(zip(x, x, x)))
#print(list(zip([1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9])))

s = 'Python дай мне силы пройти этот курс до конца!'
n = 10
it = iter(range(0,n))
its = iter(s)
lst = list(zip(its,it))
