Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> m1 = '[[12,43],[12,90]]'
>>> str1 = 'salam man mohammad hastam'
>>> str1.split(sep = ' ')
['salam', 'man', 'mohammad', 'hastam']
>>> m1 = m1[2:-2]
>>> m1
'12,43],[12,90'
>>> m1 = str1.split(sep = '],[')
>>> m1
['salam man mohammad hastam']
>>> m1 = '[[12,43],[12,90]]'
>>> m1 = m1[2:-2]
>>> m1 = m1.split(sep = '],[')
>>> m1
['12,43', '12,90']
>>> m1[0]
'12,43'
>>> m1[1]
'12,90'
>>> a = m1.split(sep = ',')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a = m1.split(sep = ',')
AttributeError: 'list' object has no attribute 'split'
>>> a = m1[0].split(sep = ',')
>>> a
['12', '43']
>>> a[0]
'12'
>>> a[1]
'43'
>>> a[0] = int(a[0])
>>> a[0]
12
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s3.py ==
[[2,5],[12,9]]
[[11,4],[7,8]]
[2, 5] [2, 5]
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s3.py ==
[[2,5],[12,9]]
[[2, 5], [2, 5]]
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s3.py ==
ruz: 2000
mah: 3
sal: 1
>>> days_passed
2059
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s3.py ==
ruz: 1
mah: 3
sal: 2000
>>> days_passed
61
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s3.py ==
ruz: 1
mah: 3
sal: 2001
60
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s3.py ==
>>> 
ruz: 1
mah: 3
sal: 2100
60
>>> d1 = {1: 'ali',2:'hasan',1:'mohammad'}
>>> d1
{1: 'mohammad', 2: 'hasan'}
>>> m1 = 'salam khubi?'
>>> m1.split(sep = ' ')
['salam', 'khubi?']
>>> a,b = m1.split(sep = ' ')
>>> a
'salam'
>>> b
'khubi?'
>>> c,d = 3,4
>>> a,b,c = m1.split(sep = ' ')
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a,b,c = m1.split(sep = ' ')
ValueError: not enough values to unpack (expected 3, got 2)
>>> obj1 = enumerate([12,56,3,8])
>>> obj1
<enumerate object at 0x00000217C07BABD0>
>>> r = range(10)
>>> r
range(0, 10)
>>> list(obj1)
[(0, 12), (1, 56), (2, 3), (3, 8)]
>>> l1 = list(obj1)
>>> l1
[]
>>> list(obj1)
[]
>>> obj1 = enumerate([12,56,3,8])
>>> l1 = list(obj1)
>>> l1
[(0, 12), (1, 56), (2, 3), (3, 8)]
>>> l1
[(0, 12), (1, 56), (2, 3), (3, 8)]
>>> l1[0]
(0, 12)
>>> for items in l1:
	a,b = items
	print(a)
	pritn(b)

	
0
Traceback (most recent call last):
  File "<pyshell#50>", line 4, in <module>
    pritn(b)
NameError: name 'pritn' is not defined
>>> for items in l1:
	a,b = items
	print(a)
	print(b)

	
0
12
1
56
2
3
3
8
>>> for a,b in l1:
	print(a)
	print(b)

	
0
12
1
56
2
3
3
8
>>> a =    5
>>> a
5
>>> a=5
>>> l1 = [6,4,7,9,3]
>>> reversed(l1)
<list_reverseiterator object at 0x00000217C074A6A0>
>>> list(reversed(l1))
[3, 9, 7, 4, 6]
>>> l1
[6, 4, 7, 9, 3]
>>> l2 = [5,0,12,4,23]
>>> zip(l1,l2)
<zip object at 0x00000217C07BD8C8>
>>> list(zip(l1,l2))
[(6, 5), (4, 0), (7, 12), (9, 4), (3, 23)]
>>> l1
[6, 4, 7, 9, 3]
>>> l2
[5, 0, 12, 4, 23]
>>> l3 = [6,3]
>>> list(zip(l1,l2))
[(6, 5), (4, 0), (7, 12), (9, 4), (3, 23)]
>>> list(zip(l1,l3))
[(6, 6), (4, 3)]
>>> list(zip(l1,l2,l3))
[(6, 5, 6), (4, 0, 3)]
>>> def func1():
	print('salam')

	
>>> func1()
salam
>>> print(2*2)
4
>>> def func2(num):
	print(num*2)

	
>>> func2(2)
4
>>> func2('salam')
salamsalam
>>> def func3(arg):
	""" in tabe yek adad daryaft mikonad va zarb dar 2 mikonad """
	print(num*2)

	
