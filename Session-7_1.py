Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> a = np.array([1,2,4])
>>> a.shape
(3,)
>>> a.dim
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.dim
AttributeError: 'numpy.ndarray' object has no attribute 'dim'
>>> a.ndim
1
>>> b = a[np.newaxis,:]
>>> b
array([[1, 2, 4]])
>>> a
array([1, 2, 4])
>>> b.shape
(1, 3)
>>> c = a[:,np.newaxis]
>>> c
array([[1],
       [2],
       [4]])
>>> c.shape
(3, 1)
>>> d = a[np.newaxis,np.newaxis,:]
>>> d
array([[[1, 2, 4]]])
>>> d.shape
(1, 1, 3)
>>> e = np.array([1,2,3,5,6,7,8,9,10,11,12])
>>> e.shape
(11,)
>>> e = np.array([1,2,3,5,6,7,8,9,10,11,12,13])
>>> e.shape
(12,)
>>> e.reshape(2,2,3)
array([[[ 1,  2,  3],
        [ 5,  6,  7]],

       [[ 8,  9, 10],
        [11, 12, 13]]])
>>> b
array([[1, 2, 4]])
>>> b.shape
(1, 3)
>>> b1 = b.squeeze()
>>> b1
array([1, 2, 4])
>>> b1.shape
(3,)
>>> e.shape
(12,)
>>> d.shape
(1, 1, 3)
>>> sum([1,2,4,7,8])
22
>>> a = np.array([[3,4,7],[6,2,8]])
>>> a
array([[3, 4, 7],
       [6, 2, 8]])
>>> np.sum(a)
30
>>> a.shape
(2, 3)
>>> a
array([[3, 4, 7],
       [6, 2, 8]])
>>> np.sum(a,axis = 0)
array([ 9,  6, 15])
>>> np.sum(a,axis = 1)
array([14, 16])
>>> b = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
>>> b.reshape(2,2,3)
array([[[ 1,  2,  3],
        [ 4,  5,  6]],

       [[ 7,  8,  9],
        [10, 11, 12]]])
>>> np.sum(b,axis = 0)
78
>>> b
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])
>>> b = b.reshape(2,2,3)
>>> b
array([[[ 1,  2,  3],
        [ 4,  5,  6]],

       [[ 7,  8,  9],
        [10, 11, 12]]])
>>> np.sum(b,axis = 0)
array([[ 8, 10, 12],
       [14, 16, 18]])
>>> np.sum(b,axis = 1)
array([[ 5,  7,  9],
       [17, 19, 21]])
>>> np.sum(b,axis = 2)
array([[ 6, 15],
       [24, 33]])
>>> np.sum(b,axis = -1)
array([[ 6, 15],
       [24, 33]])
>>> b
array([[[ 1,  2,  3],
        [ 4,  5,  6]],

       [[ 7,  8,  9],
        [10, 11, 12]]])
>>> b.min()
1
>>> b.max()
12
>>> b.min(axis = -1)
array([[ 1,  4],
       [ 7, 10]])
>>> b.min(axis = -2)
array([[1, 2, 3],
       [7, 8, 9]])
>>> b.max(axis = 0)
array([[ 7,  8,  9],
       [10, 11, 12]])
>>> b.argmin()
0
>>> b
array([[[ 1,  2,  3],
        [ 4,  5,  6]],

       [[ 7,  8,  9],
        [10, 11, 12]]])
>>> b.argmax()
11
>>> b.mean()
6.5
>>> b.mean(axis = 0)
array([[4., 5., 6.],
       [7., 8., 9.]])
>>> b.mean(axis = 1)
array([[ 2.5,  3.5,  4.5],
       [ 8.5,  9.5, 10.5]])
>>> b.mean(axis = -1)
array([[ 2.,  5.],
       [ 8., 11.]])
>>> b.std()
3.452052529534663
>>> b.std(axis = -1)
array([[0.81649658, 0.81649658],
       [0.81649658, 0.81649658]])
>>> b.var()
11.916666666666666
>>> b.var(axis = 1)
array([[2.25, 2.25, 2.25],
       [2.25, 2.25, 2.25]])
>>> e = np.array([[1,5,3],[9,2,1],[0,8,10]])
>>> e
array([[ 1,  5,  3],
       [ 9,  2,  1],
       [ 0,  8, 10]])
>>> e.clip(3,5)
array([[3, 5, 3],
       [5, 3, 3],
       [3, 5, 5]])
>>> e = np.array([[1,5,3],[9,4,1],[0,8,10]])
>>> e.clip(3,5)
array([[3, 5, 3],
       [5, 4, 3],
       [3, 5, 5]])
>>> e.ptp()
10
>>> e
array([[ 1,  5,  3],
       [ 9,  4,  1],
       [ 0,  8, 10]])
