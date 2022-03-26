# shutil.copymode(src , dest) = Copy file permissions only (not content)

import shutil

src = '/home/server/ssh.py'
dest = '/home/server/ssh_backup.py'

shutil.copymode(src , dest)