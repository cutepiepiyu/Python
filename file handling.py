"""Write Data to a file."""
f=open("security_log.txt", "w")
f.write("cyber security lab\n")
f.write("M.Sc. cyber security and cyber law\n")
f.write("This is file handling.\n")
f.close()


"""""Read data from a file."""
f=open("security_log.txt", "r")
data=f.read()
print("File content:\n", data)
f.close()


"""Append data to a file."""
f=open("security_log.txt", "a")
f.write("Appended data.\n")
f.close()


"""Read data from a file after appending."""
f=open("security_log.txt", "r")
data=f.read()
print("File content after appending:\n", data)
f.close()


"""create the file."""
f=open("cyber_security.txt", "x")
f.close()


"""r+ read and write mode."""
f=open("cyber_security.txt", "r+")
print("r+ Mode:\n", f.read())
f.write("Add data using r+ mode.")
f.close()


"""w+ write and read mode."""
f=open("cyber_security.txt", "w+")
f.write("Add data using w+ mode.")
f.seek(0)
print("w+ Mode:\n", f.read())
f.close()


"""a+ append and read mode."""
f=open("cyber_security.txt", "a+")
f.write("Add data using a+ mode.")
f.seek(0)  
"""that is why we use seek(0) to move the cursor to the beginning of the file before reading."""
print("a+ Mode:\n", f.read())
f.close()