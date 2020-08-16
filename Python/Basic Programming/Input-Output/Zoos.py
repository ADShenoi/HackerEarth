lst = [char for char in input()]
z_count = lst.count("z")
o_count = lst.count("o")
print("Yes" if z_count*2 == o_count and z_count+o_count <= 20 else "No")    