import tkinter as tk
from tkinter import*
from jinja2 import FunctionLoader
from pytube import YouTube
from tkinter import filedialog, messagebox


def createWidgets():

    link_label = Label(root, text="Youtube URL: ", bg="#FFDC00")
    link_label.grid(row=1, column=0, pady=20, padx=20)

    root.link_text = Entry(root, width=60, textvariable=video_link)
    root.link_text.grid(row=1, column=1, pady=30, padx=30)

    destination_label = Label(root, text="Destination: ", bg="#FFDC00")
    destination_label.grid(row=2, column=0, pady=5, padx=5)

    root.destination_text = Entry(root, width=45, textvariable=download_path)
    root.destination_text.grid(row=2, column=1, pady=3, padx=3)

    browse_but = Button(root, text="Browse", command=browse, width=10, bg="#FFDC00")
    browse_but.grid(row=2, column=2, pady=1, padx=1)

    download_but = Button(root, text="Download Video", command=download_video, width=25, bg="#FFDC00")
    download_but.grid(row=3, column=1, pady=3, padx=3)


def browse():

    download_dir = filedialog.askdirectory(initialdir="Your Directory Path")

    download_path.set(download_dir)


def download_video():
    url = video_link.get()
    folder = download_path.get()

    get_video = YouTube(url)
    get_stream = get_video.streams.first()
    get_stream.download(folder)

messagebox.showinfo("Success!!", "download Your video\n")

root = tk.Tk()
img = PhotoImage(file='D:\\All_Python_files\\Yt_downloader\\logoicon.png')
root.iconphoto(False,img)
root.geometry("700x600")
root.resizable(False, False)
root.title("YouTube Video Downloader")
root.config(background="#FF0000")

video_link = StringVar()
download_path = StringVar()



createWidgets()

root.mainloop()