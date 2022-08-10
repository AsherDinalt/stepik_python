a = {1,2,3,4,5,5,4,3,2,1}
a.add(7)
a.update([11,12,13,('hi', 'man')])
a.discard(11)

setA = {1,2,3,4,5}
setB = {4,5,6,7,8,9}
c = setA & setB
c = setA | setB
c = setA - setB
c = setB - setA
c = setA ^ setB

a = {x:x**2 for x in range(1,5)}

print(type(a), a)
#print(c)