Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import tkinter as tk
>>> win = tk.Tk()
>>> win.resizable(True,True)
''
>>> win.resizable(False,False)
''
>>> win.resizable(False,True)
''
>>> win.resizable(True,False)
''
>>> win.resizable(True,True)
''
>>> win.maxsize(500,700)
>>> win.minsize(300,400)
>>> 
=============================== RESTART: Shell ===============================
>>> import tkinter as tk
>>> win = tk.Tk()
>>> win.geometry('500x200')
''
>>> win.resizable(False,False)
''
>>> from tkinter.filedialog import askopenfilename
>>> askopenfilename()
''
>>> name = askopenfilename()
>>> name
'C:/Users/esmae/AppData/Local/Programs/Python/Python36/5.png'
>>> name = askopenfilename(filetypes = (("Text File","*.txt"),('All Files','*.*')))
>>> name = askopenfilename(filetypes = (("Text File","*.txt")))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    name = askopenfilename(filetypes = (("Text File","*.txt")))
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\tkinter\filedialog.py", line 375, in askopenfilename
    return Open(**options).show()
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\tkinter\commondialog.py", line 43, in show
    s = w.tk.call(self.command, *w._options(self.options))
_tkinter.TclError: bad file type "*.txt", should be "typeName {extension ?extensions ...?} ?{macType ?macTypes ...?}?"
>>> name = askopenfilename(filetypes = (("Text File","*.txt"),))
>>> 
=============================== RESTART: Shell ===============================
>>> import tkinter as tk
>>> win = tk.Tk()
>>> btn1 = tk.Button(win,text = 'click here')
>>> btn1.grid(row = 0 , column = 0)
>>> btn2 = tk.Button(win,text = 'another button')
>>> btn2.grid(row = 1, column = 1)
>>> btn3 = tk.Button(win,text = 'button 3')
>>> btn3.grid(row = 4, column = 5)
>>> btn4 = tk.Button(win,text = 'button 4')
>>> btn4.grid(row = 2, column = 3)
>>> 
=============================== RESTART: Shell ===============================
>>> import tkinter as tk
>>> win = tk.Tk()
>>> btn1 = tk.Button(win,text = 'click here')
>>> btn1.place(x = 100,y = 100)
>>> btn2 = tk.Button(win,text = 'another button')
>>> btn2.place(x = 20, y = 150)
>>> btn3 = tk.Button(win,text = 'button 3')
>>> btn3.place(relx = 0.2, rely = 0.5)
>>> btn3.place(relx = 0.2, rely = 0.5, relwidth = 0.1, relheight = 0.1)
>>> btn4 = tk.Button(win,text = 'button 4')
>>> btn4.pack()
>>> btn5 = tk.Button(win,text = 'button 5')
>>> btn5.grid(row = 3,column = 4)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    btn5.grid(row = 3,column = 4)
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\tkinter\__init__.py", line 2226, in grid_configure
    + self._options(cnf, kw))
_tkinter.TclError: cannot use geometry manager grid inside . which already has slaves managed by pack
>>> btn6 = tk.Button(win,text = 'button 6')
>>> btn6.place(x=10,y = 10)
>>> 
=============================== RESTART: Shell ===============================
>>> import tkinter as tk
>>> win = tk.Tk()
>>> btn4 = tk.Button(win,text = 'button 4')
>>> btn4.place(x= 10,y=10)
>>> btn5 = tk.Button(win,text = 'button 5')
>>> btn5.grid(row = 3,column = 4)
>>> 
=============================== RESTART: Shell ===============================
>>> import tkinter as tk
>>> win = tk.Tk()
>>> def func():
	print('salam')

	
>>> win.bind('<Button-1>',func)
'2061135320008func'
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\tkinter\__init__.py", line 1705, in __call__
    return self.func(*args)
TypeError: func() takes 0 positional arguments but 1 was given

>>> def func(event):
	print('salam')

	
>>> win.bind('<Button-1>',func)
'2061124967560func'
>>> salam
salam
salam
salam
salam
salam
salam
salam
salam

>>> def func1(event):
	print('vorud be panjere')

	
>>> win.bind('<Enter>',func1)
'2061136557768func1'
>>> vorud be panjere
vorud be panjere

>>> lb1 = tk.Label(win, text = 'text event')
>>> lb1.pack()
>>> lb1.bind('<Double-Button-1>',func1)
'2061134194312func1'
>>> vorud be panjere
vorud be panjere
vorud be panjere
salam
vorud be panjere
salam
salam
vorud be panjere
salam

