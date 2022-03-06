# os.path module is sub module of os , and is used to work on paths

import os # importing os

# 1) basename("path") = It is used to return the basename of the file . This function basically return the file name from the path given

print(os.path.basename("\\home\\server"))

# 2) dirname("path") = Return everything except basename

print(os.path.dirname("\\home\\server"))

# 3) join("path_1","path_2") = Join two path (no need to add sep. manually)

print(os.path.join("\home","server"))

# 4) split("path") = split into head = dirname | tail = basename (in tuple)

print(os.path.split("C:\\Users\\DELL\\OneDrive\\Desktop\\demo\\testdir\\dir1\\dir11"))

# 5) getsize("path") = Give size in bytes

print(os.path.getsize("C:\\Users\\DELL\\OneDrive\\Desktop\\demo"))

# 6) exists("path") = check whether the specified path exists or not (True | False)

print(os.path.exists("C:\\Users\\DELL\\OneDrive\\Desktop\\demo"))

# 7) isfile("path") = check whether the specified path is file or not (True | False)

print(os.path.isfile("C:\\Users\\DELL\\OneDrive\\Desktop\\demo"))

# 8) isdir("path") = check whether the specified path is dir or not (True | False)

print(os.path.isdir("C:\\Users\\DELL\\OneDrive\\Desktop\\demo"))

# 9) islink("path") = check whether the specified path is link or not (True | False)

print(os.path.islink("C:\\Users\\DELL\\OneDrive\\Desktop\\demo"))
