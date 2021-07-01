"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.USERPLAYLISTS = {}
        self._ISPLAYING = False
        self._ISPAUSED = False
        self._NAMEOFCURRENTVIDEO= "" 
        self._CURRENTVIDEOID = ""

    

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        video_list = self._video_library.get_all_videos()
        v_container = []

        for video in video_list:
            if video.Get_flag:
                v_container.append("{} ({}) [{}] - FLAGGED (reason: {})".format(video.title,video.video_id, " ".join(video.tags),video.Get_flagReason))
                
            else:

                temp = ""
                temp+=str(video.title) + " "
                temp+="("+str(video.video_id) +")"+ " "
                temp+= "[" + " ".join([str(tag) if len(video.tags)> 0 else [] for tag in video.tags]) + "]"
                v_container.append(temp)
        
        v_containerS = sorted(v_container)
        print("Here's a list of all available videos:")
        for video in v_containerS:
            print(video)
    


    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        try:

            videoTitle = self._video_library.get_video(video_id).title
            
            flag = self._video_library.get_video(video_id).Get_flag
            if flag:
                print("Cannot play video: Video is currently flagged (reason: {})".format(self._video_library.get_video(video_id).Get_flagReason))
            else:
                if not self._ISPLAYING:
                    print("Playing video:", videoTitle)
                    self._ISPLAYING = True
                    self._ISPAUSED = False
                    self._NAMEOFCURRENTVIDEO= videoTitle
                    self._CURRENTVIDEOID = self._video_library.get_video(video_id).video_id
                else:
                    print("Stopping video:", self._NAMEOFCURRENTVIDEO)

                    print("Playing video:" ,videoTitle)
                    self._ISPLAYING = True
                    self._ISPAUSED = False
                    self._NAMEOFCURRENTVIDEO= videoTitle
                    self._CURRENTVIDEOID = self._video_library.get_video(video_id).video_id
        except:
            print("Cannot play video: Video does not exist")
        
        

        

        

    def stop_video(self):
        """Stops the current video."""

        if self._ISPLAYING:
            print("Stopping video:" , self._NAMEOFCURRENTVIDEO)
            self._ISPLAYING = False
            self._NAMEOFCURRENTVIDEO= ""
            self._CURRENTVIDEOID = ""
            self.paused=False
        else:
            print("Cannot stop video: No video is currently playing")

    
    def play_random_video(self):
        """Plays a random video from the video library."""

        video_List = self._video_library.get_all_videos()
        
        video_list_ids = [Video.video_id for Video in video_List if self._video_library.get_video(Video.video_id).Get_flag == False]
        
        if len(video_list_ids) == 0:
            print("No videos available")
        else:
            self.play_video(random.choice(video_list_ids))
        



    def pause_video(self):
        """Pauses the current video."""

        if (not self._ISPAUSED) and self._ISPLAYING:
            print("Pausing video:", self._NAMEOFCURRENTVIDEO)
            self._ISPAUSED = True
        elif self._ISPAUSED and (self._NAMEOFCURRENTVIDEO!= ""):
            print("Video already paused:", self._NAMEOFCURRENTVIDEO)
        else:
            print("Cannot pause video: No video is currently playing")

        

    def continue_video(self):
        """Resumes playing the current video."""

        if not(self._ISPAUSED) and (self._NAMEOFCURRENTVIDEO!= ""):
            print("Cannot continue video: Video is not paused")
        elif self._ISPAUSED:
            print("Continuing video:", self._NAMEOFCURRENTVIDEO)
            self._ISPAUSED = False
        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
        if self._NAMEOFCURRENTVIDEO== "":
            print("No video is currently playing")
        else:
            video_info = self._video_library.get_video(self._CURRENTVIDEOID)
            if self._ISPAUSED:
                print("Currently playing: "+str(video_info.title) + " " + "("+str(video_info.video_id) +")" +" " + "[" + " ".join([str(tag) if len(video_info.tags)> 0 else [] for tag in video_info.tags])+ "]" + " - PAUSED")
            else:
                print("Currently playing: "+str(video_info.title) + " " + "("+str(video_info.video_id) +")" +" " + "[" + " ".join([str(tag) if len(video_info.tags)> 0 else [] for tag in video_info.tags])+ "]")

            
                
            

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in [name.lower() for name in list(self.USERPLAYLISTS.keys())]:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self.USERPLAYLISTS[playlist_name.lower()] = Playlist(playlist_name)



    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if playlist_name.lower() not in list(self.USERPLAYLISTS.keys()):
            print("Cannot add video to "+str(playlist_name)+": Playlist does not exist")
        
        else:
            try:
                videoTitle = self._video_library.get_video(video_id).title
                if self._video_library.get_video(video_id).Get_flag:
                    print("Cannot add video to my_playlist: Video is currently flagged (reason: {})".format(self._video_library.get_video(video_id).Get_flagReason))
                else:
                    self.USERPLAYLISTS[playlist_name.lower()].Add(videoTitle,playlist_name)
                

            except:
                print("Cannot add video to "+str(playlist_name)+": Video does not exist")

        
        

    def show_all_playlists(self):
        """Display all playlists."""

        if len(self.USERPLAYLISTS) == 0:

            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            for playlist,obj in sorted(self.USERPLAYLISTS.items()):
                print("     ",obj.name)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in [name.lower() for name in list(self.USERPLAYLISTS.keys())]:
            print("Cannot show playlist "+str(playlist_name)+": Playlist does not exist")
        else:
            print("Showing playlist:", playlist_name)
            playlist_obj =self.USERPLAYLISTS[playlist_name.lower()]
            playlist_content = playlist_obj.ReturnContent()
            if len(playlist_content) == 0:
                print("     No videos here yet")
            else:
                all_videos = self._video_library.get_all_videos()
                
                
                for videoT in playlist_content:

                    for video in all_videos:
                        if str(video.title) == videoT:
                            if video.Get_flag:
                                print("     {} ({}) [{}] - FLAGGED (reason: {})".format(video.title,video.video_id, " ".join(video.tags),video.Get_flagReason))
                            else:

                                print("     "+str(video.title)+" "+"(" + str(video.video_id) + ") [" +  " ".join([str(tag) if len(video.tags)> 0 else [] for tag in video.tags])+ "]")


        

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        if playlist_name.lower() not in [name.lower() for name in list(self.USERPLAYLISTS.keys())]:
            print("Cannot remove video from "+str(playlist_name)+": Playlist does not exist")
        else:
            playlist_obj = self.USERPLAYLISTS[playlist_name.lower()]
            if self._video_library.get_video(video_id) == None:
                print("Cannot remove video from "+str(playlist_name)+": Video does not exist")
            else:

            
            
                video_title = (self._video_library.get_video(video_id)).title   
            
                playlist_obj.Remove(video_title,playlist_name)

        

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in [name.lower() for name in list(self.USERPLAYLISTS.keys())]:
            print("Cannot clear playlist "+str(playlist_name)+": Playlist does not exist")
        else:
            playlist_obj = self.USERPLAYLISTS[playlist_name.lower()]
            playlist_obj.Clear()
            print("Successfully removed all videos from " + str(playlist_name))
            
        

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in [name.lower() for name in list(self.USERPLAYLISTS.keys())]:
            print("Cannot delete playlist "+str(playlist_name)+": Playlist does not exist")
        else:
            del self.USERPLAYLISTS[playlist_name.lower()]
            print("Deleted playlist:", playlist_name)
        

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        
        objUnpack = [[video.title, video.video_id, video.tags] for video in self._video_library.get_all_videos() if video.Get_flag == False]
        olist = []
        for vid in objUnpack:
            title = str(vid[0]).lower()
            if search_term.lower() in title:
                olist.append(vid)
        olist = sorted(olist, key= lambda x:x[0])
       
        if len(olist) == 0:
            print("Here are the results for {}: No search results for {}".format(search_term,search_term))
        else:
            print("Here are the results for {}:".format(search_term))
            idx = 1
            for i in olist:
                print("{}) {} ({}) {}".format(idx, i[0],i[1], ("["+" ".join([x for x in i[2]])+"]")))
                idx+=1
            print("Would you like to play any of the above? If yes, specify the number of the video.\nIf your answer is not a valid number, we will assume it's a no.")
            ans = input("YT> ")
            try:
                if 1 <= int(ans) <= idx:
                    self.play_video(olist[int(ans)-1][1])
            except:
                pass 


    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        objUnpack = [[video.title, video.video_id, video.tags] for video in self._video_library.get_all_videos() if video.Get_flag == False]
        olist = []
        for vid in objUnpack:
            tags = " ".join(vid[2])
            
            if video_tag.lower() in tags.lower():
                olist.append(vid)
        
        olist = sorted(olist, key= lambda x:x[0])
        if len(olist) == 0:
            print("Here are the results for {}: No search results for {}".format(video_tag,video_tag))
        else:
            print("Here are the results for {}:".format(video_tag))
            idx = 1
            for i in olist:
                print("{}) {} ({}) {}".format(idx, i[0],i[1], ("["+" ".join([x for x in i[2]])+"]")))
                idx+=1
            print("Would you like to play any of the above? If yes, specify the number of the video.\nIf your answer is not a valid number, we will assume it's a no.")
            ans = input("YT> ")
            try:
                if 1 <= int(ans) <= idx:
                    self.play_video(olist[int(ans)-1][1])
            except:
                pass 
        

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        try:
            Video = self._video_library.get_video(video_id)
            if Video.Get_flag:
                print("Cannot flag video: Video is already flagged")
            else:
                Video.setFlag(True)
                if flag_reason == "":
                    pass
                else:
                    Video.setFlagReason(flag_reason)
                if self._NAMEOFCURRENTVIDEO == Video.title:
                    self.stop_video()
                    print("Successfully flagged video: {} (reason: {})".format(Video.title,Video.Get_flagReason))
                else:
                    print("Successfully flagged video: {} (reason: {})".format(Video.title,Video.Get_flagReason))
                
        except :
            print("Cannot flag video: Video does not exist")

        

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        try:
            Video = self._video_library.get_video(video_id)
            if Video.Get_flag == False:
                print("Cannot remove flag from video: Video is not flagged")
            else:
                Video.setFlag(False)
                print("Successfully removed flag from video: {}".format(Video.title))
                
        except :
            print("Cannot remove flag from video: Video does not exist")
