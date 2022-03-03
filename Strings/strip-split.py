# 1) strip = Remove unecessay space or letters from extreme ends

x="SpamSpamBaconSpameggsSpamSpam"
print(x.strip("ampS"))  # ampS will not exist on extreme end in output

# lstrip = works only for left extreme

x="pythonp"
print(x.lstrip("p"))

# rstrip = works only for right extreme

x="pythonp"
print(x.rstrip("p")) # if nothing is provided then splitting will based on space

# 2) split = It will split string into list

x="python is easy"
print(x.split("is")) # splitting based on (is) and (is) will not included in list

# 3) partition = Partition the string into three parts using the given separator (gives tuple)

x="python is easy"
print(x.partition("is"))