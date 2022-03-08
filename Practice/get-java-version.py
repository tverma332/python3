# LEC 60 : Find Java Version

import subprocess
cmd = 'java -version'
sp = subprocess.Popen(cmd , shell=True , stdout=subprocess.PIPE , stderr=subprocess.PIPE , universal_newlines=True)
rc = sp.wait()
o,e = sp.communicate()
if rc == 0 :
	if bool(o) == False and bool(e) == True: # even when the command was success you're getting output in error , it is not problem with your python it's compatibility with java and operating system
		print(e.splitlines()[0].split()[2].strip("\""))
else:
	print(e)