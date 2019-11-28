import json
from os import listdir
from os.path import isfile, join, dirname, abspath
from sys import argv, exit
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d 

songs = ['Adele - Hello', 'fRh_vgS2dFE', "Drake - Hotline Bling", "Justin Bieber - What Do You Mean?", "Shawn Mendes - Stitches (Official Video)", "The Weeknd - Can't Feel My Face"]

songViews = dict()
for song in songs:
	songViews[song] = []

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
			    	if(p['snippet']['title'] in songViews):
			    		songViews[p['snippet']['title'].encode('utf-8')].append(int(p['statistics']['viewCount']))
			    	elif p['id'] in songViews:	
			    		songViews[p['id'].encode('utf-8')].append(int(p['statistics']['viewCount']))



mypath = dirname(abspath(__file__))
subfolders = ['youtube_top100', 'radio538_alarmschijf', 'radio3fm_megahit']
for i in subfolders:
	checkFilesIn(i)
print(songViews)

for k in range(len(songs)):
	ax = plt.subplot(321+k)
	x = [i for j in (range(57), range(134, 382)) for i in j]
	y = songViews[songs[k]]

	yinterp = interp1d(x, y, kind='cubic')

	plt.title(songs[k])
	plt.xlabel('day')
	plt.ylabel('views')
	ax.plot(x, y, 'o', x, yinterp(x), '-')

	lims = [
	np.min([ax.get_xlim(), ax.get_ylim()]),
	np.max([ax.get_xlim(), ax.get_ylim()])
	]

	#lowerLim = np.min(np.max(ax.get_xlim()), np.max(ax.get_ylim()))

	ax.plot([0,1], [0,1], transform=ax.transAxes)
plt.show()