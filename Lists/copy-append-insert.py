# 1) copy = Because of copy operation different memory address is alloted to (x) with value similar to (my_list)

my_list=[3,2,4,"python",5.6,"p"]

x=my_list.copy()
print(id(my_list),id(x),x)

# 2) append = Append/Add data to the end of the list

my_list=[3,2,4,"python",5.6,"p"]

my_list.append("hello")
print(my_list)

# 3) Insert = Insert data at the given index

my_list=[3,2,4,"python",5.6,"p"]

my_list.insert(3,"hello")
print(my_list)

'''
Difference between append and insert?
Both works as same but in append you can only add data to the end of list and in insert you can add wherever you want to add by just specifying the index value
'''