>>> e.max()
10
>>> e.min()
0
>>> import random
>>> a = np.array([1.3,5.1,2.2,7.8])
>>> a.round()
array([1., 5., 2., 8.])
>>> a = np.array([1.5,5.5,2.5,6.5])
>>> a.round()
array([2., 6., 2., 6.])
>>> b = np.array([1.35,2.45,5.85,6.15])
>>> b.round(decimals = 1)
array([1.4, 2.4, 5.8, 6.2])
>>> a1 = np.array([6,3,6,9])

>>> a1
array([6, 3, 6, 9])
>>> range(10)
range(0, 10)
>>> np.arange(10)
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> a = np.arange(10)
>>> a.shape
(10,)
>>> a1 = np.arange(2,10)
>>> a1
array([2, 3, 4, 5, 6, 7, 8, 9])
>>> a2 = np.arange(0,100,6)
>>> a2
array([ 0,  6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96])
>>> x = np.arange(0,2 * np.pi,np.pi/4)
>>> x
array([0.        , 0.78539816, 1.57079633, 2.35619449, 3.14159265,
       3.92699082, 4.71238898, 5.49778714])
>>> np.ones((2,3))
array([[1., 1., 1.],
       [1., 1., 1.]])
>>> np.zeros((4,5))
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])
>>> np.identity(5)
array([[1., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0.],
       [0., 0., 1., 0., 0.],
       [0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 1.]])
>>> np.identity(3)
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
>>> np.empty((2,3))
array([[1., 1., 1.],
       [1., 1., 1.]])
>>> a = np.empty((2,3))
>>> a
array([[1., 1., 1.],
       [1., 1., 1.]])
>>> a = np.linspace(0,100,10)
>>> a
array([  0.        ,  11.11111111,  22.22222222,  33.33333333,
        44.44444444,  55.55555556,  66.66666667,  77.77777778,
        88.88888889, 100.        ])
>>> x = np.linspace(0,2* np.pi,10)
>>> x
array([0.        , 0.6981317 , 1.3962634 , 2.0943951 , 2.7925268 ,
       3.4906585 , 4.1887902 , 4.88692191, 5.58505361, 6.28318531])
>>> a = np.logspace(0,1,5)
>>> a
array([ 1.        ,  1.77827941,  3.16227766,  5.62341325, 10.        ])
>>> b = np.logspace(0,1,5,base = 2)
>>> b
array([1.        , 1.18920712, 1.41421356, 1.68179283, 2.        ])
>>> np.hypot(3,4)
5.0
>>> a = np.array([[5,4,2]])
>>> b = np.array([[9,0],[1,7],[4,6]])
>>> np.cross(a,b)
array([[  0,  18, -36],
       [-14,   2,  31],
       [-12,   8,  14]])
>>> a = np.array([5,4,2])
>>> b = np.array([9,0,6])
>>> np.dot(a,b)
57
>>> x = np.linspace(0,2* np.pi,10)
>>> x
array([0.        , 0.6981317 , 1.3962634 , 2.0943951 , 2.7925268 ,
       3.4906585 , 4.1887902 , 4.88692191, 5.58505361, 6.28318531])
>>> np.sin(x)
array([ 0.00000000e+00,  6.42787610e-01,  9.84807753e-01,  8.66025404e-01,
        3.42020143e-01, -3.42020143e-01, -8.66025404e-01, -9.84807753e-01,
       -6.42787610e-01, -2.44929360e-16])
>>> np.pi
3.141592653589793
>>> y = np.sin(x)
>>> import matplotlib.pyplot as plt
>>> x
array([0.        , 0.6981317 , 1.3962634 , 2.0943951 , 2.7925268 ,
       3.4906585 , 4.1887902 , 4.88692191, 5.58505361, 6.28318531])
>>> y
array([ 0.00000000e+00,  6.42787610e-01,  9.84807753e-01,  8.66025404e-01,
        3.42020143e-01, -3.42020143e-01, -8.66025404e-01, -9.84807753e-01,
       -6.42787610e-01, -2.44929360e-16])
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x0000026D792A80F0>]
>>> plt.show()
>>> x = np.linspace(0,2* np.pi,100)
>>> y = np.sin(x)
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x0000026D79BFA6A0>]
>>> plt.show()
>>> x = np.array([4,3,5,7])
>>> y = np.array([5,1,2])
>>> plt.plot(x,y)
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    plt.plot(x,y)
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\site-packages\matplotlib\pyplot.py", line 2811, in plot
    is not None else {}), **kwargs)
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\site-packages\matplotlib\__init__.py", line 1810, in inner
    return func(ax, *args, **kwargs)
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\site-packages\matplotlib\axes\_axes.py", line 1611, in plot
    for line in self._get_lines(*args, **kwargs):
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\site-packages\matplotlib\axes\_base.py", line 393, in _grab_next_args
    yield from self._plot_args(this, kwargs)
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\site-packages\matplotlib\axes\_base.py", line 370, in _plot_args
    x, y = self._xy_from_xy(x, y)
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\site-packages\matplotlib\axes\_base.py", line 231, in _xy_from_xy
    "have shapes {} and {}".format(x.shape, y.shape))
