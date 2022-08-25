class Goods:
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024

Goods.price = 2048
Goods.inflation = 100

class Car:
    pass

setattr(Car,'model',"Тойота")
setattr(Car,'color',"Розовый")
setattr(Car,'number',"П111УУ77")

#print(Car.__dict__['color'])

class Notes:
    uid = 1005435
    title = "Шутка"
    author = "И.С. Бах"
    pages = 2

#print(getattr(Notes,'author'))

class Dictionary:
    rus = "Питон"
    eng = "Python"

#print(getattr(Dictionary,'rus_word', False))

# if 'rus_word' in Dictionary.__dict__:
#     print(getattr(Dictionary,'rus_word'))
# else:
#     print(False)

# class TravelBlog:
#     total_blogs = 0
#
# tb1 = TravelBlog()
# setattr(tb1,'name','Франция')
# setattr(tb1,'days',6)
#
# TravelBlog.total_blogs += 1
#
# tb2 = TravelBlog()
# setattr(tb1,'name','Италия')
# setattr(tb1,'days',5)
#
# TravelBlog.total_blogs += 1
#
#
# class Figure:
#     type_fig = 'ellipse'
#     color = 'red'
#
# fig1 = Figure()
# setattr(fig1,'start_pt',(10, 5) )
# setattr(fig1,'end_pt',(100, 20) )
# setattr(fig1,'color','blue' )
#
# delattr(fig1,'color')
#print(*(fig1.__dict__))

class Person:
    "class Person for study"
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'

p1 = Person()

if 'job' in p1.__dict__:
    print(True)
else:
    print(False)