"""A video playlist class."""
from pathlib import Path

class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self,name):
        self._playlistname = name
        print("Successfully created new playlist:" ,self._playlistname)
        self._playlistContent = []
    
    def Add(self,video_name,playlist_name):
        if video_name in self._playlistContent:
            print("Cannot add video to "+str(self._playlistname)+": Video already added")
        else:
            self._playlistContent.append(video_name)
            print("Added video to"+" "+ str(playlist_name)+": "+str(video_name))
   
   
    def ReturnContent(self):
        return self._playlistContent

    def Remove(self, video_name,playlistname):
        if video_name not in self._playlistContent:
            print("Cannot remove video from "+str(self._playlistname)+": Video is not in playlist.")
        else:
            
            self._playlistContent.remove(video_name)
            print("Removed video from "+str(playlistname)+": "+str(video_name))

    
    def Clear(self):
        self._playlistContent.clear()
        
    
    @property
    def name (self):
        return self._playlistname



                

    
