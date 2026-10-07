a = [5, 2, 8, 1, 3]

for i in range(len(a)):
    for j in range(len(a) - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print("Sorted list:", a)                                                                                                        

