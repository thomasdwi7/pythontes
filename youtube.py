from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import Youtube


#Function
def select_path():
    #allow user to select path
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget('text')
    #download video 
    mp4_video = Youtube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()



screen = Tk()
tittle = screen.title('YOUTUBE DONWLOAD')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#Image logo

#link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter Donwload LINK:)")
#Select path for saving 
path_label = Label(screen, text='Select path')
select_btn = Button(screen, text='Select', command=select_path)
#add to window 
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

#Add widget window 
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)



#Donwload btn
download_btn = Button(screen, text="Download File", command=download_file)
#Add to canvas
canvas.create_window(250, 390, window=download_btn)

screen.mainloop()
