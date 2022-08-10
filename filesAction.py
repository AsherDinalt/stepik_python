import pickle

file = open('/home/al/PycharmProjects/Stepik/test_file.txt',encoding="utf-8")
# print(file.read(4))
# print(file.tell())
# s = file.readlines()
# print(type(s))
file.close()

try:
    file = open('/home/al/PycharmProjects/Stepik/test_file.txt', encoding="utf-8")
    try:
        s = file.readlines()
        #print(s)
    finally:
        file.close()
except FileNotFoundError:
    print('No such file')
except:
    print('File error')

#with open('/home/al/PycharmProjects/Stepik/out_file.txt', 'w') as file
# file = open('/home/al/PycharmProjects/Stepik/out_file.txt', 'w')
# file.write('Hello, world!')
# file.close()
d = {'car': 'машина', 'tree': 'дерево', 'road': 'дорога'}

try:
    with open('/home/al/PycharmProjects/Stepik/out_file.bin', 'rb') as file:
         d1 =pickle.load(file)
         print(d1)
except FileNotFoundError:
    print('No such file')




