Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> m1 = [[3,7],[9,1]]
>>> m2 = [[2,1],[0,2]]
>>> m3 = [[3*2 + 7*1, 3*1 + 7*2],[9*2 + 1*0, 9*1 + 1*2]]
>>> m3
[[13, 17], [18, 11]]
>>> m3 = [[3*2 + 7*0, 3*1 + 7*2],[9*2 + 1*0, 9*1 + 1*2]]
>>> m3
[[6, 17], [18, 11]]
>>> m3 = [[m1[0][0]*m2[0][0] + m1[0][1] * m2[1][0]],[]]
>>> m3
[[6], []]
>>> m1[0][0]
3
>>> m2[0][0]
2
>>> t1 = (2,3)
>>> type(t1)
<class 'tuple'>
>>> t2 = 5,6,8
>>> type(t2)
<class 'tuple'>
>>> t3 = (7)
>>> type(t3)
<class 'int'>
>>> obj1 = ('ali')
>>> type(obj1)
<class 'str'>
>>> t4 = (7,)
>>> type(t4)
<class 'tuple'>
>>> obj2 = ('ali',)
>>> type(obj2)
<class 'tuple'>
>>> t2[0]
5
>>> t2
(5, 6, 8)
>>> t2[6]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    t2[6]
IndexError: tuple index out of range
>>> t2[:2]
(5, 6)
>>> t2[-1]
8
>>> t2[2] = 100
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    t2[2] = 100
TypeError: 'tuple' object does not support item assignment
>>> t2
(5, 6, 8)
>>> t2
(5, 6, 8)
>>> t1
(2, 3)
>>> t2 + t1
(5, 6, 8, 2, 3)
>>> t2 = t2[:2] + (8)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    t2 = t2[:2] + (8)
TypeError: can only concatenate tuple (not "int") to tuple
>>> t2 = t2[:2] + (8,)
>>> t2
(5, 6, 8)
>>> t2 = t2[:2] + (100,)
>>> t2
(5, 6, 100)
>>> 'a' > 3
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    'a' > 3
TypeError: '>' not supported between instances of 'str' and 'int'
>>> 'a' + 3
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    'a' + 3
TypeError: must be str, not int
>>> 'a' + 'b'
'ab'
>>> num = 12
>>> num1 , num2 = 3,4
>>> num1
3
>>> num2
4
>>> num1 = 4
>>> num2 = 3
>>> num1 , num2 = num2 , num1
>>> num1
3
>>> num2
4
>>> t2
(5, 6, 100)
>>> 5 in t2
True
>>> 1000 in t2
False
>>> 1000 not in t2
True
>>> 5 not in t2
False
>>> del(t2)
>>> t2
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    t2
NameError: name 't2' is not defined
>>> t1
(2, 3)
>>> t1.count(2)
1
>>> t1.index(3)
1
>>> d1 = {1:'salam',10:'hi','a':[43,63,736]}
>>> type(d1)
<class 'dict'>
>>> d1[1]
'salam'
>>> d1['a']
[43, 63, 736]
>>> d1[1:10]
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    d1[1:10]
TypeError: unhashable type: 'slice'
>>> d2 = {1:1,2:2,3:3,4:4}
>>> type(d2)
<class 'dict'>
>>> d2[1:3]
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    d2[1:3]
TypeError: unhashable type: 'slice'
>>> p1 = {'name' : 'ali','last_name':'hasani','age':23}
>>> p1 = ['ali','hasani',23]
>>> p1 = {'name' : 'ali','last_name':'hasani','age':23}
>>> len(p1)
3
>>> 'ali' in p1
False
>>> 'name' in p1
True
>>> l1
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    l1
NameError: name 'l1' is not defined
>>> t1
(2, 3)
>>> t1[6]
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    t1[6]
IndexError: tuple index out of range
>>> p1[6]
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    p1[6]
KeyError: 6
>>> l1 = [6,4,6,8,2]
>>> l1[7] = 500
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    l1[7] = 500
IndexError: list assignment index out of range
>>> t1[7] = 5
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    t1[7] = 5
TypeError: 'tuple' object does not support item assignment
>>> p1[7] = 500
>>> p1
{'name': 'ali', 'last_name': 'hasani', 'age': 23, 7: 500}
>>> p1['name'] = 'hasan'
>>> p1
{'name': 'hasan', 'last_name': 'hasani', 'age': 23, 7: 500}
>>> p2 = p1
>>> p1['name'] = 'abbas'
>>> p1
{'name': 'abbas', 'last_name': 'hasani', 'age': 23, 7: 500}
>>> p2
{'name': 'abbas', 'last_name': 'hasani', 'age': 23, 7: 500}
>>> p3 = p1.copy()
>>> p3
{'name': 'abbas', 'last_name': 'hasani', 'age': 23, 7: 500}
>>> id(p1)
2747133647896
>>> id(p3)
2747134264736
>>> p1 == p3
True
>>> p1 is p3
False
>>> p1.clear()
>>> p1
{}
>>> p3.keys()
dict_keys(['name', 'last_name', 'age', 7])
>>> p3.values()
dict_values(['abbas', 'hasani', 23, 500])
>>> p3.items()
dict_items([('name', 'abbas'), ('last_name', 'hasani'), ('age', 23), (7, 500)])
>>> p3
{'name': 'abbas', 'last_name': 'hasani', 'age': 23, 7: 500}
>>> p3.pop('name')
'abbas'
>>> p3
{'last_name': 'hasani', 'age': 23, 7: 500}
>>> p3.pop(1000)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    p3.pop(1000)
KeyError: 1000
>>> p3.pop(1000,'index ro peyda nakardam')
'index ro peyda nakardam'
>>> p3
{'last_name': 'hasani', 'age': 23, 7: 500}
>>> p3.get('age')
23
>>> p3['age']
23
>>> p3.get(1000)
>>> p3
{'last_name': 'hasani', 'age': 23, 7: 500}
>>> p3.get(1000,'andis nabud')
'andis nabud'
>>> p3
{'last_name': 'hasani', 'age': 23, 7: 500}
>>> p3.setdefault('age')
23
>>> p3.setdefault(1000,'andis nabud')
'andis nabud'
>>> p3
{'last_name': 'hasani', 'age': 23, 7: 500, 1000: 'andis nabud'}
>>> p3.clear()
>>> p3
{}
>>> p4 = {}
>>> type(p4)
<class 'dict'>
>>> set1 = {12,644,7,3,7,93,7,2,15,100}
>>> type(set1)
<class 'set'>
>>> len(set1)
8
>>> set1
{2, 3, 644, 100, 7, 12, 15, 93}
>>> set2 = {1,1,1,1,1,1,1,1}
>>> len(set2)
1
>>> set2
{1}
>>> set1 + set2
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    set1 + set2
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> p3
{}
>>> p4
{}
>>> p1
{}
>>> p2
{}
>>> p1 = {'name' : 'ali','last_name':'hasani','age':23}
>>> p2 = {'ali' : 12}
>>> p1 + p2
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    p1 + p2
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> set1
{2, 3, 644, 100, 7, 12, 15, 93}
>>> set1.add(1000)
>>> set1
{2, 3, 644, 100, 7, 1000, 12, 15, 93}
>>> set1.add(1000)
>>> set1
{2, 3, 644, 100, 7, 1000, 12, 15, 93}
>>> set1.clear()
>>> set1
set()
>>> set3 = set()
>>> set3
set()
>>> set1.add(1)
>>> id(set1)
2747133894728
>>> set1.add('a')
>>> id(set1)
2747133894728
>>> set4 = {4,5,3,7,9}
>>> set4.add('salam')
>>> set4
{3, 4, 5, 7, 9, 'salam'}
>>> set4
{3, 4, 5, 7, 9, 'salam'}
>>> set1
{1, 'a'}
>>> set2 = {5,7,2,4,10}
>>> set4
{3, 4, 5, 7, 9, 'salam'}
>>> set2.intersection(set4)
{4, 5, 7}
>>> set2.union(set4)
{2, 3, 4, 5, 7, 9, 10, 'salam'}
>>> set2.difference(set4)
{2, 10}
>>> set4.difference(set2)
{9, 3, 'salam'}
>>> set4.symmetric_difference(set2)
{2, 3, 'salam', 9, 10}
>>> set5 = {10,4}
>>> set2.issubset(set5)
False
>>> set5.issubset(set2)
True
>>> set2.issuperset(set5)
True
>>> set5.issuperset(set2)
False
>>> set5.discard(10)
>>> set5
{4}
>>> set5.discard(11)
>>> set5.update('salam')
>>> set5
{4, 'm', 'a', 'l', 's'}
>>> input('yek adad varde konid')
yek adad varde konid12
'12'
>>> num = input('yek adad varde konid: ')
yek adad varde konid: 12
>>> num1 = input('esme khodetuno varde konid: ')
esme khodetuno varde konid: mohammad
>>> type(num1)
<class 'str'>
>>> num1
'mohammad'
>>> type(num)
<class 'str'>
>>> num
'12'
>>> print(num * 2)
1212
>>> '12'*2
'1212'
>>> '12'+'12'
'1212'
>>> 12*2
24
>>> int('12')
12
>>> print(int(num) * 2)
24
>>> num = int(input('yek adad varde konid: '))
yek adad varde konid: 12
>>> num
12
>>> type(num)
<class 'int'>
>>> num * 2
24
>>> num = int(input('yek adad varde konid: '))
yek adad varde konid: salam
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    num = int(input('yek adad varde konid: '))
ValueError: invalid literal for int() with base 10: 'salam'
>>> float('2.4')
2.4
>>> str(24)
'24'
>>> complex(2,5)
(2+5j)
>>> a = list()
>>> a
[]
>>> a = list('salam')
>>> a
['s', 'a', 'l', 'a', 'm']
>>> b = tuple('salam1')
>>> b
('s', 'a', 'l', 'a', 'm', '1')
>>> c = dict()
>>> c
{}
>>> c[1] = 1
>>> c
{1: 1}
>>> d = set()
>>> d
set()
>>> d = set('salam')
>>> d
{'s', 'a', 'l', 'm'}
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s2.py ==
13
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s2.py ==
 adad aval ro varde konid: 13
 adad dovom ro varde konid: 5
