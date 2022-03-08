# LEC 59 : Find Bash version of Linux OS

import subprocess
cmd = "bash --version"
sp = subprocess.Popen(cmd , shell = True , stdout = subprocess.PIPE , stderr = subprocess.PIPE , universal_newlines = True)
rc = sp.wait()
out , err = sp.communicate()
if rc == 0 :
  print(f"Bash version is : {out.splitlines()[0].split()[3].split('(')[0]}")
else :
  print("Command was failed and error is :",err)