>>> def func3(arg):
	""" in tabe yek adad daryaft mikonad va zarb dar 2 mikonad """
	print(arg*2)

	
>>> func3(2)
4
>>> str1 = 'salam
SyntaxError: EOL while scanning string literal
>>> str2 = "salam
SyntaxError: EOL while scanning string literal
>>> str1 = 'salam\nman mohammad\nhastam'
>>> print(str1)
salam
man mohammad
hastam
>>> str3 = """salam
man mohammad
hastam"""
>>> print(str3)
salam
man mohammad
hastam
>>> str1
'salam\nman mohammad\nhastam'
>>> str3
'salam\nman mohammad\nhastam'
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s3.py ==
>>> func(2,3)
6
>>> func(2,5,6)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    func(2,5,6)
TypeError: func() takes 2 positional arguments but 3 were given
>>> func(1)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    func(1)
TypeError: func() missing 1 required positional argument: 'arg2'
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s3.py ==
>>> func(2,3)
8
>>> func(3,2)
9
>>> func(arg2 = 3,arg1 = 5)
125
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s3.py ==
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s3.py ==
>>> func(3,5)
salam
man mohammad hastam
243
>>> a = func(3,5)
salam
man mohammad hastam
243
>>> a
>>> a
>>> a
>>> a
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s3.py ==
>>> a = func(3,5)
salam
man mohammad hastam
243
>>> a
243
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s3.py ==
>>> a = func(3,5)
salam
man mohammad hastam
243
>>> a
(243, 12, 'salam')
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s3.py ==
>>> a = func(3,5)
salam
man mohammad hastam
243
>>> a
(243, 12, 'salam')
>>> a,b,c = func(3,5)
salam
man mohammad hastam
243
>>> a
243
>>> b
12
>>> c
'salam'
>>> a,b = func(3,5)
salam
man mohammad hastam
243
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    a,b = func(3,5)
ValueError: too many values to unpack (expected 2)
>>> def pos(num):
	for i in range(num)
	
SyntaxError: invalid syntax
>>> def pos(num):
	for i in range(num):
		print(i)

		
>>> pos(5)
0
1
2
3
4
>>> def dev(num1,num2):
	if (num1%num2 == 0 or num2%num1 == 0):
		return 'bakhshpazir'
	return 'gheir bakhshpazir'

>>> dev(8,2)
'bakhshpazir'
>>> dev(8,3)
'gheir bakhshpazir'
>>> def dev(num1,num2):
	if (num1%num2 == 0):
		return 'bakhshpazir'
	return 'gheir bakhshpazir'

>>> def prime(num):
	limit = int(num ** 0.5)
	for i in range(limit):
		if num % i == 0:
			return 'aval nist'
	return 'aval'

>>> l1 = [4,3,6,4]
>>> sum(l1)
17
>>> def sum1(arg):
	jam = 0
	for i in arg:
		jam += i
	return jam

>>> sum1(l1)
17
>>> def sum2(*arg):
	print(arg)

	
>>> sum2(12,5,2,6,7,3,6)
(12, 5, 2, 6, 7, 3, 6)
>>> def sum2(*arg):
	print(type(arg))


	
>>> sum2(12,5,2,6,7,3,6)
<class 'tuple'>
>>> sum2(1)
<class 'tuple'>
>>> sum2(1,6)
<class 'tuple'>
>>> def sum2(*arg):
	jam = 0
	for i in arg:
		jam += i
	return jam

>>> sum2(12,5,2,6)
25
>>> sum2(12,5,2,6,7)
32
>>> sum2(12,5)
17
>>> def sum3(arg1,*arg):
	jam = 0
	for i in arg:
		jam += i
	return arg1 * arg

>>> sum2()
0
>>> sum3()
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    sum3()
TypeError: sum3() missing 1 required positional argument: 'arg1'
>>> sum3(3)
()
>>> 3 * (4,5,6)
(4, 5, 6, 4, 5, 6, 4, 5, 6)
>>> 3*()
()
>>> l1 = [30,29,30,31,30]
>>> sum(l1)
150
>>> sum(l1[:2])
59
>>> def func(first_name, last_name):
	print('my name is '+first_name+' '+'last_name')

	
>>> func('mohmaad','esmaeeli')
my name is mohmaad last_name
>>> def func(first_name, last_name):
	print('my name is '+first_name+' '+last_name)

	
>>> func('mohmaad','esmaeeli')
my name is mohmaad esmaeeli
>>> func()
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    func()
TypeError: func() missing 2 required positional arguments: 'first_name' and 'last_name'
>>> def func(*args):
	print('my name is '+args[0]+' '+args[1])

	
