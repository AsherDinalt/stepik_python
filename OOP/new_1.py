# class Point:
#     def __new__(cls, *args, **kwargs):
#         print('Вызов __new__ для '+str(cls), id(cls))
#         return super().__new__(cls) #обязательно!!! иначе не работает
#
#     def __init__(self, a=0, b=0):
#         print('Вызов __init__ для ' + str(self), id(self))
#         self.a = a
#         self.b = b
#
# pt = Point(1,2)
# ====================================
# class AbstractClass:
#     def __new__(cls, *args, **kwargs):
#         return 'Ошибка: нельзя создавать объекты абстрактного класса'
#
# obj = AbstractClass()
# print(obj)
# ====================================
#
# class SingletonFive:
#     __last_instanse = None
#     __num = 0
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__num < 5:
#             s_obj = super().__new__(cls)
#             cls.__num += 1
#             cls.__last_instanse = s_obj
#             return s_obj
#         else:
#             return cls.__last_instanse
#     def __del__(self):
#         self.__num = 0
#         self.__last_instanse = None
#
#     def __init__(self, name):
#         self.name = name
#
#
# objs = [SingletonFive(str(n)) for n in range(10)]
# print(*map(id, objs))
# ====================================
# TYPE_OS = 1 # 1 - Windows; 2 - Linux
#
# class DialogWindows:
#     name_class = "DialogWindows"
#
# class DialogLinux:
#     name_class = "DialogLinux"
#
# class Dialog:
#
#     def __new__(cls, *args, **kwargs):
#         if TYPE_OS == 1:
#              dg = DialogWindows()
#         else:
#             dg = DialogLinux()
#         setattr(dg,'name',args[0])
#         return dg
#
#     def __init__(self, name):
#         self.name = name
#
# dlg = Dialog('1234')
# print(dlg.name)
# ====================================
# class Point:
#     def __init__(self, a=0, b=0):
#         self.a = a
#         self.b = b
#
#
#     def clone(self):
#         return Point(self.a, self.b)
#
# pt = Point(1,2)
# pt_clone = pt.clone()
# ====================================
# class Factory:
#     def build_sequence(self):
#         return []
#     def build_number(self,st):
#         return float(st)
#
# class Loader:
#     def parse_format(self, string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq
#
#
# # эти строчки не менять!
# ld = Loader()
# s = '4, 5, -6.5'
# res = ld.parse_format(s, Factory())
# print(res)
#
