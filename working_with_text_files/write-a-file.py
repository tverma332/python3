'''
# METHOD 1 =  fo.write('file','w')

fo = open ("random" , "w")

fo.write("This is random text file\n") # \n is similar to press enter to take your cursor to next line so you can write from next line the new text
fo.write("This is second line")

fo.close()
'''

# METHOD 2 = fo.writelines()

my_content = ["This is date-1\n" , "This is data-2\n" , "This is date-3"]
fo = open("random.txt" , "w")

fo.writelines(my_content)
fo.close()

# METHOD 2.x = when you don't want to add \n again and again you can use the below method

my_content = ["This is date-1" , "This is data-2" , "This is date-3"]
fo = open("random.txt" , "w")
for x in my_content:
	fo.writelines(x+"\n")
fo.close()