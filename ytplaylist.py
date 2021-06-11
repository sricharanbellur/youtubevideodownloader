from pytube import Playlist
playlist=Playlist('https://www.youtube.com/watch?v=k_STMxz31Q4&list=PLVDfFatHsysRbgO2AGFiJ07F5HVDCLCcF')
for video in playlist.videos:
    video.streams.first().download("E:/ISE_6_Sem")