# subprocess module
* Default module in python
* Used to execute operating system commands
* The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes

`NOTE` : Before this we had os.system("cmd") to run operating system commands but the problem with that command was that we couldn't able to store output of command in variable instead we get only 0 = sucess | 1 = not success only , it was drawback of os.system("cmd") so we will be using subprocess module wherever we need the output of the command to be saved in variable.

**Syntax :**
```py
import subprocess

sp = subprocess.Popen(cmd , shell = True/False , stdout = subprocess.PIPE , stderr = subprocess.PIPE , universal_newlines = True)
```

**Parameters :**

`stdout` = Value of output obtained from standard output stream.

`stderr` = Value of error obtained(if any) from standard error stream.

`shell` = boolean parameter.If True the commands get executed through a new shell environment, and if False python will not open new shell terminal simply it will run with python itself which is more fast and efficient.

`universal_newlines` = Boolean parameter.If true files containing stdout and stderr are opened in universal newline mode. By default you'll be get outpur as binary to convert that into string we use this parameter

![](/Modules-in-python/subprocess/img/subprocess.png)