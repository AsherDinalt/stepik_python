# class MediaPlayer:
#     def open(self, file):
#         self.filename = file
#     def play(self):
#         print(f'Воспроизведение {self.filename}')
#
#
# media1 = MediaPlayer()
# media1.open('filemedia1')
# media2 = MediaPlayer()
# media2.open('filemedia2')
# media1.play()
# # media2.play()
# class Graph:
#     LIMIT_Y = [0,10]
#     def set_data(self, data):
#         self.data = data
#     def draw(self):
#         ll = list(filter(lambda l: self.LIMIT_Y[0] <= l and l <= self.LIMIT_Y[1], self.data))
#         print(*ll)
#
# graph1 = Graph()
# graph1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
# graph1.draw()
#
# class StreamData:
#     def create(self, fields, lst_values):
#         if len(fields) != len(lst_values):
#             return False
#         for i in range(0,len(fields)):
#             setattr(self, fields[i], lst_values[i])
#         return True
#
# FIELDS = ('id', 'title', 'pages')
# LST = [123,'Good morning', 16]
#
# str_1 = StreamData()
# str_1.create(FIELDS, LST)
# print(str_1.__dict__)

# lst_in = ['1 Сергей 35 120000','2 Федор 23 12000','3 Иван 13 1200']
#
# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')
#
#     def insert(self, data):
#         for dd in data:
#             d = dict()
#             ll = list(map(str, dd.split()))
#             for i in range(0,4):
#                 d[self.FIELDS[i]] = ll[i]
#             self.lst_data.append(d)
#
#     def select(self, a, b):
#         if b > len(self.lst_data)-1: b = len(self.lst_data)-1
#         ll = []
#         for i in range(a,b+1):
#             ll.append(self.lst_data[i])
#         return ll
#
# db = DataBase()
# db.insert(lst_in)
# class Translator:
#     lst_trans = []
#     def add(self, eng, rus):
#         t = (eng,rus)
#         if t in self.lst_trans: return
#         self.lst_trans.append(t)
#
#     def remove(self, eng):
#         for ll in self.lst_trans:
#             if ll[0] == eng:
#                 self.lst_trans.remove(ll)
#
#     def translate(self, eng):
#         ll = []
#         for l in self.lst_trans:
#             if l[0] == eng:
#                 ll.append(l[1])
#         return ll
#
# tr = Translator()
# tr.add('tree', 'дерево')
# tr.add('car','машина')
# tr.add('leaf', 'лист')
# tr.add('river', 'река')
# tr.add('go', 'идти')
# tr.add('go', 'ехать')
# tr.add('go', 'ходить')
# tr.add('milk', 'молоко')
# tr.remove('car')
#
# print(*tr.translate('go'))