>>> 
>>> def func2(event):
	print(event.x,event.y)

	
>>> vorud be panjere
vorud be panjere
SyntaxError: invalid syntax
>>> win.bind('<Motion>',func2)
'2061151727496func2'
>>> vorud be panjere
4 1
4 2
6 4
7 4
9 5
9 6
10 6
10 7
11 8
15 12
16 13
17 14
18 16
20 19
22 20
23 22
26 24
29 27
30 27
31 28
31 30
33 32
33 33
34 35
38 39
39 39
40 40
42 40
47 41
50 41
51 41
54 41
58 40
62 39
68 37
69 36
71 36
72 35
73 34
74 34
75 33
77 33
78 32
79 32
81 31
82 31
83 31
86 31
88 31
90 31
92 31
93 32
94 32
95 32
96 33
97 34
99 36
101 37
101 38
101 39
102 41
103 43
103 47
102 50
101 52
100 53
98 56
98 57
97 58
97 59
96 60
94 61
92 63
91 64
91 65
90 65
89 66
89 67
88 67
87 68
86 69
85 69
85 70
84 71
83 72
82 74
81 75
80 76
80 78
79 78
79 79
79 80
78 83
78 84
78 87
78 90
78 92
79 94
79 95
81 97
81 98
83 99
85 101
86 101
87 101
88 102
vorud be panjere
4 5
6 6
vorud be panjere
430 341
vorud be panjere
104 1
104 0

>>> 
=============================== RESTART: Shell ===============================
>>> import tkinter as tk
>>> win = tk.Tk()
>>> c1 = tk.Canvas(win,bg = 'red')
>>> c1.pack()
>>> def draw_circle(event):
	x1 = event.x - 1
	y1 = event.y - 1
	x2 = event.x + 1
	y2 = event.y + 1
	c1.creat_oval(x1,y1,x2,y2,fill = 'black')

	
>>> c1.bind('<Motion>',draw_circle)
'2128462149192draw_circle'
>>> Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\tkinter\__init__.py", line 1705, in __call__
    return self.func(*args)
  File "<pyshell#88>", line 6, in draw_circle
AttributeError: 'Canvas' object has no attribute 'creat_oval'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\tkinter\__init__.py", line 1705, in __call__
    return self.func(*args)
  File "<pyshell#88>", line 6, in draw_circle
AttributeError: 'Canvas' object has no attribute 'creat_oval'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\tkinter\__init__.py", line 1705, in __call__
    return self.func(*args)
  File "<pyshell#88>", line 6, in draw_circle
AttributeError: 'Canvas' object has no attribute 'creat_oval'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\tkinter\__init__.py", line 1705, in __call__
    return self.func(*args)
  File "<pyshell#88>", line 6, in draw_circle
AttributeError: 'Canvas' object has no attribute 'creat_oval'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\tkinter\__init__.py", line 1705, in __call__
    return self.func(*args)
  File "<pyshell#88>", line 6, in draw_circle
AttributeError: 'Canvas' object has no attribute 'creat_oval'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\tkinter\__init__.py", line 1705, in __call__
    return self.func(*args)
  File "<pyshell#88>", line 6, in draw_circle
AttributeError: 'Canvas' object has no attribute 'creat_oval'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\tkinter\__init__.py", line 1705, in __call__
    return self.func(*args)
  File "<pyshell#88>", line 6, in draw_circle
AttributeError: 'Canvas' object has no attribute 'creat_oval'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\tkinter\__init__.py", line 1705, in __call__
    return self.func(*args)
  File "<pyshell#88>", line 6, in draw_circle
AttributeError: 'Canvas' object has no attribute 'creat_oval'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\tkinter\__init__.py", line 1705, in __call__
    return self.func(*args)
  File "<pyshell#88>", line 6, in draw_circle
AttributeError: 'Canvas' object has no attribute 'creat_oval'
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\tkinter\__init__.py", line 1705, in __call__
    return self.func(*args)
  File "<pyshell#88>", line 6, in draw_circle
AttributeError: 'Canvas' object has no attribute 'creat_oval'
def draw_circle(event):
	x1 = event.x - 1
	y1 = event.y - 1
	x2 = event.x + 1
	y2 = event.y + 1
	c1.create_oval(x1,y1,x2,y2,fill = 'black')

	
>>> c1.bind('<Motion>',draw_circle)
'2128459785864draw_circle'
>>> def draw_circle(event):
	x1 = event.x - 10
	y1 = event.y - 10
	x2 = event.x + 10
	y2 = event.y + 10
	c1.create_oval(x1,y1,x2,y2,fill = 'black')

	