ValueError: x and y must have same first dimension, but have shapes (4,) and (3,)
>>> y = np.array([5,1,2,10])
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x0000026D79C5FDA0>]
>>> plt.show()
>>> x
array([4, 3, 5, 7])
>>> y
array([ 5,  1,  2, 10])
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x0000026D79ECFD30>]
>>> plt.show()
>>> x = np.linspace(0, 2* np.pi,100)
>>> y1 = np.sin(x)
>>> y2 = np.cos(x)
>>> plt.plot(x,y1,x,y2)
[<matplotlib.lines.Line2D object at 0x0000026D79F307B8>, <matplotlib.lines.Line2D object at 0x0000026D79F30940>]
>>> plt.show()
>>> plt.plot(np.sin(x))
[<matplotlib.lines.Line2D object at 0x0000026D79F93DD8>]
>>> plt.show()
>>> plt.plot(x,y,'r-^')
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    plt.plot(x,y,'r-^')
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\site-packages\matplotlib\pyplot.py", line 2811, in plot
    is not None else {}), **kwargs)
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\site-packages\matplotlib\__init__.py", line 1810, in inner
    return func(ax, *args, **kwargs)
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\site-packages\matplotlib\axes\_axes.py", line 1611, in plot
    for line in self._get_lines(*args, **kwargs):
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\site-packages\matplotlib\axes\_base.py", line 393, in _grab_next_args
    yield from self._plot_args(this, kwargs)
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\site-packages\matplotlib\axes\_base.py", line 370, in _plot_args
    x, y = self._xy_from_xy(x, y)
  File "C:\Users\esmae\AppData\Local\Programs\Python\Python36\lib\site-packages\matplotlib\axes\_base.py", line 231, in _xy_from_xy
    "have shapes {} and {}".format(x.shape, y.shape))
ValueError: x and y must have same first dimension, but have shapes (100,) and (4,)
>>> x
array([0.        , 0.06346652, 0.12693304, 0.19039955, 0.25386607,
       0.31733259, 0.38079911, 0.44426563, 0.50773215, 0.57119866,
       0.63466518, 0.6981317 , 0.76159822, 0.82506474, 0.88853126,
       0.95199777, 1.01546429, 1.07893081, 1.14239733, 1.20586385,
       1.26933037, 1.33279688, 1.3962634 , 1.45972992, 1.52319644,
       1.58666296, 1.65012947, 1.71359599, 1.77706251, 1.84052903,
       1.90399555, 1.96746207, 2.03092858, 2.0943951 , 2.15786162,
       2.22132814, 2.28479466, 2.34826118, 2.41172769, 2.47519421,
       2.53866073, 2.60212725, 2.66559377, 2.72906028, 2.7925268 ,
       2.85599332, 2.91945984, 2.98292636, 3.04639288, 3.10985939,
       3.17332591, 3.23679243, 3.30025895, 3.36372547, 3.42719199,
       3.4906585 , 3.55412502, 3.61759154, 3.68105806, 3.74452458,
       3.8079911 , 3.87145761, 3.93492413, 3.99839065, 4.06185717,
       4.12532369, 4.1887902 , 4.25225672, 4.31572324, 4.37918976,
       4.44265628, 4.5061228 , 4.56958931, 4.63305583, 4.69652235,
       4.75998887, 4.82345539, 4.88692191, 4.95038842, 5.01385494,
       5.07732146, 5.14078798, 5.2042545 , 5.26772102, 5.33118753,
       5.39465405, 5.45812057, 5.52158709, 5.58505361, 5.64852012,
       5.71198664, 5.77545316, 5.83891968, 5.9023862 , 5.96585272,
       6.02931923, 6.09278575, 6.15625227, 6.21971879, 6.28318531])
