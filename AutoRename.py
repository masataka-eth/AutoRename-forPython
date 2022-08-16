// SPDX-License-Identifier: MIT
// Created by masataka.eth
import os
import tkinter
from tkinter import filedialog
import re
import glob

root = tkinter.Tk()
root.title('Auto Rename')
root.geometry("500x460")
root.resizable(width=False, height=False)

# global --------------------------------------
selecttext  =""
datalist =[]
targetfolder = ""

# Function ------------------------------------ 
def close_window():
    root.destroy()

def beforecheck():
    if checkvar.get() == 1:
        btn0["state"] = "normal"
        btn1["state"] = "normal"
        btn2["state"] = "normal"
        rdo1["state"] = "normal"
        rdo2["state"] = "normal"
        rdo3["state"] = "normal"
    else:
        btn0["state"] = "disable"
        btn1["state"] = "disable"
        btn2["state"] = "disable"
        rdo1["state"] = "disable"
        rdo2["state"] = "disable"
        rdo3["state"] = "disable"

def ReadInputdata():
    global selecttext
    global datalist

    try:
        typ = [('text file','*.txt')] 
        selecttext = filedialog.askopenfilename(filetypes = typ)
        if selecttext == "":
            return

        f = open(selecttext, 'r', encoding='UTF-8')
        templist = f.readlines()
        f.close()

        var0.set('Selected ListText : ' + selecttext)

        datalist.clear()
        for data in templist:
            datalist.append(data.strip())
        var2.set("")
    except:
        var2.set("Exception error occurred!")

def SelectFolder():
    try:
        global targetfolder
        dir = 'C:\\temp'
        targetfolder = filedialog.askdirectory(initialdir = dir) 
        if targetfolder == "":
            return

        var1.set('Selected Folder : ' + targetfolder)
        var2.set("")
    except:
        var2.set("Exception error occurred!")

def chgradio():
    try:
        if radiovar.get() == 2:
            rdo3_txt["state"] = "normal"
        else:
            rdo3_txt["state"] = "disable"
    except:
        var2.set("Exception error occurred!")

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def ExeOutput():
    try:
        files = sorted(glob.glob(targetfolder + "/*"), key=natural_keys)
        if len(files) != len(datalist):
            var2.set("Text list and number of files differ!")
            return
        
        extension = ""
        if radiovar.get() == 0:
            extension = ".png"
        elif radiovar.get() == 1:
            extension = ".jpeg"
        else:
            extension = "." + rdo3_txt.get()

        i = 0
        for file in files:
            print(file)
            os.rename(file, targetfolder + '/' + datalist[i] + extension)
            i+=1
        var2.set("Success Complete!")
    except:
        var2.set("Exception error occurred!")

# Control -----------------------------------
# before check
checkvar = tkinter.IntVar()
# default:value=0
checkvar.set(0)
chk = tkinter.Checkbutton(root, text='I have made a backup of the subject folder',command=beforecheck,variable=checkvar)

# 1.Select namelist text
btn0 = tkinter.Button(root, text='Select namelist text',
width = 50,
height = 2,
bg = "White",
command=ReadInputdata,
state="disable"
)
var0= tkinter.StringVar()
var0.set("")
label0 = tkinter.Label(root, textvariable = var0, font=("Yu Gothic", "10"))

# 2.Select rename folder
btn1 = tkinter.Button(root, text='Select rename folder',
width = 50,
height = 2,
bg = "White",
command=SelectFolder,
state="disable"
)
var1= tkinter.StringVar()
var1.set("")
label1 = tkinter.Label(root, textvariable = var1, font=("Yu Gothic", "10"))

# radio buttom
radiovar = tkinter.IntVar()
# default:value=0
radiovar.set(0)
rdo1 = tkinter.Radiobutton(root, value=0,variable=radiovar,command=chgradio,state="disable",text='png')
rdo2 = tkinter.Radiobutton(root, value=1,variable=radiovar,command=chgradio,state="disable",text='jpeg')
rdo3 = tkinter.Radiobutton(root, value=2,variable=radiovar,command=chgradio,state="disable",text='other >')
rdo3_txt = tkinter.Entry(width=20,state="disable")

#3.Go buttom!
btn2 = tkinter.Button(root, text='Go',
width = 50,
height = 2,
bg = "White",
command=ExeOutput,
state="disable"
)
var2= tkinter.StringVar()
var2.set("")
label2 = tkinter.Label(root, textvariable = var2, font=("Yu Gothic", "12"),foreground='red')

btn_close = tkinter.Button(root, text='Close',
width = 20,
height = 2,
bg = "White",
command = close_window
)

#parts design
start = 20
chk.place(x=20, y=start)
btn0.place(x=20, y=start + 40)
label0.place(x=20, y=start + 100)
btn1.place(x=20, y=start + 140)
label1.place(x=20, y=start + 200)
rdo1.place(x=20, y=start + 240)
rdo2.place(x=100, y=start + 240)
rdo3.place(x=180, y=start + 240)
rdo3_txt.place(x=250, y=start + 240)
btn2.place(x=20, y=start + 280)
label2.place(x=20, y=start + 340)
btn_close.place(x=325, y=400)

root.mainloop()