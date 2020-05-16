name = input("Введите наименование товаров через пробел: ").split()
price = input("Введите цену каждого товара через пробел: ").split()
value = input("Введите количество каждого товара через пробел: ").split()

# print(name, price, value)

number = len(name)
#name = ["компьютер", "принтер", "сканер"]
#price = [20000, 6000, 2000]
#value = [5, 2, 7]
i = 0
st = []

while i < number:
    n = name[i]
    p = price[i]
    v = value[i]
    list = {"название": n, "цена": p, "количество": v, "ед": "шт."}
    i = i + 1
    cort = (i, list)
    st.insert(i, cort)
print(st)

