# shutil.copy2(src , dest) = Copy data as well as the metadata

import shutil

src = '/home/server/ssh.py'
dest = '/home/server/ssh_backup.py'

shutil.copy2(src , dest)