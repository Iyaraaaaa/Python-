import os

if os.path.exists("123.txt"):
    os.remove("123.txt")
else:
    print("File does not exist.")
