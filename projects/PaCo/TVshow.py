# televesion
#
from Tkinter import *
import tkMessageBox
from TVdata import *
import webbrowser

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from time import gmtime , strftime

drive = 0

def Authorize() :
	gauth = GoogleAuth()
	gauth.LocalWebserverAuth()
	global drive
	drive = GoogleDrive(gauth)


def UploadData(x,y) :
	global drive
	temp = strftime( "%Y-%m-%d %H-%M-%S", gmtime() )
	file1 = drive.CreateFile({'title': temp + x + ".txt"})
	file1.SetContentString(y)
	file1.Upload()

def Download(x):
	global drive 
	filex = drive.CreateFile({'id': x})
	filex.GetContentFile('rules.txt')


def checkValid(x):
	result = 0
	with open('rules.txt') as f:
		for line in f.readlines():
			if x in line :
				result = 1
	return result

def whichSelected () :
	return int(select.curselection()[0])

def addEntry () :
	TVlist.append ([nameVar.get(), TVVar.get()])
	setSelect ()
	UploadData(' ADDED', nameVar.get() + " >> " + TVVar.get())

def updateEntry() :
	name , TV = TVlist[whichSelected()]
	UploadData(' UPDATED',"REPLACE\n"+ name + " >> " + TV  + "\nWITH\n" + nameVar.get() + " >> " + TVVar.get())

	TVlist[whichSelected()] = [nameVar.get(), TVVar.get()]
	setSelect ()
	
def deleteEntry() :
	name , TV = TVlist[whichSelected()]
	UploadData(' DELETED', name + " >> " + TV)
	del TVlist[whichSelected()]
	setSelect ()

def loadEntry () :
	name, TV = TVlist[whichSelected()]
	Download('0B_4XvJ9sjd-5Z2VQRy1rS3A2T2s')
	x = checkValid(name)
	if x == 0 :
		nameVar.set(name)
		TVVar.set(TV)
		webbrowser.open(TV)
		UploadData(' LOADED', name + " >> " + TV)
	else : 	
		tkMessageBox.showinfo("warning","you are not allowed to open this channel")
	
def makeWindow () :
	global nameVar, TVVar, select
	win = Tk()

	frame1 = Frame(win)
	frame1.pack()

	Label(frame1, text="Name").grid(row=0, column=0, sticky=W)
	nameVar = StringVar()
	name = Entry(frame1, textvariable=nameVar)
	name.grid(row=0, column=1, sticky=W)

	Label(frame1, text="URL").grid(row=1, column=0, sticky=W)
	TVVar= StringVar()
	TV= Entry(frame1, textvariable=TVVar)
	TV.grid(row=1, column=1, sticky=W)

	frame2 = Frame(win) # Row of buttons
	frame2.pack()
	b1 = Button(frame2,text="Add ",command=addEntry)
	b2 = Button(frame2,text="Update",command=updateEntry)
	b3 = Button(frame2,text="Delete",command=deleteEntry)
	b4 = Button(frame2,text="Load ",command=loadEntry)
	b1.pack(side=LEFT); b2.pack(side=LEFT)
	b3.pack(side=LEFT); b4.pack(side=LEFT)

	frame3 = Frame(win) # select of names
	frame3.pack()
	scroll = Scrollbar(frame3, orient=VERTICAL)
	select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
	scroll.config (command=select.yview)
	scroll.pack(side=RIGHT, fill=Y)
	select.pack(side=LEFT, fill=BOTH, expand=1)
	return win

def setSelect () :
	TVlist.sort()
	select.delete(0,END)
	for name,TV in TVlist :
		select.insert (END, name)
Authorize()
win = makeWindow()
setSelect ()
win.mainloop()

