# LEC 22 : Display given string at center/left/right of a line in title format


import os
terminal_size = os.get_terminal_size().columns
my_string = input("Enter your String: ")

print(my_string.center(terminal_size).title())
print(my_string.ljust(terminal_size).title())
print(my_string.rjust(terminal_size).title())