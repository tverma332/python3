# 1) count = To count how many time a particular word & char. is appearing

x="Keep grinding keep hustling"
print(x.count("t"))

# 2) index = To get index of letter(gives the lowest index)

x="Keep grinding keep hustling"
print(x.index("t"))  # will give the lowest index value of (t)

# 3) find = To get index of letter(gives the lowest index) | Return -1 on failure.

x="Keep grinding keep hustling"
print(x.find("t"))


'''
NOTE : print(x.index("t",34)) : Search starts from index value 34 including 34
'''
