Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l1=[1,2,3,"hi",4,5,"hello"]
l1 append(6)
SyntaxError: invalid syntax
l1.append(6)
l1=[1,2,3,"hi",4,5,"hello"]
l1.append(6)
print l1
SyntaxError: incomplete input
print (l1)
[1, 2, 3, 'hi', 4, 5, 'hello', 6]
l1.append(6,7)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    l1.append(6,7)
TypeError: list.append() takes exactly one argument (2 given)

[1, 2, 3, 'hi', 4, 5, 'hello', 6]l1.append(6,7)
SyntaxError: invalid syntax

[1, 2, 3, 'hi', 4, 5, 'hello', 6]l1.append(6,7)l1=[1,2,3,"hi",4,5,"hello"]
SyntaxError: invalid syntax
l1=[1,2,3,"hi",4,5,"hello"]
l1.append([6,7])
print (l1)
[1, 2, 3, 'hi', 4, 5, 'hello', [6, 7]]
l1.extend([6,7])
print (l1)
[1, 2, 3, 'hi', 4, 5, 'hello', [6, 7], 6, 7]
l1.remove([6,7])
print (l1)
[1, 2, 3, 'hi', 4, 5, 'hello', 6, 7]
l2=[1, 2, 3, 'hi', 4, 5, 'hello', 6, 7]
l2.insert(10)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    l2.insert(10)
TypeError: insert expected 2 arguments, got 1
l2.insert(10.3)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    l2.insert(10.3)
TypeError: insert expected 2 arguments, got 1
l2.insert(2,99)
l2
[1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
l2.pop(3)
3
l2
[1, 2, 99, 'hi', 4, 5, 'hello', 6, 7]
l2=[1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
l2
[1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
l2.pop(2)
99
l2
[1, 2, 3, 'hi', 4, 5, 'hello', 6, 7]
l2=[1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
l1
[1, 2, 3, 'hi', 4, 5, 'hello', 6, 7]
l2
[1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
print(l1)
[1, 2, 3, 'hi', 4, 5, 'hello', 6, 7]
l2
[1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]


print(l1+l2)
[1, 2, 3, 'hi', 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
a=l1+l2
a
[1, 2, 3, 'hi', 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
la
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    la
NameError: name 'la' is not defined. Did you mean: 'l1'?
la=a
a
[1, 2, 3, 'hi', 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
la
[1, 2, 3, 'hi', 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
a.pop(2)
3
a
[1, 2, 'hi', 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
a.remove("hi")
a
[1, 2, 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
la
[1, 2, 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
[1, 2, 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
[1, 2, 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]





















l1
[1, 2, 3, 'hi', 4, 5, 'hello', 6, 7]
l2
[1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
la
[1, 2, 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
a
[1, 2, 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
a=l1
a
[1, 2, 3, 'hi', 4, 5, 'hello', 6, 7]
la
[1, 2, 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
l1=a
l2=b
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    l2=b
NameError: name 'b' is not defined
b=l2
a=l1
c-la
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    c-la
NameError: name 'c' is not defined
la
[1, 2, 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
a
[1, 2, 3, 'hi', 4, 5, 'hello', 6, 7]
b
[1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
print(la[0:6])
[1, 2, 4, 5, 'hello', 6]
 c=la
 
SyntaxError: unexpected indent
c=la
c
[1, 2, 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]








a
[1, 2, 3, 'hi', 4, 5, 'hello', 6, 7]
b
[1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
c
[1, 2, 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
print(a+b+c)
[1, 2, 3, 'hi', 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7, 1, 2, 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
d=a+b+c
d
[1, 2, 3, 'hi', 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7, 1, 2, 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]










a
[1, 2, 3, 'hi', 4, 5, 'hello', 6, 7]
b
[1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
c
[1, 2, 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
d
[1, 2, 3, 'hi', 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7, 1, 2, 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
e
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    e
NameError: name 'e' is not defined




















>>> 

... 
>>> 

... 
>>> 
>>> 

... 
... 
>>> 

>>> 

... 
... 
>>> 

... 
... 
>>> 
>>> a
[1, 2, 3, 'hi', 4, 5, 'hello', 6, 7]
>>> b
[1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
>>> c
[1, 2, 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
>>> d
[1, 2, 3, 'hi', 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7, 1, 2, 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
>>> print(c[0:8:3])
[1, 5, 7]
>>> c
[1, 2, 4, 5, 'hello', 6, 7, 1, 2, 99, 3, 'hi', 4, 5, 'hello', 6, 7]
>>> print(c[0:8:3])
[1, 5, 7]
>>> print(c[0:18:3])
[1, 5, 7, 99, 4, 6]
print (a)
