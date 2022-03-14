# LEC 64 : How to get header and no of rows in a csv file

# next() = method returns the current row and advances the iterator to the next row

import csv

req_file = "C:\\Users\\DELL\\OneDrive\\Desktop\\demo\\my.csv"

fo = open(req_file , "r")
content = csv.reader(fo , delimiter = ',')
header = next(content)

print("The header is : ",header)

print(f"The number of rows are : {len(list(content))}")

fo.close()