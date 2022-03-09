# working with text files 
Python provides inbuilt functions for creating, writing and reading files. There are two types of files that can be handled in python, normal text files and binary files (written in binary language, 0s and 1s).

1. `Text files` : In this type of file, Each line of text is terminated with a special character called EOL (End of Line), which is the new line character (‘\n’) in python by default.

2. `Binary files` : In this type of file, there is no terminator for a line and the data is stored after converting it into machine understandable binary language

## File Access Modes 

Access modes govern the type of operations possible in the opened file. It refers to how the file will be used once its opened. These modes also define the location of the File Handle in the file. File handle is like a cursor, which defines from where the data has to be read or written in the file. There are 6 access modes in python.

1. `Read Only (‘r’)` : Open text file for reading. The handle is positioned at the beginning of the file. If the file does not exists, raises I/O error. This is also the default mode in which file is opened.

2. `Read and Write (‘r+’)` : Open the file for reading and writing. The handle is positioned at the beginning of the file. Raises I/O error if the file does not exists.

3. `Write Only (‘w’)` : Open the file for writing. For existing file, the data is truncated and over-written. The handle is positioned at the beginning of the file. Creates the file if the file does not exists.

4. `Write and Read (‘w+’)` : Open the file for reading and writing. For existing file, data is truncated and over-written. The handle is positioned at the beginning of the file.

5. `Append Only (‘a’)` : Open the file for writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.

6. `Append and Read (‘a+’)` : Open the file for reading and writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data

## Opening a File 

It is done using the open( ) function. No module is required to be imported for this function.

Syntax :
`File_object = open(r"File_Name","Access_Mode")`


```py
# Open function to open the file "MyFile1.txt" 
# (same directory) in append mode and

fo = open("MyFile.txt","a")
```

## Closing a File 


close() function closes the file and frees the memory space acquired by that file. It is used at the time when the file is no longer needed or if it is to be opened in a different file mode

Syntax : 
`File_object.close()`

```py
# Opening and Closing a file "MyFile.txt"
# for object name fo

fo = open("MyFile.txt","a")
fo.close()
```

## Writing to a file 

There are two ways to write in a file.

1. `write()` : Inserts the string str1 in a single line in the text file

Syntax : 
`File_object.write(str1)`

```py
fo = open ("random" , "w")

fo.write("This is random text file\n")
fo.write("This is second line")

fo.close()
```

2. `writelines()` : For a list of string elements, each string is inserted in the text file.Used to insert multiple strings at a single time

Syntax : `File_object.writelines(L) for L = [str1, str2, str3]`

```py
my_content = ["This is date-1\n" , "This is data-2\n" , "This is date-3"]
fo = open("random.txt" , "w")

fo.writelines(my_content)
fo.close()
```

## Appending to a file 

It will add new data not overwrite , means when you append a data that data will be inserted at the end i.e after existing data
<br>

`Use access mode = "a"`

```py
fo =open("random.txt" , "a")

fo.write("This is second line\n")

fo.close()
```

## Reading from a file

There are three ways to read data from a text file.

1. `read()` : Returns the read bytes in form of a string. Reads n bytes, if no n specified, reads the entire file

Syntax : `File_object.read(n)`

```py
fo = open("random.txt" , "r")

print(fo.read())

fo.close()
```

2. `readline()` : Reads a line of the file and returns in form of a string

Syntax : `File_object.readline()`

```py
fo = open("random.txt" , "r")

print(fo.readline()) # read first line
print(fo.readline()) # read second line
fo.close()
```

3. `readlines()` : Reads all the lines and return them as each line a string element in a list

Syntax : `File_object.readlines()`

```py
fo = open("random.txt" , "r")

x = fo.readlines()
fo.close()

print(x)
```