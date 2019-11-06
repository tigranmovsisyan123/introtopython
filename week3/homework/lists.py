#Lists
a = [1, 4, 5, 7, 8, -2, 0, -1]
a_sorted = a.copy()
print(a[3], a[5])
a_sorted.sort(reverse = True)
print(a_sorted)
print(a_sorted[1:4],a_sorted[2:7])
del a_sorted[2]
del a_sorted[2]
print(a_sorted)
b = ["grapes","Potatoes","tomatoes","Orange","Lemon","Broccoli","Carrot","Sausages"]
b_sorted = b.copy()
b_sorted.sort()
c = a[1:4] + b[4:7]
print(c)