# LEC 93 : Transfer a file form local server to remote server and vice versa using paramiko of python

import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect( hostname = '138.91.163.228' , username = 'azureuser' , password = 'Carry@minati' , port = 22)
sftp_client = ssh.open_sftp()

# sftp_client.get('/home/azureuser/lisa' , 'xyx') # Download file form remote server to local server

sftp_client.put('practice.py' , '/home/azureuser/xyz.py') # Transfer file form local server to remote server

sftp_client.close()
ssh.close()