n = input("Введите любую фразу: ").split()
for i in range(len(n)):
    if len(list(n[i])) > 10:
        m = list(n[i])
        n[i] = "".join(m[:10])

for k, i in enumerate(n):
    print(k + 1, i)
