Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def func1(n):
	print('salam')

	
>>> func1(12)
salam
>>> a = func1(12)
salam
>>> a
>>> a
>>> a
>>> a
>>> type(a)
<class 'NoneType'>
>>> def func2(n):
	return lambda a:a*n

>>> m = func2(100)
>>> m(3)
300
>>> func2(200)
<function func2.<locals>.<lambda> at 0x000001EC137B3AE8>
>>> tabe = func2(200)
>>> tabe(3)
600
>>> if =
SyntaxError: invalid syntax
>>> class people:
	""" kelas marbut be ensanha """
	first_name = ''
	last_name = ''
	age = 0
	id_number = 0

	
>>> ali = people()
>>> hasan = people()
>>> l1 = [4,3,6]
>>> type(l1)
<class 'list'>
>>> type(ali)
<class '__main__.people'>
>>> type(hasan)
<class '__main__.people'>
>>> ali.first_name
''
>>> ali.first_name = 'ALI'
>>> ali.first_name
'ALI'
>>> ali.last_name
''
>>> ali.last_name = "ALAVI"
>>> ali.last_name
'ALAVI'
>>> ali.age = 23
>>> ali.id_number = 1274820
>>> hasan.first_name
''
>>> hasattr(ali,first_name)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    hasattr(ali,first_name)
NameError: name 'first_name' is not defined
>>> def func():
	name = 12

	
>>> name
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> hasattr(ali,'first_name')
True
>>> hasattr(ali,'age')
True
>>> hasattr(ali,'major')
False
>>> ali.age
23
>>> getattr(ali,'age')
23
>>> delattr(ali,'first_name')
>>> ali.first_name
''
>>> class people:
	""" kelas marbut be ensanha """
	first_name = None
	last_name = None
	age = None
	id_number = 0

	
>>> ali = people()
>>> ali.first_name
>>> type(ali.first_name)
<class 'NoneType'>
>>> setattr(ali,'first_name','ALI')
>>> ali.first_name
'ALI'
>>> ali.major
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    ali.major
AttributeError: 'people' object has no attribute 'major'
>>> ali.major = 'GIS'
>>> ali.major
'GIS'
>>> hasan.major
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    hasan.major
AttributeError: 'people' object has no attribute 'major'
>>> 
=============================== RESTART: Shell ===============================
>>> class people:
	""" kelas marbut be ensanha """
	first_name = None
	last_name = None
	age = None
	id_number = 0

	
>>> def func(obj):
	print('salam '+ obj.first_name + ' ' + obj.last_name)

	
>>> ali = people()
>>> ali.first_name = 'ALI'
>>> ali.last_name = "ALAVI'
SyntaxError: EOL while scanning string literal
>>> ali.last_name = "ALAVI"
>>> func(ali)
salam ALI ALAVI
>>> def func(3)
SyntaxError: invalid syntax
>>> func(3)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    func(3)
  File "<pyshell#69>", line 2, in func
    print('salam '+ obj.first_name + ' ' + obj.last_name)
AttributeError: 'int' object has no attribute 'first_name'
>>> l1 = [4,2,5,9]
>>> func(l1)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    func(l1)
  File "<pyshell#69>", line 2, in func
    print('salam '+ obj.first_name + ' ' + obj.last_name)
AttributeError: 'list' object has no attribute 'first_name'
>>> class coordinate:
	x = 0
	y = 0

	
>>> p1 = coordinate()
>>> p2 = coordinate()
>>> p1.x = 3
>>> p1.y = 4
>>> p2.x = 10
>>> p2.y = 7
>>> def func1(point):
	return (point.x ** 2 + point.y ** 2)**0.5

