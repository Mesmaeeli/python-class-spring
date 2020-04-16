Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = 6
>>> print(num)
6
>>> num
6
>>> num1,num2 = 3,4
>>> num1
3
>>> print(num2)
4
>>> num3 = num4 = num5 = 0
>>> print(num3)
0
>>> num4
0
>>> type(num)
<class 'int'>
>>> num6 = 1.3
>>> type(num6)
<class 'float'>
>>> num7 = 3.14567
>>> print(num7)
3.14567
>>> num8 = 4 + 6j
>>> print(num8)
(4+6j)
>>> type(num8)
<class 'complex'>
>>> b1 = True
>>> b2 = False
>>> type(b1)
<class 'bool'>
>>> if = 3
SyntaxError: invalid syntax
>>> print = 7
>>> print(4)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(4)
TypeError: 'int' object is not callable
>>> s1 = None
>>> print(s1)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(s1)
TypeError: 'int' object is not callable
>>> 
=============================== RESTART: Shell ===============================
>>> s1 = None
>>> print(s1)
None
>>> s1
>>> print(s2)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(s2)
NameError: name 's2' is not defined
>>> s2
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    s2
NameError: name 's2' is not defined
>>> str1 = 'hello world'
>>> type(str1)
<class 'str'>
>>> num1 = 5
>>> num2 = 4
>>> num1 + num2
9
>>> num1 * num2
20
>>> num2 - num1
-1
>>> num1 / num2
1.25
>>> num1 // num2
1
>>> num3 = 12
>>> num3 % num1
2
>>> 2 ** 3
8
>>> 3 ** 2
9
>>> num1 == num2
False
>>> num1 == 5
True
>>> num1 != num2
True
>>> num1 != 5
False
>>> num1 > 2
True
>>>  num1 < 1000
SyntaxError: unexpected indent
>>> num1 < 1000
True
>>> True and True
True
>>> (num1 == 5) and True
True
>>> (num1 > 6) and (num1 == 5)
False
>>> (num1 > 6) or (num1 == 5)
True
>>> (num1 > 6) or (num1 == 4)
False
>>> (num1 > 6) or (num1 == 4) or (num2 == 4)
True
>>> not True
False
>>> not False
True
>>> not (num1 > 6)
True
>>> not (num1 == 5)
False
>>> 4 & 5
4
>>> 5 | 7
7
>>> 9 | 2
11
>>> 9 ^ 2
11
>>> 9 ^ 3
10
>>> 4 >> 2
1
>>> 2 << 1
4
>>> num1 = 6
>>> num1 += 2
>>> print(num1)
8
>>> num1 *= 3
>>> num1
24
>>> num1 /= 4
>>> num1 = num1 / 4
>>> num1
1.5
>>> id(num1)
2521960028872
>>> num2 = 5
>>> id(num2)
1983152368
>>> num2 is 5
True
>>> num2 is 120
False
>>> str1 = hello
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    str1 = hello
NameError: name 'hello' is not defined
>>> str1 = 'hello world'
>>> str2 = '%^&&*#       1245asdfAZSDDF'
>>> print(str1)
hello world
>>> str1
'hello world'
>>> str1[6]
'w'
>>> str1[2]
'l'
>>> str1[11]
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    str1[11]
IndexError: string index out of range
>>> str1[3:6]
'lo '
>>> str1[3:7]
'lo w'
>>> len(str1)
11
>>> str1[10]
'd'
>>> str1[-1]
'd'
>>> str1[len(str1)-1]
'd'
>>> str1[-1]
'd'
>>> str1
'hello world'
>>> str1[-1:3]
''
>>> str1[3:-1]
'lo worl'
>>> str1[3:]
'lo world'
>>> str1[:6]
'hello '
>>> id(str1)
2522000652912
>>> str1 = 'hello'
>>> id(str1)
2521999853976
>>> 3 + 5
8
>>> 'ali' + 'salam'
'alisalam'
>>> str1.capitalize()
'Hello'
>>> str1
'hello'
>>> str1 = str1.capitalize()
>>> str1
'Hello'
>>> str1.count('l')
2
>>> str1.count('l',3)
1
>>> str1.endswith('o')
True
>>> str1.endswith('z')
False
>>> str1.find('e')
1
>>> str1
'Hello'
>>> str1.find('l')
2
>>> str1.find('z')
-1
>>> str1.index('e')
1
>>> str1.index('l')
2
>>> str1.index('z')
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    str1.index('z')
ValueError: substring not found
>>> str1.find('l',3)
3
>>> str1.lower()
'hello'
>>> str1.upper()
'HELLO'
>>> str1.isalpha()
True
>>> str1.isdigit()
False
>>> 'l' in str1
True
>>> 'z' in str1
False
>>> 'o' not in str1
False
>>> 'z' not in str1
True
>>> l1 = [12,'asgdg',4.5]
>>> type(l1)
<class 'list'>
>>> l1[2]
4.5
>>> l1[0]
12
>>> l1[:2]
[12, 'asgdg']
>>> l2 = [4,3,5,7,4,7,8]
>>> l2
[4, 3, 5, 7, 4, 7, 8]
>>> l2[2:6]
[5, 7, 4, 7]
>>> l2[-7:3]
[4, 3, 5]
>>> id(l2)
2522000651784
>>> l2[5] = 122
>>> l2
[4, 3, 5, 7, 4, 122, 8]
>>> id(l2)
2522000651784
>>> str1
'Hello'
>>> str1[2] = 'L'
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    str1[2] = 'L'
TypeError: 'str' object does not support item assignment
>>> l3 = [5,3,6,[12,12],6,9]
>>> l3[3]
[12, 12]
>>> l3[3][0]
12
>>> l3 = [5,3,6,[12,13],6,9]
>>> l3[3][0]
12
>>> l3[3][1]
13
>>> str1
'Hello'
>>> str1[:2] + 'L' + str1[3:]
'HeLlo'
>>> str1
'Hello'
>>> str1 = str1[:2] + 'L' + str1[3:]
>>> str1
'HeLlo'
>>> l3[-3][-2]
12
>>> len(l3)
6
>>> 5 in l3
True
>>> 9 in l3
True
>>> 24 not in l3
True
>>> l3 = [5,3,6,[12,13],6,9]
>>> l3[-3][-2]
12
>>> l3
[5, 3, 6, [12, 13], 6, 9]
>>> 12 in l3
False
>>> l3
[5, 3, 6, [12, 13], 6, 9]
>>> l3.append('salam')
>>> l3
[5, 3, 6, [12, 13], 6, 9, 'salam']
>>> str1
'HeLlo'
>>> l3.extend(str1)
>>> l3
[5, 3, 6, [12, 13], 6, 9, 'salam', 'H', 'e', 'L', 'l', 'o']
>>> l4 = [5,4,6,2]
>>> l3.extend(l4)
>>> l3
[5, 3, 6, [12, 13], 6, 9, 'salam', 'H', 'e', 'L', 'l', 'o', 5, 4, 6, 2]
>>> l3.insert(3,'mohammad')
>>> l3
[5, 3, 6, 'mohammad', [12, 13], 6, 9, 'salam', 'H', 'e', 'L', 'l', 'o', 5, 4, 6, 2]
>>> l3.remove(6)
>>> l3
[5, 3, 'mohammad', [12, 13], 6, 9, 'salam', 'H', 'e', 'L', 'l', 'o', 5, 4, 6, 2]
>>> l3.index(3)
1
>>> l3.count(6)
2
>>> l3.reverse()
>>> l3
[2, 6, 4, 5, 'o', 'l', 'L', 'e', 'H', 'salam', 9, 6, [12, 13], 'mohammad', 3, 5]
>>> l3.clear()
>>> l3
[]
>>> l4
[5, 4, 6, 2]
>>> l4.sort()
>>> l4
[2, 4, 5, 6]
>>> l5 = ['a',5,35,'z']
>>> l5.sort()
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    l5.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> 'a' < 5
Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    'a' < 5
TypeError: '<' not supported between instances of 'str' and 'int'
>>> l6 = ['f','a','r','e']
>>> l6.sort()
>>> l6
['a', 'e', 'f', 'r']
>>> id(l6)
2522000652104
>>> list1 = [5,4,6,8,3,7,0]
>>> list2 = list1
>>> list1[3] = 100
>>> list1
[5, 4, 6, 100, 3, 7, 0]
>>> list2
[5, 4, 6, 100, 3, 7, 0]
>>> id(list2)
2522000848776
>>> id(list1)
2522000848776
>>> list3 = list1.copy()
>>> id(list3)
2522000652232
>>> list1
[5, 4, 6, 100, 3, 7, 0]
>>> list3
[5, 4, 6, 100, 3, 7, 0]
>>> list1 == list3
True
>>> list1 is list3
False
>>> list1[3] = 7
>>> list1
[5, 4, 6, 7, 3, 7, 0]
>>> list3
[5, 4, 6, 100, 3, 7, 0]
>>> list1
[5, 4, 6, 7, 3, 7, 0]
>>> list1[2] = [67,89]
>>> list1[2]
[67, 89]
>>> list1
[5, 4, [67, 89], 7, 3, 7, 0]
>>> list1[2:3] = [23,24]
>>> list1
[5, 4, 23, 24, 7, 3, 7, 0]
>>> list1[:] = [4,5]
>>> list1
[4, 5]
>>> del(list1)
>>> list1
Traceback (most recent call last):
  File "<pyshell#218>", line 1, in <module>
    list1
NameError: name 'list1' is not defined
>>> list1 = [5, 4, 23, 24, 7, 3, 7, 0]
>>> del(list1[2])
>>> list1
[5, 4, 24, 7, 3, 7, 0]
>>> list1[2:3] = []
>>> list1

[5, 4, 7, 3, 7, 0]
>>> 
