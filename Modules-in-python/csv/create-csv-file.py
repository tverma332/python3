# 1) writerow = write single row only
'''
import csv
req_file = "C:\\Users\\DELL\\OneDrive\\Desktop\\demo\\demo.csv"

fo = open(req_file , "w" , newline = "")

csv_writer = csv.writer(fo , delimiter = ",")
csv_writer.writerow(['S_No' , 'Name' , 'age'])
csv_writer.writerow([1 , 'john' , 21])
csv_writer.writerow([2 , 'Jeff' , 23])


fo.close()
'''

# 2) writerows = write multiple rows

import csv
req_file = r"C:\Users\DELL\OneDrive\Desktop\demo\demo.csv"

fo = open(req_file , "w" , newline = "")

csv_writer = csv.writer(fo , delimiter = ",")
my_data = [ ['S_No' , 'Name' , 'age'] , [1 , 'john' , 21] , [2 , 'Jeff' , 23]]
csv_writer.writerows(my_data)


fo.close()