import json
from os import listdir
from os.path import isfile, join, dirname, abspath
from sys import argv, exit
import matplotlib.pyplot as plt
import numpy as np

songs = ['Adele - Hello', 'Drake - Hotline Bling', 'The Weeknd - Often (NSFW)', 
	'Fais & Afrojack - Used To Have It All (Official Video)', 'Kensington - Sorry (official audio)', 
	"HVGzOg333CI"]

songRatioList = dict()
for song in songs:
	songRatioList[song] = ([], [])

def checkFilesIn(j):
	files = [f for f in listdir(j) if isfile(join(j, f))]
	for i in files:
		with open(j+"\\"+i) as json_file:
		    data = json.load(json_file)
		    for p in data:
		    	if(p['snippet']['title'].encode('utf-8') in songs or p['id'] in songs):
			    	#print(p['snippet']['title'].encode('utf-8'))
			    	#print(p['statistics']['likeCount'])
			    	#print(p['statistics']['dislikeCount'])
			    	#print('')
			    	likes = int(p['statistics']['likeCount'])
			    	dislikes = int(p['statistics']['dislikeCount'])

			    	if(p['snippet']['title'] in songRatioList):
			    		songRatioList[p['snippet']['title'].encode('utf-8')][0].append(likes + dislikes)
			    		songRatioList[p['snippet']['title'].encode('utf-8')][1].append(likes - dislikes)
			    	elif p['id'] in songRatioList:	
				    	songRatioList[p['id'].encode('utf-8')][0].append(likes + dislikes)
				    	songRatioList[p['id'].encode('utf-8')][1].append(likes - dislikes)
			    
		
mypath = dirname(abspath(__file__))
subfolders = ['youtube_top100', 'radio538_alarmschijf', 'radio3fm_megahit']
for i in subfolders:
	checkFilesIn(i)
print(songRatioList)

for i in range(len(songs)):
	plt.subplot(321+i)
	x = songRatioList[songs[i]][0]
	y = songRatioList[songs[i]][1]
	plt.scatter(x,y)
	yinterp = np.interp(x, x, y)
	plt.plot(x,yinterp)
	plt.title(songs[i])
	plt.xlabel('likes + dislikes')
	plt.ylabel('likes - dislikes')
	
plt.show()