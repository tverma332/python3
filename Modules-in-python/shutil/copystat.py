# shutil.copystat(src , dest) = Copy metadata only(not file content)

import shutil

src = '/home/server/ssh.py'
dest = '/home/server/ssh_backup.py'

shutil.copystat(src , dest)