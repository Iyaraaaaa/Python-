Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
... def personal():
... 
...     name = input("Enter name is : ")
...     age = int(input("Enter Your Age :"))
... 
...     
>>> print("Your name is:" , name)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print("Your name is:" , name)
NameError: name 'name' is not defined
>>> 
>>> def personal():
... 
...     name = input("Enter name is : ")
...     age = int(input("Enter Your Age :"))
...     print("Your name is:" , name)
...     print("Your Age is:" , age)
... 
...     
>>> personal()
Enter name is : Iyara
Enter Your Age :22
Your name is: Iyara
Your Age is: 22
>>> 
>>> 
