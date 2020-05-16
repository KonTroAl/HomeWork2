lenght = int(input("Какой длины будет ваш список? "))
i = 0
my_list = []
while i < lenght:
    n = int(input("Enter you number: "))
    my_list.append(n)
    i = i + 1
print(my_list)

new_list = []
for el in range(len(my_list) - 1):
    var_1 = my_list[el]
    var_2 = my_list[el + 1]
    var_1, var_2 = var_2, var_1
    new_list.append(var_1)
    new_list.append(var_2)
new_list.pop()

print(new_list)
