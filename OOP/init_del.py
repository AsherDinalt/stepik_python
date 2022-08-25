# class Test1():
#     def __del__(self):
#         print('Deleting class Test1 ' + str(self))
#
# t = Test1()
# t = 0
# class Line:
#     def __init__(self,a,b,c,d):
#         self.sp = (a,b)
#         self.ep = (c, d)
#
# class Rect:
#     def __init__(self,a,b,c,d):
#         self.sp = (a,b)
#         self.ep = (c, d)
#
# class Ellipse:
#     def __init__(self,a,b,c,d):
#         self.sp = (a,b)
#         self.ep = (c, d)
#=========================================================================
# import random
# random.seed()
# elements = []
# for i in range(217):
#     j = random.randint(1,3)
#     a = random.uniform(0, 1000000)
#     b = random.uniform(0, 1000000)
#     c = random.uniform(0, a)
#     d = random.uniform(0, b)
#     if j == 1:
#         elements.append(Line(a,b,c,d))
#     elif j == 2:
#         elements.append(Rect(a, b, c, d))
#     else:
#         elements.append(Ellipse(a, b, c, d))
#
# for el in elements:
#     if isinstance(el, Line):
#         el.ep = (0,0)
#         el.sp = (0,0)
#=========================================================================
# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def is_triangle(self):
#         if ( (type(self.a) != float and type(self.a) != int)
#             or (type(self.b) != float and type(self.b) != int)
#             or (type(self.c) != float and type(self.c) != int)):
#             return 1
#         if self.a < 0 or self.b < 0 or self.c < 0:
#             return 1
#         if self.a + self.b < self.c or self.b + self.c < self.a or self.c + self.a < self.b:
#             return 2
#         return 3
#
# tr = TriangleChecker(1,1,5)
# print(tr.is_triangle())
#
#=========================================================================
# class Graph:
#
#     def __init__(self, data =[], isShow = True):
#         self.data = data[:]
#         self.is_show = isShow
#
#     def set_data(self, data):
#         self.data = data
#
#     def set_show(self, fl_show):
#         self.is_show = fl_show
#
#     def show_table(self):
#         if self.is_show:
#             print(*self.data)
#         else:
#             print('Отображение данных закрыто')
#
#     def show_graph(self):
#         if self.is_show:
#             print('Графическое отображение данных: ',*self.data)
#         else:
#             print('Отображение данных закрыто')
#
#     def show_bar(self):
#         if self.is_show:
#             print('Столбчатая диаграмма: ', *self.data)
#         else:
#             print('Отображение данных закрыто')
#
#
# s = '8 11 10 -32 0 7 18'
# data_graph = list(map(int, s.split()))
# gr = Graph(data_graph)
# gr.show_bar()
# gr.set_show(False)
# gr.show_table()
#=========================================================================
# class CPU:
#     def __init__(self, name, fr):
#         self.name = name
#         self.fr = fr
#
# class Memory:
#
#     def __init__(self, name, volume):
#         self.name = name
#         self.volume = volume
#
# class MotherBoard:
#     total_mem_slots = 4
#     def __init__(self, name, cpu, mem_slots):
#         self.name = name
#         self.cpu = cpu
#         self.mem_slots = mem_slots
#
#     def get_config(self):
#         res = []
#         res.append('Материнская плата: '+ self.name)
#         res.append('Центральный процессор: '+ self.cpu.name + ', ' +str(self.cpu.fr))
#         if len(self.mem_slots) >=1:
#             res.append('Слотов памяти: '+ str(self.total_mem_slots))
#             st = 'Память: '
#             for i in range(len(self.mem_slots)):
#                 if i != len(self.mem_slots)-1:
#                     st += self.mem_slots[i].name +'-'+str(self.mem_slots[i].volume) + '; '
#                 else:
#                     st += self.mem_slots[i].name + '-' + str(self.mem_slots[i].volume)
#             res.append(st.strip())
#         return res
#
#
# gp = CPU('Процессор Intel', 5700)
# mp1 = Memory('Memory 2GB', 2048)
# mp2 = Memory('Memory 16GB', 16384)
# mp = [mp1,mp2]
# mb = MotherBoard('Материнская плата', gp,mp)
#print(mb.get_config())
#=========================================================================
# class Table:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
# class TV:
#    def __init__(self, name, price):
#        self.name = name
#        self.price = price
# class Notebook:
#    def __init__(self, name, price):
#        self.name = name
#        self.price = price
# class Cup:
#    def __init__(self, name, price):
#        self.name = name
#        self.price = price
#
# class Cart:
#     goods = []
#
#     def add(self, gd):
#         self.goods.append(gd)
#     def remove(self, indx):
#         if indx in range(len(self.goods)-1):
#             self.goods.pop(indx)
#     def get_list(self):
#         res = []
#         for i in range(len(self.goods)):
#             if i != len(self.goods)-1:
#                 res.append(self.goods[i].name + ': '+ str(self.goods[i].price)+',')
#             else:
#                 res.append(self.goods[i].name + ': ' + str(self.goods[i].price))
#         return res
#
# tv1 = TV('TV1', 1500)
# tv2 = TV('TV2', 2800)
# tb1 = Table('TABLE', 893)
# nt1 = Notebook('NT1', 12566)
# nt2 = Notebook('NT2', 9988)
# cp1 = Cup('CUP',50)
# cart = Cart()
# cart.add(tv1)
# cart.add(tv2)
# cart.add(tb1)
# cart.add(nt1)
# cart.add(nt2)
# cart.add(cp1)
#print(cart.get_list())
#=========================================================================
# lst_in = ['1. Первые шаги в ООП',
#           '1.1 Как правильно проходить этот курс',
#           '1.2 Концепция ООП простыми словами',
#           '1.3 Классы и объекты. Атрибуты классов и объектов',
#           '1.4 Методы классов. Параметр self',
#           '1.5 Инициализатор init и финализатор del',
#           '1.6 Магический метод new. Пример паттерна Singleton',
#           '1.7 Методы класса (classmethod) и статические методы (staticmethod)']
#
# class ListObject:
#     def __init__(self, data, next_obj = None):
#         self.data = data
#         self.next_obj = next_obj
#     def link(self, obj):
#         self.next_obj = obj
#
# head_obj = ListObject(lst_in[0])
# c_obj = head_obj
# for i in range(1,len(lst_in)):
#     n_obj = ListObject(lst_in[i])
#     c_obj.link(n_obj)
#     c_obj = n_obj
#
# c_obj = head_obj
# while True:
#     print(c_obj.data)
#     if c_obj.next_obj != None:
#         c_obj = c_obj.next_obj
#     else:
#         break
#=========================================================================
# import random
#
# class Cell:
#     def __init__(self, around_mines = 0, mine = False):
#         self.around_mines = around_mines
#         self.mine = mine
#         self.fl_open = True
#
# class GamePole:
#
#     def __init__(self, N, M):
#         self.N = N # размер поля NxN
#         self.M = M # число мин
#         self.pole = [[Cell() for i in range(self.N)] for j in range(self.N)]
#         self.init()
#
#
#     def init(self):
#         m = 0
#         while m < self.M:
#             i = random.randint(0, self.N - 1)
#             j = random.randint(0, self.N - 1)
#             if self.pole[i][j].mine:
#                 continue
#             self.pole[i][j].mine = True
#             m +=1
#         idx = (-1, -1),(-1, -0),(-1, 1),(0, -1), (0, 1),(1, -1),(1, 0),(1, 1)
#         for i in range(self.N):
#             for j in range(self.N):
#                 n = sum(self.pole[i+k][j+l].mine for k,l in idx if 0<=i+k<self.N and 0<=j+l<self.N)
#                 self.pole[i][j].around_mines = n
#
#     def show(self):
#         for pp in self.pole:
#             print(*map(lambda p : '#' if not p.fl_open else p.around_mines if not p.mine else '*', pp))
#
#
#
#
# pole_game = GamePole(10,12)
# pole_game.show()
#
# N = 10
# M = 10
#
#
# def get_around_mines(i, j):
#     n = 0
#     for k in range(-1, 2):
#         for l in range(-1, 2):
#             ii, jj = k + i, l + j
#             if ii < 0 or jj < 0 or ii >= N or jj >= N:
#                 continue
#             if pole_game.pole[ii][jj].mine:
#                 n += 1
#     return n
#
#
# for i in range(N):
#     for j in range(N):
#         if not pole_game.pole[i][j].mine:
#             assert pole_game.pole[i][j].around_mines == get_around_mines(i,
#                                                                          j), f"неверное число мин вокруг клетки с индексами {i, j}"
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#































