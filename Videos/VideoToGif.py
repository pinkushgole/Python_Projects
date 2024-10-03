# pip install moviepy: work on video file

from moviepy.editor import *

video=VideoFileClip("ganesh.mp4").subclip(00,4)

video.write_gif("t1.gif")
