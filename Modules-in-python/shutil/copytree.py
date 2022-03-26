# shutil.copytree(src , dest) = Replicate complete dir from src to dest

import shutil

src = '/home/server/azure'
dest = '/home/server/aws'

shutil.copytree(src , dest)

# NOTE : The destination directory must not already exists 