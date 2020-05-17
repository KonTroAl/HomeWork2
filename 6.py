name = input("Введите наименование товаров через пробел: ").split()
price = input("Введите цену каждого товара через пробел: ").split()
value = input("Введите количество каждого товара через пробел: ").split()

number = len(name)
i = 0
st = []

for i in range(number):
    n = name[i]
    p = price[i]
    v = value[i]
    list = {"название ": n, "цена ": p, "количество ": v, "ед ": "шт."}
    i = i + 1
    cort = (i, list)
    st.insert(i, cort)
print(st)

sum = {
    "название": name,
    "цена": price,
    "количество": value,
    "ед ": "шт."
}
print(sum)
