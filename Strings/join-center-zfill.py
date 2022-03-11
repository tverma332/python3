# 1) join = When you want to add something between the string letters

x = "python"
y="*".join(x) 
print(y)

# 2) center = When you want to print string anywhere in center of given (any_number)

x="python"
y=x.center(34)
print(y)

# 3) zfill = Pad a numeric string with zeros on the left, to fill a field of the given width

x="python"
print(x.zfill(9))