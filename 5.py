my_list = [7, 5, 3, 3, 2]
n = int(input("Введите значение рейтинга: "))
lenght = len(my_list)
if n in my_list:
    id = my_list.index(n)
    my_list.insert(id, n)
else:
    if n > max(my_list):
        my_list.insert(0, n)
    elif n < min(my_list):
        my_list.insert(lenght, n)
    else:
        for i in range(lenght):
            a = my_list[i]
            b = my_list.index(a)
            if n > a:
                my_list.insert(b, n)
                break
print(my_list)
