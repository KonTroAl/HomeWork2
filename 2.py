my_list = [1, 2, 3, 4, 5]
new_list = []
for i in range(len(my_list)):
    new_list.insert(i, my_list[i])
print(new_list)