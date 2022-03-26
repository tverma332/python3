# shutil.copyfile(src , dest) = Copy only data but not file permissions

import shutil

src = '/home/server/ssh.py'
dest = '/home/server/ssh_backup.py'

shutil.copyfile(src , dest)