>>> func1(p1)
5.0
>>> p1.x
3
>>> p2.x
10
>>> del(p1.x)
>>> p1.x
0
>>> p1.z
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    p1.z
AttributeError: 'coordinate' object has no attribute 'z'
>>> p1.z = 12
>>> p1.z
12
>>> p2.z
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    p2.z
AttributeError: 'coordinate' object has no attribute 'z'
>>> del(p1.z)
>>> p1.z
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    p1.z
AttributeError: 'coordinate' object has no attribute 'z'
>>> 
=============================== RESTART: Shell ===============================
>>> class coordinte:
	x = 0
	y = 0
	def show():
		print(x,y)

		
>>> p1 = coordinate()
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    p1 = coordinate()
NameError: name 'coordinate' is not defined
>>> p1 = coordinte()
>>> p1.show()
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    p1.show()
TypeError: show() takes 0 positional arguments but 1 was given
>>> class coordinte:
	x = 0
	y = 0
	def show(obj):
		print(obj.x,obj.y)

		
>>> p1 = coordinte()
>>> p1.show()
0 0
>>> def show():
	print('salam')

	
>>> show()
salam
>>> class coordinte:
	x = 0
	y = 0
	def show(obj):
		print(obj.x,obj.y)
	def fasele(obj):
		print((point.x ** 2 + point.y ** 2)**0.5)

		
>>> p1 = coordinte()
>>> p1.x = 3
>>> p1.y = 4
>>> p1.fasele(4)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    p1.fasele(4)
TypeError: fasele() takes 1 positional argument but 2 were given
>>> p1.fasele()
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    p1.fasele()
  File "<pyshell#123>", line 7, in fasele
    print((point.x ** 2 + point.y ** 2)**0.5)
NameError: name 'point' is not defined
>>> class coordinte:
	x = 0
	y = 0
	def show(obj):
		print(obj.x,obj.y)
	def fasele(obj):
		print((obj.x ** 2 + obj.y ** 2)**0.5)

		
>>> p1 = coordinte()
>>> p1.x = 3
>>> p1.y = 4
>>> p1.fasele()
5.0
>>> type(p1.fasele())
5.0
<class 'NoneType'>
>>> class coordinte:
	x = 0
	y = 0
	def show(obj):
		print(obj.x,obj.y)
	def fasele(obj):
		return((obj.x ** 2 + obj.y ** 2)**0.5)

		
>>> p1 = coordinte()
>>> p1.x = 3
>>> p1.y = 4
>>> type(p1.fasele())
<class 'float'>
>>> class time:
	hour = 0
	minute = 0
	second = 0

	
>>> t1 = time()
>>> t1.hour
0
>>> class time:
	def __init__(obj,h,m,s):
		obj.hour = h
		obj.minute = m
		obj.second = s

		
>>> t1 = time
>>> t1 = time()
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    t1 = time()
TypeError: __init__() missing 3 required positional arguments: 'h', 'm', and 's'
>>> t1 = time(3,10,57)
>>> t1.hour
3
>>> t1.minute
10
>>> t1.second
57
>>> class time:
	def __init__(obj,h,m,s):
		obj.hour = h
		obj.minute = m
		obj.second = s
	def show(obj):
		return str(obj.hour)+':'+str(obj.minute)+':'+str(obj.second)

	
>>> t1 = time(3,10,57)
>>> t1.show()
'3:10:57'
>>> class time:
	def __init__(obj,h,m,s):
		obj.hour = h
		obj.minute = m
		obj.second = s
	def show(obj,ruz):
		obj.date = ruz
		return str(obj.hour)+':'+str(obj.minute)+':'+str(obj.second)

	
>>> t1 = time(3,10,57)
>>> t1.show(3)
'3:10:57'
>>> t1.date
3
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s4.py ==
>>> t1 = time(12,34,29)
>>> t1.show(5)
'12:34:29'
>>> t1.number_of_seconds()
'45269'
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s4.py ==
>>> t1 = time(12,34,29)
>>> t1.ezafe_kardan(4,12,0)
>>> t1.hour
16
>>> t1.minute
46
>>> t1.second
29
>>> t2 = time(6:4:1)
SyntaxError: invalid syntax
>>> t2 = time(6,4,1)
>>> t1.add(t2)
Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    t1.add(t2)
AttributeError: 'time' object has no attribute 'add'
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s4.py ==
>>> t1 = time(12,34,29)
>>> t2 = time(6,4,1)
>>> t1.add(t2)
>>> t1.hour
18
>>> t1.minute
38
>>> t1.second
30
>>> t1.add(10)
Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    t1.add(10)
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s4.py", line 15, in add
    obj.hour += saate_jadid.hour
