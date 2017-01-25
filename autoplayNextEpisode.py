import subprocess
import send2trash
import os
import sys 

while  True:					# loop to play next episode if ENTER is the input
	animeDirectory = "D:\Anime\\"
	animeTitle     = "one piece"
	listEpisode    = os.listdir(animeDirectory + animeTitle)
	episodeToWatch = animeDirectory + animeTitle + "\\" + listEpisode[0]
	print("Now playing: "+ episodeToWatch)
	vlc_path	   = r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
	process        = subprocess.Popen([vlc_path, episodeToWatch])
	process.wait()


	isEpisodeViewed = input('''Episode finished ? :
	y - YES, delete episode.
	n - NO, don't delete episode.
	ENTER - Delete episode and play next episode.
	s - delete episode and shutdown the computer. 
	''')
	if isEpisodeViewed=="y":	# watch only one episode
		send2trash.send2trash(episodeToWatch)
		print ("Deleted : %s" % episodeToWatch)
		break
	elif isEpisodeViewed=="n":
		break					# don't delete the unfinished episode 
	elif isEpisodeViewed=="":	# watch the next episode
		send2trash.send2trash(episodeToWatch)
		print ("Deleted : %s" % episodeToWatch)
		continue
	elif isEpisodeViewed=="s":  # delete episode and shutdown the computer 
		send2trash.send2trash(episodeToWatch)
		print ("Deleted : %s" % episodeToWatch)
		os.system('shutdown -s')
		break					
		
