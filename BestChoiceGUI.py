#!/usr/local/bin/python
from Tkinter import *
import tkMessageBox
janela=Tk() 
janela.title("Cheaper one.")
janela.resizable(width=False, height=False)
def reset():
	lp1.delete(0,END)
	lp2.delete(0,END)
	ls1.delete(0,END)
	ls2.delete(0,END)
	lq1.delete(0,END)
	lq2.delete(0,END)
def calc():
	global lp1,lp2,ls1,ls2,lq1,lq2
	lp1f=lp1.get()
	lp2f=lp2.get()
	ls1f=ls1.get()
	ls2f=ls2.get()
	lq1f=lq1.get()
	lq2f=lq2.get()
	try:
		lq1f= float(lq1f)
		lq2f= float(lq2f)
		ls1f= float(ls1f)
		ls2f= float(ls2f)
		lp1f= float(lp1f)
		lp2f= float(lp2f)
	except:
		tkMessageBox.showerror("Erro","Enter only numbers! use only (.) instead of (,)")
		janela.mainloop() 
	if lq1f == 0:
		tkMessageBox.showerror("Erro","You can't enter 0")
		janela.mainloop() 
	if lq2f == 0:
		tkMessageBox.showerror("Erro","You can't enter 0")
		janela.mainloop() 
	if ls1f == 0:
		tkMessageBox.showerror("Erro","You can't enter 0")
		janela.mainloop() 
	if ls1f == 0:
		tkMessageBox.showerror("Erro","You can't enter 0")
		janela.mainloop() 
	if lp1f == 0:
		tkMessageBox.showerror("Erro","You can't enter 0")
		janela.mainloop() 
	if lp2f == 0:
		tkMessageBox.showerror("Erro","You can't enter 0")
		janela.mainloop() 
	p1=lp1f/(ls1f*lq1f)
	p2=lp2f/(ls2f*lq2f)
	if p2 == p1: 
		tkMessageBox.showinfo("Done","Both have the same price")
	elif p1<p2:
		r=100-((p1/p2)*100)
                r="%.2f" % r
		r=str(r)
		tkMessageBox.showinfo("Done","Product 1 is cheaper "+r+"%")
	else:
		r=100-((p2/p1)*100)
		r="%.2f" % r
		r=str(r)
		tkMessageBox.showinfo("Done","Product 2 is cheaper "+r+"%")
def duvid():
	tkMessageBox.showinfo("Help","Enter only numbers! use only (.) instead of (,) and never use only 0.")
l1=Label(janela,text="Product 1")
l1.grid(row=0,column=0)
l2=Label(janela,text="Product 2")
l2.grid(row=0,column=2)
lp=Label(janela,text="Price")
lp.grid(row=1,column=1)
ls=Label(janela,text="Volume")
ls.grid(row=2,column=1)
lq=Label(janela,text="How many itens")
lq.grid(row=3,column=1)
lp1=Entry(janela)
lp1.grid(row=1,column=0)
ls1=Entry(janela)
ls1.grid(row=2,column=0)
lq1=Entry(janela)
lq1.grid(row=3,column=0)
lp2=Entry(janela)
lp2.grid(row=1,column=2)
ls2=Entry(janela)
ls2.grid(row=2,column=2)
lq2=Entry(janela)
lq2.grid(row=3,column=2)
c=Button(janela,text="Calculate", command=calc)
c.grid(row=4,column=2)
cr=Label(janela,text="Made by: Luiz Garbin")
cr.grid(row=5, column=1)
d=Button(janela,text="Help", command=duvid)
d.grid(row=4,column=1)
res=Button(janela,text="Clear", command=reset)
res.grid(row=4,column=0)
janela.mainloop() 
