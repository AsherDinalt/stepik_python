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