>>> func('esmaeeli','mohmaad',)
my name is esmaeeli mohmaad
>>> def func1(**args):
	print(args)

	
>>> func1(name = 'mohammad',last_name = 'esmaeeli')
{'name': 'mohammad', 'last_name': 'esmaeeli'}
>>> def func1(**args):
	print('my name is '+args[name]+' '+args[last_name])

	
>>> func1(name = 'mohammad',last_name = 'esmaeeli')
Traceback (most recent call last):
  File "<pyshell#210>", line 1, in <module>
    func1(name = 'mohammad',last_name = 'esmaeeli')
  File "<pyshell#209>", line 2, in func1
    print('my name is '+args[name]+' '+args[last_name])
NameError: name 'name' is not defined
>>> def func1(**args):
	print('my name is '+args[name]+' '+args[last_name])

	
>>> func1(name = 'mohammad',last_name = 'esmaeeli')
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    func1(name = 'mohammad',last_name = 'esmaeeli')
  File "<pyshell#212>", line 2, in func1
    print('my name is '+args[name]+' '+args[last_name])
NameError: name 'name' is not defined
>>> def func1(**args):
	print(args)
	print('my name is '+args[name]+' '+args[last_name])

	
>>> func1()
{}
Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    func1()
  File "<pyshell#215>", line 3, in func1
    print('my name is '+args[name]+' '+args[last_name])
NameError: name 'name' is not defined
>>> def func1(**args):
	print(args)
	print('my name is '+args[name]+' '+args[last_name])

	
>>> func1(name = 'ali',last_name = 'hasan')
{'name': 'ali', 'last_name': 'hasan'}
Traceback (most recent call last):
  File "<pyshell#219>", line 1, in <module>
    func1(name = 'ali',last_name = 'hasan')
  File "<pyshell#218>", line 3, in func1
    print('my name is '+args[name]+' '+args[last_name])
NameError: name 'name' is not defined
>>> def func1(**args):
	print(args)

	
>>> func1(name = 'ali',last_name = 'hasan')
{'name': 'ali', 'last_name': 'hasan'}
>>> def func1(**args):
	print(args)
	print('my name is '+args['name']+' '+args['last_name'])

	
>>> func1(name = 'ali',last_name = 'hasan')
{'name': 'ali', 'last_name': 'hasan'}
my name is ali hasan
>>> func1(last_name = 'hasani',name = 'ali',)
{'last_name': 'hasani', 'name': 'ali'}
my name is ali hasani
>>> def func(num):
	result = 1
	for i in range(1,num+1):
		result *= i
	return result

>>> func(5)
120
>>> def func1(num):
	return num * func1(num-1)

>>> func1(5)
Traceback (most recent call last):
  File "<pyshell#237>", line 1, in <module>
    func1(5)
  File "<pyshell#236>", line 2, in func1
    return num * func1(num-1)
  File "<pyshell#236>", line 2, in func1
    return num * func1(num-1)
  File "<pyshell#236>", line 2, in func1
    return num * func1(num-1)
  [Previous line repeated 991 more times]
RecursionError: maximum recursion depth exceeded
>>> def func1(num):
	if num==1:
		return 1
	return num * func1(num-1)

>>> func1(4)
24
>>> (lambda arg1,arg2: arg1*arg2)(2,3)

6
>>> l1 = [1,4,2,6,3,8]
>>> l1 * 2
[1, 4, 2, 6, 3, 8, 1, 4, 2, 6, 3, 8]
>>> def func(arg):
	return arg*2

>>> map(func,l1)
<map object at 0x0000021727AEAF28>
>>> list(map(func,l1))
[2, 8, 4, 12, 6, 16]
>>> list(map(lambda x:x*3,l1))
[3, 12, 6, 18, 9, 24]
>>> def func(arg):
	if arg%2 == 0:
		return True
	return False

>>> list(filter(func,l1))
[4, 2, 6, 8]
>>> l3 = [5,7,2,6,0,1,9,2,3]
>>> list(filter(lambda x:(x%3 == 0),l3))
[6, 0, 9, 3]
>>> 
=============================== RESTART: Shell ===============================
>>> def func(arg):
	num = arg * 2
	return num

>>> func(5)
10
>>> num
Traceback (most recent call last):
  File "<pyshell#264>", line 1, in <module>
    num
NameError: name 'num' is not defined
>>> arg
Traceback (most recent call last):
  File "<pyshell#265>", line 1, in <module>
    arg
NameError: name 'arg' is not defined
>>> str1 = 5
>>> num2 = 124
>>> 
