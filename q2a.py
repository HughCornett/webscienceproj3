import json
from os import listdir
from os.path import isfile, join, dirname, abspath
from sys import argv, exit
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d 

songs = [('Adele - Hello', 18), ('fRh_vgS2dFE', 18), ("Drake - Hotline Bling", 14), ("Justin Bieber - What Do You Mean?", 71), ("Shawn Mendes - Stitches (Official Video)", 138), ("The Weeknd - Can't Feel My Face", 103)]

songViews = dict()
for song in songs:
	songViews[song[0]] = []

def checkFilesIn(j):
	files = [f for f in listdir(j) if isfile(join(j, f))]
	for i in files:
		with open(j+"\\"+i) as json_file:
		    data = json.load(json_file)
		    for p in data:
		    	if(p['snippet']['title'].encode('utf-8') in (i[0] for i in songs) or p['id'] in (j[0] for j in songs)):
			    	
			    	if(p['snippet']['title'] in songViews):
			    		songViews[p['snippet']['title'].encode('utf-8')].append(int(p['statistics']['viewCount']))
			    	elif p['id'] in songViews:	
			    		songViews[p['id'].encode('utf-8')].append(int(p['statistics']['viewCount']))



mypath = dirname(abspath(__file__))
subfolders = ['youtube_top100', 'radio538_alarmschijf', 'radio3fm_megahit']
for i in subfolders:
	checkFilesIn(i)
#print(songViews)

for k in range(len(songs)):
	ax = plt.subplot(321+k)

	print(songViews[songs[k][0]])

	x = [0]
	y = [0]
	x.extend([i for j in (range(songs[k][1], 57+songs[k][1]), range(songs[k][1]+134, songs[k][1]+382)) for i in j])
	y.extend(songViews[songs[k][0]])

	print(len(x))
	print(len(y))
	print(y)

	yinterp = interp1d(x, y, kind='cubic')

	plt.title(songs[k][0])
	plt.xlabel('day')
	plt.ylabel('views')
	ax.plot(x, y, 'o', x, yinterp(x), '-')

	ax.plot([0,1], [0,1], transform=ax.transAxes)
plt.show()