AttributeError: 'int' object has no attribute 'hour'
>>> t1.add(t2)
>>> str1 = 'ali'
>>> str2 = 'hasan'
>>> str1 + str2
'alihasan'
>>> t1 + t2
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    t1 + t2
TypeError: unsupported operand type(s) for +: 'time' and 'time'
>>> t1 + 4
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    t1 + 4
TypeError: unsupported operand type(s) for +: 'time' and 'int'
>>> l1 = [5,4,6,2]
>>> l1 + 3
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    l1 + 3
TypeError: can only concatenate list (not "int") to list
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s4.py ==
>>> t1 = time(12,34,29)
>>> t2 = time(6,4,1)
>>> t1 + t2
>>> t1.hour
18
>>> t.minute
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    t.minute
NameError: name 't' is not defined
>>> t1.minute
38
>>> t1.second
30
>>> 12 > 5
True
>>> a = 12
>>> a == 12
True
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s4.py ==
>>> t1 = time(12,34,29)
>>> t2 = time(6,4,1)
>>> t1 > t2
>>> t2 < t1
True
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s4.py ==
>>> t1 = time(12,34,29)
>>> t2 = time(6,4,1)
>>> t1 > t2
False
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s4.py ==
>>> t1 = time(12,34,29)
>>> t2 = time(6,4,1)
>>> t1 > t2
True
>>> t1 < t2
False
>>> t1
<__main__.time object at 0x0000017646C7AEF0>
>>> print(t1)
<__main__.time object at 0x0000017646C7AEF0>
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s4.py ==
>>> t1 = time(12,34,29)
>>> t1
<__main__.time object at 0x000001ADF950AEB8>
>>> print(t1)
12:34:29
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s4.py ==
>>> t1 = time(12,34,29)
>>> print(t1)
Traceback (most recent call last):
  File "<pyshell#227>", line 1, in <module>
    print(t1)
TypeError: __str__ returned non-string (type int)
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s4.py ==
>>> t1 = time(12,34,29)
>>> print(t1)
12
>>> t1
<__main__.time object at 0x00000292D3B5AE80>
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s4.py ==
>>> t1 = time(12,34,29)
>>> print(t1)
12
>>> t1
12:34:29
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s4.py ==
>>> t1 = time(12,34,29)
>>> print(t1)
12
>>> t1
Traceback (most recent call last):
  File "<pyshell#236>", line 1, in <module>
    t1
TypeError: __repr__ returned non-string (type int)
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s4.py ==
>>> l1 = [4,3,6,7]
>>> l2 = [4,2,6,8]
>>> m = zip(l1,l2)
>>> m
<zip object at 0x00000245E8801948>
>>> print(m)
<zip object at 0x00000245E8801948>
>>> l1 = [4,2,36,0]
>>> id(l1)
2499276708424
>>> l1[0] = 100
>>> l1
[100, 2, 36, 0]
>>> id(l1)
2499276708424
>>> str1 = 'salam'
>>> id(str1)
2499276810200
>>> str1[0]
's'
>>> str1[0] = 'S'
Traceback (most recent call last):
  File "<pyshell#250>", line 1, in <module>
    str1[0] = 'S'
TypeError: 'str' object does not support item assignment
>>> str1 = 'S' + str1[1:]
>>> str1
'Salam'
>>> id(str1)
2499276810312
>>> l1
[100, 2, 36, 0]
>>> l1.append(4)
>>> l1
[100, 2, 36, 0, 4]
>>> l1 = [5,3,7,8]
>>> id(l1)
2499276943496
>>> 
