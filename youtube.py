from pytube import YouTube
#YouTube('https://youtu.be/9bZkp7q19f0').streams.get_highest_resolution().download()
yt = YouTube("https://www.youtube.com/watch?v=4M_AiGA5wpA")
(yt.streams
    .filter(progressive=True, file_extension='mp4')
    .order_by('resolution')[-1]
    .download())