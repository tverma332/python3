import subprocess
cmd = "dir" # command you wish to run
sp = subprocess.Popen(cmd , shell = True , stdout = subprocess.PIPE , stderr = subprocess.PIPE , universal_newlines = True)
rc = sp.wait()
out , err = sp.communicate()
print(f"The return code is {rc}")
print(f" OUTPUT is : \n{out}")
print(f" ERROR is : \n{err}")