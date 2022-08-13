# x = {}
# print(type(x) in (float, int))
# print(isinstance(x, (str, float, dict)))
# print(type(x) == bool)
# print(isinstance(x, (str, float)))
# print(type(x) is int)
def get_add(a, b):
    if (type(a) in (str,int,float)) and (type(b) in (str,int,float)) and type(a) == type(b):
        return a + b
    elif (type(a) in (int,float)) and (type(b) in (int,float)):
        return a + b
    else: return None

def get_sum(it):
    s = sum(filter(lambda x: type(x) == int, it))
    return s


def get_even_sum(it):
    s = sum(filter(lambda x: x % 2 == 0, list(filter(lambda x: type(x) == int, it))))
    return s

def get_list_dig(lst):
    ll = list(filter(lambda x: (type(x) == int or type(x) == float), lst))
    return ll

print(get_list_dig([1,2,3, "a", True, [4, 5], "c", (4, 5)]))