Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> Mark_1 = int(input("Enter the mark : "))
Enter the mark : 45
>>> Mark_2 = int(input("Enter the mark : "))
Enter the mark : 55
>>> Mark_3 = int(input("Enter the mark : "))
Enter the mark : 89
>>> 
>>> sum = Mark_1+Mark_2+Mark_3
>>> 
>>> avg = sum/3
>>> 
>>> if(avg >= 75):
...     grade = " A "
... elif(avg >= 65):
...     grade = " B "
... elif(avg >= 55):
...     grade = " C "
... elif(avg >= 35):
...     grade = "S"
... else:
...     grade = "F"
... 
...     
>>> print(grade)
 C 
