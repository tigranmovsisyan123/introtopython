a1 = ["Cookies", "Chocolate",8, True, -3, -5, "Chocolate", 8 , False, 8]
b1 = [8, True, 10, 14, "Chocolate", "Milk", "Jelly", True, False, True]
set_a = set(a1)
set_b = set(b1)
union_ab =set_a.union(set_b)
intersection_ab = set_a.intersection(set_b)
union_ab.update({"Kit-Kat","Oreo"})
print(union_ab)
new_set = union_ab | intersection_ab
if "Chocolate" in new_set:
    print(new_set)
    
new_set.discard("Oreo")  
print(new_set)