>>> y = np.sin(x)
>>> plt.plot(x,y,'r-^')
[<matplotlib.lines.Line2D object at 0x0000026D79F570B8>]
>>> plt.show()
>>> x = np.rand(200)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    x = np.rand(200)
AttributeError: module 'numpy' has no attribute 'rand'
>>> x = np.random.rand(200)
>>> x
array([0.26601894, 0.16964226, 0.7606571 , 0.41491448, 0.21063721,
       0.42535211, 0.01907442, 0.65846428, 0.30950981, 0.16416217,
       0.57147848, 0.17411538, 0.13551159, 0.35443132, 0.42148619,
       0.95953396, 0.35067314, 0.73027328, 0.06356101, 0.22804131,
       0.8441279 , 0.97703063, 0.09819024, 0.23571554, 0.58000023,
       0.07643552, 0.41941707, 0.8001898 , 0.89133137, 0.62956859,
       0.21534421, 0.80734587, 0.69030514, 0.68014844, 0.61468349,
       0.83865398, 0.53450815, 0.9491521 , 0.90687213, 0.40495266,
       0.20846066, 0.92305315, 0.07510895, 0.87565921, 0.86001211,
       0.85822703, 0.06270954, 0.20012692, 0.18820755, 0.76295577,
       0.81260804, 0.57510853, 0.00862609, 0.90228259, 0.94187944,
       0.9295537 , 0.17174631, 0.79362418, 0.76907655, 0.62904628,
       0.30088995, 0.19236736, 0.20874829, 0.89250879, 0.7416183 ,
       0.40935712, 0.89310402, 0.9528735 , 0.64551818, 0.55611996,
       0.09187272, 0.42766923, 0.76187197, 0.17027075, 0.123452  ,
       0.36820114, 0.10656193, 0.17628991, 0.93667902, 0.27159109,
       0.89473121, 0.38779133, 0.22142068, 0.02261144, 0.44343152,
       0.85864613, 0.24106004, 0.0159359 , 0.96318296, 0.87591406,
       0.43157628, 0.50777863, 0.33591184, 0.26453748, 0.70049394,
       0.13126609, 0.24613144, 0.63702713, 0.1098833 , 0.64498637,
       0.56273155, 0.2271277 , 0.11116764, 0.89312701, 0.79619875,
       0.91346993, 0.49752507, 0.62231255, 0.58907004, 0.48686179,
       0.0272822 , 0.55245568, 0.69314414, 0.72029523, 0.28228031,
       0.13747652, 0.79011902, 0.95619368, 0.81338811, 0.09803   ,
       0.73557543, 0.36819001, 0.4831571 , 0.55620167, 0.79198322,
       0.12159132, 0.8453185 , 0.76686298, 0.0090333 , 0.12258129,
       0.57437706, 0.02056882, 0.23435783, 0.51582165, 0.65864416,
       0.05640493, 0.9364497 , 0.26130432, 0.54590699, 0.43319037,
       0.42570994, 0.58223121, 0.88372093, 0.14127086, 0.61452368,
       0.30991712, 0.59487199, 0.77048285, 0.64814053, 0.36770806,
       0.16987911, 0.46484094, 0.20546855, 0.19939048, 0.6055597 ,
       0.97071729, 0.7918245 , 0.04912676, 0.33954024, 0.75560626,
       0.23562108, 0.99634465, 0.21520635, 0.66112039, 0.24631116,
       0.34650563, 0.04989661, 0.07242486, 0.39679954, 0.08779097,
       0.80218094, 0.14931075, 0.03965502, 0.99475116, 0.26829424,
       0.06440539, 0.02343206, 0.82503713, 0.26074445, 0.96995967,
       0.33308628, 0.35620265, 0.06808233, 0.02119012, 0.69562812,
       0.20061202, 0.90720059, 0.3750996 , 0.59533197, 0.04922459,
       0.65403378, 0.40107913, 0.94579127, 0.26473756, 0.21324971,
       0.25121293, 0.59180057, 0.62143013, 0.99789278, 0.31813188])
>>> y = np.random.rand(200)
>>> plt.scatter(x,y)
<matplotlib.collections.PathCollection object at 0x0000026D7A4FAD30>
>>> plt.show()
>>> x = np.linspace(0, 2* np.pi , 100)
>>> y1 = np.sin(x)
>>> y2 = np.cos(x)
>>> plt.plot(x,y1)
[<matplotlib.lines.Line2D object at 0x0000026D7A618898>]
>>> plt.plot(x,y2)
[<matplotlib.lines.Line2D object at 0x0000026D7A62B080>]
>>> plt.show()
>>> plt.figure()
<Figure size 640x480 with 0 Axes>
>>> plt.plot(x,y1)
[<matplotlib.lines.Line2D object at 0x0000026D79F30978>]
>>> plt.figure()
<Figure size 640x480 with 0 Axes>
>>> plt.plot(x,y2)
[<matplotlib.lines.Line2D object at 0x0000026D79277FD0>]
>>> plt.show()
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==
No handles with labels found to put in legend.

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==
No handles with labels found to put in legend.

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==

== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==
>>> 
== RESTART: C:/Users/esmae/AppData/Local/Programs/Python/Python36/p11s7.py ==
>>> mat
(<Figure size 640x480 with 4 Axes>, array([[<matplotlib.axes._subplots.AxesSubplot object at 0x0000016C1F329D30>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0000016C23E8CE10>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x0000016C23EC03C8>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x0000016C23EE5940>]],
      dtype=object))
>>> 