18
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s2.py ==
 matris aval ro varde konid: [[12,5],[8,11]]
Traceback (most recent call last):
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s2.py", line 1, in <module>
    m1 = int(input(' matris aval ro varde konid: '))
ValueError: invalid literal for int() with base 10: '[[12,5],[8,11]]'
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s2.py ==
 matris aval ro varde konid: [[12,5],[8,11]]
 matris dovom ro varde konid: []
Traceback (most recent call last):
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s2.py", line 3, in <module>
    m2 = int(input(' matris dovom ro varde konid: '))
ValueError: invalid literal for int() with base 10: '[]'
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s2.py ==
 matris aval ro varde konid: [[12,5],[8,11]]
 matris dovom ro varde konid: [[12,5],[8,11]]
[[12,5],[8,11]]
Traceback (most recent call last):
  File "C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s2.py", line 8, in <module>
    print(m3)
NameError: name 'm3' is not defined
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s2.py ==
 matris aval ro varde konid: [[12,5],[8,11]]
 matris dovom ro varde konid: [[12,5],[8,11]]
[[12,5],[8,11]]
>>> m1
'[[12,5],[8,11]]'
>>> list(m1)
['[', '[', '1', '2', ',', '5', ']', ',', '[', '8', ',', '1', '1', ']', ']']
>>> m1[2:4]
'12'
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s2.py ==
 matris aval ro varde konid: 
