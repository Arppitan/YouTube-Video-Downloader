import os


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


resource_path('ytd.gif')
# Importing tkinter
from tkinter import *
# Importing YouTube module
# from pip._internal.models import link
from pytube import YouTube

# initializing tkinter
root = Tk()
# setting the geometry of the GUI
root.geometry('400x350')
# setting the title of the GUI
root.title("YouTube Video Downloader")
# setting background colour to the GUI
root.configure(bg='#696969')


# defining download function
def download():
    # to avoid traceback
    try:
        myVar.set("Downloading....")
        root.update()
        YouTube(link.get()).streams.first().download()
        link.set(" Video Downloaded Successfully")
    except Exception as e:
        myVar.set("Mistake")
        root.update()
        link.set("Enter the correct link")


# created the Label widget to welcome user
Label(root, text="YouTube\nDownloader", font="Consolas 15 bold").pack()
# declaring StringVar type variable
myVar = StringVar()
# setting the default text to myVar
myVar.set("Enter the link below")
# created the Entry widget to ask user to enter the url
Entry(root, textvariable=myVar, width=30).pack(pady=10)
# declaring StringVar type variable
link = StringVar()
# created the Entry widget to get the link
Entry(root, textvariable=link, width=60).pack(pady=20)
# created and called the download function to download video
Button(root, text="Download video", command=download).pack()
# running the mainloop
root.mainloop()
