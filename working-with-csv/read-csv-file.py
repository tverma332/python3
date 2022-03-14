# 1) Using csv Module
'''
import csv
req_file = "C:\\Users\\DELL\\OneDrive\\Desktop\\demo\\my.csv"

fo = open(req_file , "r")
content = csv.reader(fo,delimiter = ',')

for x in content:
	print(x)

fo.close()

'''

# 2) Using without CSV

req_file = "C:\\Users\\DELL\\OneDrive\\Desktop\\demo\\my.csv"

fo = open(req_file , "r")
content = fo.readlines()
fo.close()

for x in content:
	print(x.strip("\n").split(","))