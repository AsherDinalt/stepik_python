def prn(name):
    def inner():
        print(f'Hi, {name}')
    return inner

f = prn('Alex')
f()