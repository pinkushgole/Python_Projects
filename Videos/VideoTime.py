from moviepy.editor import VideoFileClip
from datetime import timedelta
with VideoFileClip("ganesh.mp4") as video:
        duration_seconds = video.duration  

print("Videos Time Duration :",duration_seconds)

duration = timedelta(seconds=duration_seconds)

print("Videos Time Duration :",duration)
      
    