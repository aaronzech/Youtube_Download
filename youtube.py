from pytube import YouTube
downloadLocation = 'C:/Users/zechaaron/Downloads'

print("Enter Youtube Link")
link = input()
yt = YouTube(link)

print("Title:", yt.title) # Youtube Video Title
print("Views:",yt.views) # View Count
print(yt.thumbnail_url) #Thumb Nail URL

yd = yt.streams.get_highest_resolution() # Get highest video quality
yd.download(downloadLocation) # Download and Save to location

