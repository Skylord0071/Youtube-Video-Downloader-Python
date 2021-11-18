import pywhatkit
from pytube import YouTube


while True:
    a = input("Which video do you want sir... ")
    url = pywhatkit.playonyt((a), open_video=False)

    g = input("Sir do want a youtube video link ??(y/n)")
    if g == 'y':
        print(url)

    yt = YouTube(url)
    #Showing details
    print("Title: ",yt.title)
    print("Number of views: ",yt.views)
    print("Length of video: ",yt.length)
    print("Rating of video: ",yt.rating)
    #Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()

    #Starting download
    print("Downloading...")
    ys.download()
    print("Download completed!!")

    sir = input("Do you want to download again? (y/n)")
    if sir.lower() == 'n':
        print("Thank you sir")
        break
