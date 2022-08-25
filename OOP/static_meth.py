# from math import sqrt
#
#
# class Vector:
#     MIN_COORD = 0
#     MAX_COORD = 100
#
#     @classmethod
#     def validate(cls, arg):
#         return cls.MIN_COORD <= arg <= cls.MAX_COORD
#
#     def __init__(self, x,y):
#         self.x = self.y = 0
#         if self.validate(x) and self.validate(x):
#             self.x = x
#             self.y = y
#
#     def get_coords(self):
#         return self.x, self.y
#
#     @staticmethod
#     def v_len(x,y):
#         return sqrt(x*x + y*y)
#
# v1 = Vector(15,25)
# v2 = Vector(1,2)
# v1.MIN_COORD = 20
# v1.MAX_COORD = 40
# print(v1.MIN_COORD, v1.MAX_COORD)
# print(v2.MIN_COORD, v2.MAX_COORD)
# print(Vector.MIN_COORD, Vector.MAX_COORD)
#
#==================================
# class Factory:
#     @staticmethod
#     def build_sequence():
#         return []
#
#     @staticmethod
#     def build_number(s):
#         return int(s)
#
#
#
# class Loader:
#     @staticmethod
#     def parse_format(string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq
#
#
# # эти строчки не менять!
# res = Loader.parse_format("1, 2, 3, -5, 10", Factory)
# print(res)
#==================================
# from string import ascii_lowercase, digits
# class TextInput:
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
#     def __init__(self, name, size = 10):
#         self.name = ''
#         self.check_name(name)
#         self.name = name
#         self.size = size
#
#
#     def get_html(self):
#         return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"
#
#     @classmethod
#     def check_name(cls, name):
#         if len(name) < 3: raise ValueError("некорректное поле name")
#         for s in name:
#             if not s in cls.CHARS_CORRECT: raise ValueError("некорректное поле name")
#
# class PasswordInput:
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
#     def __init__(self, name, size=10):
#         self.name = ''
#         self.check_name(name)
#         self.name = name
#         self.size = size
#
#     def get_html(self):
#         return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"
#
#     @classmethod
#     def check_name(cls, name):
#         if len(name) < 3: raise ValueError("некорректное поле name")
#         for s in name:
#             if not s in cls.CHARS_CORRECT: raise ValueError("некорректное поле name")
#
#
#
#
# class FormLogin:
#     def __init__(self, lgn, psw):
#         self.login = lgn
#         self.password = psw
#
#     def render_template(self):
#         return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
#
#
# # эти строчки не менять
# login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
# html = login.render_template()
#
# print(html)
#==================================
# from string import ascii_lowercase, digits
#
#
# class CardCheck:
#     CHARS_FOR_NAME = ascii_lowercase.upper() + digits
#
#     @staticmethod
#     def check_card_number(card_num):
#         if len(card_num) !=19 : return False
#         if(card_num[4] != '-' or card_num[9] != '-' or card_num[14] != '-'): return False
#         for st in ''.join(map(str, card_num.split('-'))):
#             if not st.isdigit(): return False
#         return True
#
#     @staticmethod
#     def check_name(card_name):
#         st_lst = list(map(str, card_name.split()))
#         if len(st_lst) !=2 : return False
#         for st in ''.join(map(str, st_lst)):
#             if st not in ascii_lowercase.upper(): return False
#         return True
#
# is_number = CardCheck.check_card_number("1234-5378-9012-0000")
# print(is_number)
# is_name = CardCheck.check_name("SERGEI BALAKIREV")
# print(is_name)
#==================================
#
# class Video:
#     def create(self, name):
#         self.name = name
#
#     def play(self):
#         print(f'воспроизведение видео {self.name}')
#
# class YouTube:
#     videos = []
#
#     @classmethod
#     def add_video(cls, video):
#         cls.videos.append(video)
#
#     @classmethod
#     def play(cls, video_indx):
#         cls.videos[video_indx].play()
#
# v1 = Video()
# v2 = Video()
# v1.create('Python')
# v2.create('Python ООП')
# YouTube.add_video(v1)
# YouTube.add_video(v2)
# YouTube.play(0)
# YouTube.play(1)
#==================================
# class Application:
#     def __init__(self, name, blocked = False):
#         self.name = name
#         self.blocked = blocked
#
#
# class AppStore:
#     def __init__(self):
#         self.app_list = []
#
#     def add_application(self, app):
#         self.app_list.append(app)
#
#     def remove_application(self, app):
#         self.app_list.remove(app)
#
#     def block_application(self, app):
#         app.blocked = True
#
#     def total_apps(self):
#         return len(self.app_list)
#
# store = AppStore()
# app_youtube = Application("Youtube")
# store.add_application(app_youtube)
# store.remove_application(app_youtube)
#
# print(store.total_apps())
#
# class Message:
#     def __init__(self, message, fl_like = False):
#         self.message = message
#         self.fl_like = fl_like
#
# class Viber:
#     __mess_list = []
#
#     @classmethod
#     def add_message(cls, msg):
#         cls.__mess_list.append(msg)
#
#     @classmethod
#     def remove_message(cls, msg):
#         cls.__mess_list.remove(msg)
#
#     @classmethod
#     def show_last_message(cls, num):
#         b = num if num > len(cls.__mess_list) else len(cls.__mess_list)
#         for i in range(1,b):
#             print(cls.__mess_list[:-i].message)
#
#     @classmethod
#     def total_messages(cls):
#         return len(cls.__mess_list)
#
#     @staticmethod
#     def set_like(msg):
#         msg.fl_like = not msg.fl_like
#
# msg = Message("Всем привет!")
# Viber.add_message(msg)
# Viber.add_message(Message("Это курс по Python ООП."))
# Viber.add_message(Message("Что вы о нем думаете?"))
# Viber.set_like(msg)
# Viber.remove_message(msg)




