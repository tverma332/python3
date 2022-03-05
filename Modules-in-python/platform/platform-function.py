import platform # Importing platform Module

# 1) node() = Returns the computer's network name (which may not be fully qualified)

print(platform.node())

# 2) machine() = Returns the machine type, e.g. 'i386'

print(platform.machine())

# 3) platform() = Returns a single string identifying the underlying platform with as much useful information as possible (but no more :)

print(platform.platform())

# 4) processor() = Returns the (true) processor name, e.g. 'amdk6'

print(platform.processor())

# 5) system() = Returns the system/OS name, e.g. 'Linux', 'Windows' or 'Java'

print(platform.system())

# 6) architecture() = Returns info about the architecture

print(platform.architecture())

# 7) uname() =  Returns a tuple of strings (system, node, release, version, machine, processor) identifying the underlying platform

print(platform.uname())

# 8) version() = Returns the system's release version, e.g. '#3 on degas'

print(platform.version())

# 9) python_version() = Returns the Python version as string 'major.minor.patchlevel'

print(platform.python_version())