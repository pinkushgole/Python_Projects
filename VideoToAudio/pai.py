import moviepy.editor

video=moviepy.editor.VideoFileClip("ganesh.mp4")


aud=video.audio

aud.write_audiofile("demo.mp3")
print("--END--")