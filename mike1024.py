# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:45:16 2020

@author: K0718
"""

from pytube import YouTube
import tkinter as tk
window=tk.Tk()

#########by teacher############
window.title("Youtube下載器")
window.geometry("500x150")
window.resizable(False,False)

#######################

progress=0
def showProgress(stream,chunk,bytes_remaining):
    size=stream.filesize
    global progress
    preprogress=progress
    currentprogress=int((size-bytes_remaining)*100/size)
    progress=currentprogress
    
    if progress == 100:
        print("下載完成")
        return
    
    if preprogress!=progress:
        scale.set(progress)
        window.update()
        #print("目前進度:"+ (currentprogress)+"%") #by mike
        print("目前進度:"+ str(currentprogress)+"%") #by teacher
        
    
    


def onClick():
    global var
    var.set(entry.get())
    try:
      yt = YouTube(var.get(),on_progress_callback=showProgress)
      stream = yt.streams.first()
      stream.download()
    except:
        print("下載失敗")


 
    
label=tk.Label(window,text="請不要輸入Youtube網址")
label.pack()


var = tk.StringVar()
entry=tk.Entry(window,width=50)
entry.pack()


#########by teacher###############
button=tk.Button(window,text="下載",command=onClick)
button.pack()

##########################


scale = tk.Scale(window,label="進度條",orient=tk.HORIZONTAL,length=200) #by mike
scale.pack()
window.mainloop()