# a, b = map(int, input().split())
# print(a ** b)

str1 = "dobavlyaem---slagi--slug-k--url---adresam"
str2 = str1.replace("---","-").replace("--","-")

s = "My best friend is Python!"
s1 = s.replace(" ","\'",1).replace(" ", "\"")

rate = 73.54
rb = 1000
usd = rb / rate

s = f"Вы можете получить {usd}$ за {rb} рублей по курсу {rate}"
print(s)

