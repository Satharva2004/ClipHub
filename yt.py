from pytube import YouTube

url = input("provide link: ")
my_video = YouTube(url)

print(my_video.title)
print(my_video.thumbnail_url)

videos = my_video.streams.filter(progressive=True)
vid = list(enumerate(videos))
for i in vid:
    print(i)

strn = int(input("Provide index to download: "))
videos[strn].download()
print("Succesfull vid")





