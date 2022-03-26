import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname = '138.91.163.228' , username = 'azureuser' , password = 'Carry@minati' , port = 22)
stdin , stdout , stderr = ssh.exec_command('whoami')

print("The ouput is: ")
print(stdout.read())

print("The error is: ")
print(stderr.read())