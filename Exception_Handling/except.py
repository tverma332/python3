def main():	
	try:
		fo = open("hell.txt")
		print(fo.read())
	except Exception as e:
		print(e)
		
	
main()