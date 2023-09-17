
import datetime

import os
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import mysql.connector as mysql
from PIL import ImageTk,Image


root = Tk()
img1 = Image.open("folder_image.jpg")
img = ImageTk.PhotoImage(img1)
folders = {}#{"Images":['jpeg', 'jpg', 'png', 'heic', 'gif','svg','psd','ps','ico','ai','bmp','tif','tiff']}
def FOLDER():
        Formats = [ 
        ['Images','jpeg', 'jpg', 'png', 'heic', 'gif','svg','psd','ps','ico','ai','bmp','tif','tiff'],
        ['Programs','html', 'sql', 'js','java'],
        ['PyPrograms','py'],
        ['Videos','mp4', 'mov'],
        ['Audio','mp3', 'wav', 'm4a','aif','cda','mid','midi','mpa','ogg','wma','wpl'],
        ['PDFs','pdf'],
        ['Docs','docx'],
        ['Presentations','pptx', 'ppt'],
        ['ZipDocs','zip', 'jar','7z','rar','arj','deb','pkg','rpm','tar','z'],
        ['Text','txt'],
        ['DiskImages','bin','dmg','iso','toast','vcd'],
        ['DataBases','csv','dat','db','dbf','log','mdb','sav','sql','tar','xml','json'],
        ['Executables','apk','bat','cgi','pl','com','exe','gadget','msi','wsf'],
        ['Misc','']]

        for i in Formats:
            folders[i[0]] = i[1:]

FOLDER()

    
def createGUI():
    root.geometry("350x350")
    root.title("Oh Soldier Prettify My Folder")
    uploadBut = Button(root, text="Upload Folder", bg="#cccccc", command=openfolder)
    uploadBut.place(x=120,y=250)
    text = Frame(root, height=50,width=300)#*****************
    imageFrame = Frame(root,height=128,width=128)
    imageFrame.place(x=100,y=70)
    text.place(x=25,y=10)
    font = ("Comic Sans MS", 20, "bold")
    warmWelcome = Label(text, text="Clean Your Folder!",font=font)
    warmWelcome.place(x=50,y=10)
    
    imgLabel = Label(imageFrame, image=img)
    imgLabel.place(x=0,y=0)




def cleanItAsap(folderPath):
    if folderPath != '':
        os.chdir(folderPath)
        items = os.listdir()
        if len(items) != 0 :
                # messagebox.askyesno("Proceed", f"{root.folderPath}\nIs the desitination Folder correct?")
            for i in items:
                if not os.path.isdir(i):
                    ext = i.split(".")[-1].lower()
                    for k in folders:
                        if ext in folders[k] and k != 'misc':
                            try:
                                os.mkdir(k)
                            except:
                                pass
                            try:
                                os.rename(i, k+'/'+i)
                            except:
                                pass

                        if ext not in [k for i in list(folders.values()) for k in i]:
                            try:
                                os.mkdir("Misc")
                            except:
                                pass
                            try:
                                # os.rename(i, k+'/'+i)
                                os.rename(i, "Misc"+'/'+i)
                            except:
                                # print(e)
                                pass
            else :
                messagebox.showinfo("Successful",f"The Folder is now clean 🙌")

        elif len(items)==0:
            messagebox.showerror("ERROR","Folder is Empty")
        else:
            messagebox.showinfo("Cancelled", "Cancelled on the behalf of user")
    else:
        # messagebox.showerror("ERROR","Enter Valid Path")
        messagebox.showinfo("Cancelled", "Cancelled on the behalf of user")
                        

def openfolder():
    folderPath = askdirectory()
    cleanItAsap(folderPath)


            
createGUI()

    
root.mainloop()