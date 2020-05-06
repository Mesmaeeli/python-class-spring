import tkinter as tk



def change1():
   if s2.get() == '1':
      lb1.config(background = 'red')
   elif s2.get() == '2':
      lb1.config(background = 'blue')
   elif s2.get() == '3':
      lb1.config(background = 'yellow')
   else:
      lb1.config(background = 'black')
      
win = tk.Tk()
lb1 = tk.Label(win,text = 'class python')
btn1 = tk.Button(win,text = 'change color',command = change1)


s1 = tk.StringVar()
s2 = tk.StringVar()

r1 = tk.Radiobutton(win,text = 'red',variable = s2, value = 1)
r2 = tk.Radiobutton(win,text = 'blue',variable = s2, value = 2)
r3 = tk.Radiobutton(win,text = 'yellow',variable = s2, value = 3)


lb1.pack()
btn1.pack()

r1.pack()
r2.pack()
r3.pack()




