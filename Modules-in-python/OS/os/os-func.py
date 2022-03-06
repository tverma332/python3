import os # importing os module

# 1) getcwd() = Print current working directory

print(os.getcwd())

# 2) chdir("path") = Change the current working dir to the specified path

print(os.chdir("c:\\users"))

# 3) listdir("path") = Return the list of dir & files present in specified path and by default gives list of file & dir of current path

print(os.listdir("c:\\users"))

# 4) mkdir("path") = Create a dir in specified path (if not provided then in current path)

print(os.mkdir(r"C:\\Users\\DELL\\OneDrive\\Desktop\\demo\\testdir"))

# 5) makedirs("path") = Recursive creation of directories

print(os.makedirs("C:\\Users\\DELL\\OneDrive\\Desktop\\demo\\testdir\\dir1\\dir11"))

# 6) rmdir("path") = Remove a dir from specified path

print(os.rmdir("C:\\Users\\DELL\\OneDrive\\Desktop\\demo\\testdir\\dir1\\dir11"))

# 7) rename("src_path","dest_path") = Rename the dir or file

print(os.rename("C:\\Users\\DELL\\OneDrive\\Desktop\\demo\\testdir","C:\\Users\\DELL\\OneDrive\\Desktop\\demo\\examdir"))

# 8) remove("path") = Remove a file form specified path

print(os.remove("C:\\Users\\DELL\\OneDrive\\Desktop\\demo\\examdir\\file.txt"))
