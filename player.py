import subprocess

video_file = "/home/pi/Desktop/videos/80s.mp4"

command = [
    "mpv",
    "--monitoraspect=4:3",
    "--fs",
    "--loop-file=inf",
    "--video-unscaled=yes",
    "--audio=auto",
    "--audio-device=pulse/bluez_sink.08_EB_ED_F3_8C_1B.a2dp_sink",
    "--volume=20",
    video_file
]

subprocess.run(command)
