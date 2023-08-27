
import subprocess

video_file = "/home/pi/Desktop/videos/80s.mp4"

command = ["mpv",
"--monitoraspect=4:3",
"--fs",
"--loop-file=inf",
"--video-unscaled=yes",
"--audio=auto",
video_file]

subprocess.run(command)