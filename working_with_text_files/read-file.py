'''
# METHOD 1 = fo.read()

fo = open("random.txt" , "r")

print(fo.read())

fo.close()
'''

'''
# METHOD 2 = fo.readline()

fo = open("random.txt" , "r")

print(fo.readline()) # read first line
print(fo.readline()) # read second line
fo.close()
'''

'''
# METHOD 3 = fo.readlines()

fo = open("random.txt" , "r")

x = fo.readlines()
fo.close()

print(x)

'''