=============================== RESTART: Shell ===============================
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 12
positive
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: -10
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 12
positive
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: -10
positive
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 4
odd
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 3
odd
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 12
even
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 12
even
positive
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 12
even
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 13
odd
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 49
7
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 25
5
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 9
3
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 105
3
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 9
3
hich kodum
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 105
bakhshpaziri
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 12
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
Traceback (most recent call last):
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py", line 4, in <module>
    print('positive')
KeyboardInterrupt
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 15
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
positive
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 3
positive
positive
positive
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 100
100
99
98
97
96
95
94
93
92
91
90
89
88
87
86
85
84
83
82
81
80
79
78
77
76
75
74
73
72
71
70
69
68
67
66
65
64
63
62
61
60
59
58
57
56
55
54
53
52
51
50
49
48
47
46
45
44
43
42
41
40
39
38
37
36
35
34
33
32
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 9
9
Traceback (most recent call last):
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py", line 6, in <module>
    if num % 5 == 0:
NameError: name 'num' is not defined
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 9
9
8
7
6
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 12
12
11
10
9
8
7
6
5
4
3
2
1
halghe tamum shod
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 12
12
11
10
9
8
7
6
5
4
3
2
1
halghe tamum shod
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 12
12
11
10
9
8
7
6
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 7
7
6
5
4
3
2
1
halghe tamum shod
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 12
12
11
10
9
7
6
5
4
3
2
1
halghe tamum shod
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 12
12
11
10
9
done
>>> 
== RESTART: C:\Users\esmae\AppData\Local\Programs\Python\Python36\p11s2.py ==
yek adad vared konid: 12
>>> l1 = [3,2,5,3,8,2]
>>> for var in l1:
	print(var)

	
3
2
5
3
8
2
>>> str1 = 'salam donya'
>>> for char in str1:
	print(char)

	
s
a
l
a
m
 
d
o
n
y
a
>>> for char in str1:
	if char != 'a':
		print(char)

		
s
l
m
 
d
o
n
y
>>> for char in str1:
	print(char + '12')

	
s12
a12
l12
a12
m12
 12
d12
o12
n12
y12
a12
>>> len(str1)
11
>>> num = 4
>>> for i in [1,1,1]:
	num = num * num

	
>>> num
65536
>>> 4*4
16
>>> 16*16
256
>>> 256*256
65536
>>> for i in [1,1,1]:
	num = num * 4

	
>>> num
4194304
>>> num = 4
>>> for i in [1,1,1]:
	num = num * 4

	
>>> num
256
>>> range(3)
range(0, 3)
>>> for sub in range(3):
	print(sub)

	
0
1
2
>>> for i in range(3,10):
	print(i)

	
3
4
5
6
7
8
9
>>> for i in range(3,10,2):
	print(i)

	
3
5
7
9
>>> type(range(10))
<class 'range'>
>>> num = 4
>>> for i in range(3):
	num = num * 4

	
>>> num
256
>>> months = [31,28,31,30,31,30,31,30,31,30,31,30]
>>> m = 3
>>> result = 0
>>> for i in month[:m-1]:
	result = result + m

	
Traceback (most recent call last):
  File "<pyshell#258>", line 1, in <module>
    for i in month[:m-1]:
NameError: name 'month' is not defined
>>> for i in months[:m-1]:
	result = result + m

	
>>> result
6
>>> for i in months[:m-1]:
	result = result + i

	
>>> result
65
>>> result = 0
>>> 
>>> for i in months[:m-1]:
	result = result + i

	
>>> result
59
>>> months
[31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
>>> d = 5
>>> result + d
64
>>> 
