# Used to create a dictionary with required keys

my_dict={"two",1,4.4}
my_new_dict=dict.fromkeys(my_dict)
print(my_new_dict)

# Adding values to keys
my_new_dict[1.4]="one point four"
my_new_dict[1]="one"
my_new_dict["two"]=2
print(my_new_dict)