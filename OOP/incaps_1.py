# from accessify import private, protected
#
# class Point:
#     def __init__(self,x,y):
#         self.__x = self.__y = 0
#         if self.__check_value(x) and self.__check_value(x):
#             self.__x = x
#             self.__y = y
#     @private
#     @classmethod
#     def __check_value(cls,x):
#         return type(x) in (int, float)
#
#     def set_coord(self,x,y):
#         if self.__check_value(x) and self.__check_value(x):
#             self.__x = x
#             self.__y = y
#         else: raise ValueError('Must be numbers')
#
#     def get_coord(self):
#         return self.__x, self.__y
# #
# p = Point(1,2)
#===========================================================
# class Clock:
#     def __init__(self):
#         self.__time = 0
#     def get_time(self):
#         return self.__time
#
#     def __check_time(self, tm):
#         if 0 <= tm < 100000:
#             self.__time = tm
#             return True
#         else:
#             return False
#
#     def set_time(self,tm):
#         self.__check_time(tm)
#
# clock = Clock()
# clock.set_time(4530)
#
# class Money:
#     @staticmethod
#     def check_money(m):
#         if type(m) == int and m > 0: return True
#         else: return False
#
#     def __init__(self, m):
#         self.__money = 0
#         if self.check_money(m):
#             self.__money = m
#
#     def set_money(self, m):
#         if self.check_money(m):
#             self.__money = m
#
#     def get_money(self):
#         return self.__money
#
#     def add_money(self, mn):
#         if self.check_money(mn.get_money()):
#             self.__money += mn.get_money()
import random
# class Book:
#     def __init__(self,author,title,price):
#         self.__author = author
#         self.__price = price
#         self.__title = title
#     def set_title(self,title):
#         self.__title = title
#     def set_author(self, author):
#         self.__author = author
#     def set_price(self, price):
#         self.__price = price
#     def get_title(self):
#         return self.__title
#     def get_author(self):
#         return self.__author
#     def get_price(self):
#         return self.__price
#
# class Line:
#     def __init__(self, x1,y1,x2,y2):
#         self.__x1 = x1
#         self.__x2 = x2
#         self.__y1 = y1
#         self.__y2 = y2
#
#     def set_coords(self, x1, y1, x2, y2):
#         self.__x1 = x1
#         self.__x2 = x2
#         self.__y1 = y1
#         self.__y2 = y2
#
#     def get_coords(self):
#         return self.__x1, self.__y1, self.__x2, self.__y2
#
#     def draw(self):
#        print(*self.get_coords())
#===============================================
# class Point:
#     def __init__(self, x,y):
#         self.__x = x
#         self.__y = y
#     def get_coords(self):
#         return self.__x, self.__y
#
# class Rectangle:
#
#     def __init__(self, *args):
#         if (len(args)) == 2:
#             x1,y1 = args[0].get_coords()
#             x2, y2 = args[1].get_coords()
#             self.__sp = Point(x1,y1)
#             self.__ep = Point(x2,y2)
#         else:
#             self.__sp = Point(args[0],args[1])
#             self.__ep = Point(args[2],args[3])
#
#     def set_coords(self, sp, ep):
#         self.__sp = sp
#         self.__ep = ep
#
#     def get_coords(self):
#         return self.__sp ,self.__ep
#
#     def draw(self):
#         x1, y1 = self.__sp.get_coords()
#         x2, y2 = self.__ep.get_coords()
#         print(f'Прямоугольник с координатами: ({x1}, {y1}) ({x2}, {y2})')
#
# rect = Rectangle(Point(0,0),Point(20, 34))
#===============================================
# class ObjList:
#     def __init__(self, data):
#         self.__data = data
#         self.__prev = None
#         self.__next = None
#     def set_prev(self, obj):
#         if obj == None:
#             self.__prev = None
#         else:
#             self.__prev = obj
#     def set_next(self, obj):
#         if obj == None:
#             self.__next = None
#         else:
#             self.__next = obj
#     def get_prev(self):
#         return self.__prev
#     def get_next(self):
#         return self.__next
#     def set_data(self, data):
#         self.__data = data
#     def get_data(self):
#         return self.__data
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def add_obj(self, obj):
#         if self.head == None:
#             self.head = obj
#             self.tail = obj
#         else:
#             obj.set_prev(self.tail)
#             self.tail.set_next(obj)
#             self.tail = obj
#
#     def remove_obj(self):
#         if self.tail == None: return
#         oo = self.tail
#         self.tail = oo.get_prev()
#         if self.tail == None:
#             self.head = None
#             return
#         else:
#             self.tail.set_next(None)
#         oo.set_prev(None)
#
#     def get_data(self):
#         data_lst = []
#         c_addr = self.head
#         while True:
#             if c_addr == None: break
#             data_lst.append(c_addr.get_data())
#             c_addr = c_addr.get_next()
#         return data_lst
#
# lst = LinkedList()
# lst.add_obj(ObjList("данные 1"))
# lst.add_obj(ObjList("данные 2"))
# lst.add_obj(ObjList("данные 3"))
# obj4 = ObjList("данные 4")
# lst.add_obj(obj4)
# lst.remove_obj()
#
# res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
# print(res)
#==========================================================
# from string import ascii_lowercase, ascii_uppercase, digits
#
# class EmailValidator:
#     def __new__(cls, *args, **kwargs):
#         pass
#
#     @classmethod
#     def __is_email_str(cls, email):
#         if type(email) != str: return False
#         else: return True
#
#     @classmethod
#     def check_email(cls,st):
#         if not cls.__is_email_str(st): return False
#         if st.count('@') != 1:
#             return False
#         elif st.count('.') != 1:
#             return False
#         elif st.find('.', st.find('@')) < 0:
#             return False
#         else:
#             isURL = True
#             for s in st:
#                 if not ('a' <= s <= 'z' or
#                         'A' <= s <= 'Z' or
#                         '0' <= s <= '9' or
#                         s in '_@.'):
#                     isURL = False
#                     break
#             if isURL:
#                 return True
#             else:
#                 return False
#
#     @classmethod
#     def get_random_email(cls):
#         eml=''
#         str=ascii_lowercase + ascii_uppercase
#         i = int(random.uniform(0, len(str)))
#         eml += str[i]
#         str += digits
#         N = int(random.uniform(0, 20))
#         for i in range(N):
#             j = int(random.uniform(0, len(str)))
#             eml += str[j]
#         eml += '@gmail.com'
#         return eml
#
#
# res = EmailValidator.check_email("sc..lib@list.ru")
#
# print(res)
#
