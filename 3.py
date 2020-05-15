n = int(input("Введите порядковый номер месяца: "))
month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = n - 1

if month[b] == 12:
    print("winter")
elif 1 <= month[b] <= 2:
    print("winter")
elif 3 <= month[b] <= 5:
    print("spring")
elif 6 <= month[b] <= 8:
    print("summer")
elif 9 <= month[b] <= 11:
    print("autumn")
#############