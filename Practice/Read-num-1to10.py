# LEC 35 : Read a number between 1-10 and display it in words

'''

# METHOD 1 --------------------------------------------------------------------------

num = eval(input("Enter your number: "))

if num==1:
	print("one")
elif num==2:
	print("two")
elif num==3:
	print("three")
elif num==4:
	print("four")
elif num==5:
	print("five")
elif num==6:
	print("six")
elif num==7:
	print("seven")
elif num==8:
	print("eight")
elif num==9:
	print("nine")
elif num==10:
	print("Ten")
else:
	print("Please enter the number between range 1-10")

'''

'''

# METHOD 2  --------------------------------------------------------------------------

num = eval(input("Enter your number between 1-10: "))

if num not in [1,2,3,4,5,6,7,8,9,10]:
	print("Please enter the number between range 1-10")
else:
	if num==1:
		print("one")
	elif num==2:
		print("two")
	elif num==3:
		print("three")
	elif num==4:
		print("four")
	elif num==5:
		print("five")
	elif num==6:
		print("six")
	elif num==7:
		print("seven")
	elif num==8:
		print("eight")
	elif num==9:
		print("nine")
	else:
		print("Ten")

'''

# METHOD 3 (Dictionary Method) --------------------------------------------------------------------------

num = eval(input("Enter number between 1 to 3: "))
dictio = {1:"one",2:"two",3:"three"}

if num in [1,2,3]:
	print(dictio[num]) 
else:
	print("Please enter the number between 1-3")