>>> c1.bind('<Motion>',draw_circle)
'2128460911688draw_circle'
>>> 
=============================== RESTART: Shell ===============================
>>> import tkinter as tk
>>> win = tk.Tk()
>>> from tkinter import messagebox
>>> messagebox.askyesno()
True
>>> messagebox.askyesno()
False
>>> messagebox.askyesno('shoru mojadad','dobare bazi konim?')
True
>>> restart = messagebox.askyesno('shoru mojadad','dobare bazi konim?')
>>> restart
True
>>> messagebox.showwarning()
'ok'
>>> import random
>>> l1 = ['ali','mohammad','hasan','hossein']
>>> random.choice(l1)
'mohammad'
>>> random.choice(l1)
'ali'
>>> random.choice(l1)
'hasan'
>>> random.choice(l1)
'hasan'
>>> random.choice(l1)
'hossein'
>>> import os
>>> os.getcwd()
'C:\\Users\\esmae\\AppData\\Local\\Programs\\Python\\Python36'
>>> os.chdir('C:/Users/esmae/Desktop/UTech/Python Course/')
>>> os.getcwd()
'C:\\Users\\esmae\\Desktop\\UTech\\Python Course'
>>> 
=============================== RESTART: Shell ===============================
>>> import numpy
>>> 
=============================== RESTART: Shell ===============================
>>> import numpy as np
>>> a = np.array([6,3,7,8,3,8])
>>> print(a)
[6 3 7 8 3 8]
>>> l = [3,5,4,6,3,7]
>>> print(l)
[3, 5, 4, 6, 3, 7]
>>> a
array([6, 3, 7, 8, 3, 8])
>>> l1 = [3,5,6]
>>> l2 = [6,3,7]
>>> l1 + l2
[3, 5, 6, 6, 3, 7]
>>> a1 = np.array([7,3,8])
>>> a2 = np.array([9,0,1])
>>> a1 + a2
array([16,  3,  9])
>>> type(a1)
<class 'numpy.ndarray'>
>>> l1 * l2
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    l1 * l2
TypeError: can't multiply sequence by non-int of type 'list'
>>> a1 * a2
array([63,  0,  8])
>>> a1 ** a2
array([40353607,        1,        8], dtype=int32)
>>> a.dtype
dtype('int32')
>>> a
array([6, 3, 7, 8, 3, 8])
>>> a.shape
(6,)
>>> a.size
6
>>> a.ndim
1
>>> a
array([6, 3, 7, 8, 3, 8])
>>> a[0]
6
>>> a[-1]
8
>>> id(a)
1619802556576
>>> a[0] = 100
>>> a
array([100,   3,   7,   8,   3,   8])
>>> id(a)
1619802556576
>>> a[:] = 0
>>> a
array([0, 0, 0, 0, 0, 0])
>>> a.fill(13)
>>> a
array([13, 13, 13, 13, 13, 13])
>>> a.dtype
dtype('int32')
>>> a[0] = 10.6
>>> a
array([10, 13, 13, 13, 13, 13])
>>> a.fill(3.4)
>>> a
array([3, 3, 3, 3, 3, 3])
>>> a1
array([7, 3, 8])
>>> a = np.array([5,3,6,9,1,5,8,3,7,9])
>>> a[1:5]
array([3, 6, 9, 1])
>>> a[1:-7]
array([3, 6])
>>> l1
[3, 5, 6]
>>> l = [6,4,6,9,3,8,0]
>>> l[1:5:2]
[4, 9]
>>> a[0:6:2]
array([5, 6, 1])
>>> l = [[5,3],[8,4]]
>>> l
[[5, 3], [8, 4]]
>>> a2 = np.array([[5,3],[8,4]])
>>> a2
array([[5, 3],
       [8, 4]])
>>> a2.shape
(2, 2)
>>> a2 = np.array([[5,3,6],[8,4,8]])
>>> a2.shape
(2, 3)
>>> a2
array([[5, 3, 6],
       [8, 4, 8]])
>>> a2.size
6
>>> a2.ndim
2
>>> l
[[5, 3], [8, 4]]
>>> l[1][0]
8
>>> a2[1,2]
8
>>> a2
array([[5, 3, 6],
       [8, 4, 8]])
