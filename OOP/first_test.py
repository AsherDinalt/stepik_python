class Server:
    curr_num = 0
    def __new__(cls, *args, **kwargs):
        cls.curr_num +=1
        return super().__new__(cls)
    def __init__(self):
        self.ip = self.curr_num
        self.buffer  = []
    def get_ip(self):
        return self.ip
    def get_data(self):
        s = []
        for st in self.buffer:
            s.append(st)
        self.buffer = []
        return s

    def send_data(self,dt):
        Router.buffer.append(dt)


class Router:
    serv_list = []
    buffer = []

    def link(self,serv):
        if not serv in self.serv_list:
            self.serv_list.append(serv)

    def unlink(self, serv):
        if serv in self.serv_list:
            self.serv_list.remove(serv)
            return True
        else: return False

    def send_data(self):
        for dt in self.buffer:
            for sv in self.serv_list:
                if sv.get_ip() == dt.ip:
                    sv.buffer.append(dt)
                    break
        self.buffer = []


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


s1 = Server()
s2 = Server()
r = Router()
r.link(s1)
r.link(s2)
dt1 = Data('First data sent', s2.get_ip())
dt2 = Data('Second data sent', s2.get_ip())
dt3 = Data('Third data sent', s2.get_ip())
s1.send_data(dt1)
s1.send_data(dt2)
s1.send_data(dt3)
r.send_data()

print(len(r.buffer))
for stt in s2.get_data():
    print(stt.data)
print(len(s2.buffer))