# LEC 62 : Copy the contents of a file to another file

sfile = "C:\\Users\\Automation\\Desktop\\random.txt" 
dfile = "C:\\Users\\Automation\\Desktop\\newrandom.txt"

sfo = open(sfile)
print(sfo.mode)
content = sfo.read()
sfo.close()

dfo = open(dfile , 'w')
dfo.write(content)
dfo.close()

# NOTE : Enter path as per your system