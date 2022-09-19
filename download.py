
from pytube import YouTube
from sys import argv

link = argv[1]

yt = YouTube(link) # YouTube object
print("Title: ", yt.title)

# Get the highest resolution possible
ys = yt.streams.get_highest_resolution()

print("Downloading...")
ys.download() # Download to the current directory
print("Download completed!!")