>>> a2 = np.array([5,3,6,8,4,8])
>>> a2
array([5, 3, 6, 8, 4, 8])
>>> b = a2[1:3]
>>> b
array([3, 6])
>>> b[0] = 10
>>> b
array([10,  6])
>>> a2
array([ 5, 10,  6,  8,  4,  8])
>>> a[0,6,2]
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    a[0,6,2]
IndexError: too many indices for array
>>> array([ 5, 10,  6,  8,  4,  8,8,5])
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    array([ 5, 10,  6,  8,  4,  8,8,5])
NameError: name 'array' is not defined
>>> a2 = np.array([ 5, 10,  6,  8,  4,  8,8,5])
>>> a2
array([ 5, 10,  6,  8,  4,  8,  8,  5])
>>> a[0,6,2]
Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    a[0,6,2]
IndexError: too many indices for array
>>> a[0]
5
>>> a[2]
6
>>> a[6]
8
>>> index =  [0,2,6]
>>> a[index]
array([5, 6, 8])
>>> a[[0,2,6]]
array([5, 6, 8])
>>> a[(0,2,6)]
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    a[(0,2,6)]
IndexError: too many indices for array
>>> a[[0,6,2]]
array([5, 8, 6])
>>> a
array([5, 3, 6, 9, 1, 5, 8, 3, 7, 9])
>>> a > 4
array([ True, False,  True,  True, False,  True,  True, False,  True,
        True])
>>> index = a > 4
>>> a[index]
array([5, 6, 9, 5, 8, 7, 9])
>>> a[a%2 == 0]
array([6, 8])
>>> np.where(a%2 == 0)
(array([2, 6], dtype=int64),)
>>> a
array([5, 3, 6, 9, 1, 5, 8, 3, 7, 9])
>>> a2
array([ 5, 10,  6,  8,  4,  8,  8,  5])
>>> a3 = np.array([[1,5,7],[6,4,8]])
>>> np.where(a3>4)
(array([0, 0, 1, 1], dtype=int64), array([1, 2, 0, 2], dtype=int64))
>>> a3
array([[1, 5, 7],
       [6, 4, 8]])
>>> a3.shape
(2, 3)
>>> a3.reshape(1,6)
array([[1, 5, 7, 6, 4, 8]])
>>> a3.reshape(3,2)
array([[1, 5],
       [7, 6],
       [4, 8]])
>>> a3.reshape(3,5)
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    a3.reshape(3,5)
ValueError: cannot reshape array of size 6 into shape (3,5)
>>> a3
array([[1, 5, 7],
       [6, 4, 8]])
>>> a3.transpose()
array([[1, 6],
       [5, 4],
       [7, 8]])
>>> a.T
array([5, 3, 6, 9, 1, 5, 8, 3, 7, 9])
>>> a3.T
array([[1, 6],
       [5, 4],
       [7, 8]])
>>> a4 = np.array([[12,7,4,0],[19,3,8,3],[4,2,7,9],[7,4,8,0]])
>>> a4
array([[12,  7,  4,  0],
       [19,  3,  8,  3],
       [ 4,  2,  7,  9],
       [ 7,  4,  8,  0]])
>>> a4.diagonal()
array([12,  3,  7,  0])
>>> a4.diagonal(offset = 1)
array([7, 8, 9])
>>> a4.diagonal(offset = 2)
array([4, 3])
>>> a4.diagonal(offset = 3)
array([0])
>>> a4.diagonal(offset = 100)
array([], dtype=int32)
>>> a4.diagonal(offset = -1)
array([19,  2,  8])
>>> a4.diagonal(offset = -2)
array([4, 4])
>>> a4.diagonal(offset = -3)
array([7])
>>> a5 = np.array([6.3,3,8.1,2.9])
>>> a5
array([6.3, 3. , 8.1, 2.9])
>>> a5.dtype
dtype('float64')
>>> a5 = np.array([6.3,3,8.1,2.9] , dtype = 'int32' )
>>> a5
array([6, 3, 8, 2])
>>> a6 = np.array([1+2j,6+5j,9-1j])
>>> a6.dtype
dtype('complex128')
>>> a.real
array([5, 3, 6, 9, 1, 5, 8, 3, 7, 9])
>>> a6.real
array([1., 6., 9.])
>>> a6.imag
array([ 2.,  5., -1.])
>>> a6.conj()
array([1.-2.j, 6.-5.j, 9.+1.j])
>>> a5
array([6, 3, 8, 2])
>>> a5.dtype
dtype('int32')
>>> np.asarray(a5,dtype = 'float')
array([6., 3., 8., 2.])
>>> a5
array([6, 3, 8, 2])
>>> a5.astype('float')
array([6., 3., 8., 2.])
>>> a5
array([6, 3, 8, 2])
>>> 
