import json
from os import listdir
from os.path import isfile, join, dirname, abspath
from sys import argv, exit
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

files = ['20151109_1800_data.json', '20151123_1800_data.json', '20151207_1800_data.json', '20160104_1800_data.json', '20160403_1800_data.json', '20161127_1800_data.json']

fileViews = dict()
for file in files:
	fileViews[file] = dict()

def checkFilesIn(j):
	for i in files:
		#try:
		with open(j+"\\"+i) as json_file:
		    data = json.load(json_file)
		    for p in range(len(data)):
		    	print(p)
		    	#views += p['statistics']['viewCount']
		    	fileViews[i][p] = int(data[p]['statistics']['viewCount'])
		    	if i == '20161127_1800_data.json':
		    		print(data[p]['statistics']['viewCount'])

def f(x, z):
	with np.errstate(divide='ignore', invalid='ignore'):
		y=[]
		for i in x:
			if i != 0:
				y.append(long(z[0])/pow(i, 1))
			else:
				y.append(float('Inf'))
		return y

mypath = dirname(abspath(__file__))
subfolders = ['youtube_top100']#, 'radio538_alarmschijf', 'radio3fm_megahit']
for i in subfolders:
	checkFilesIn(i)
#print(fileViews)

def fun1():
	for i in range(len(files)):
		plt.subplot(321+i)


		y = []
		for key, value in sorted(fileViews[files[i]].items(), key=lambda item: item[1], reverse=True):
			y.append(value)
		x = range(len(y))

		x = np.array(x)
		print(y)
		y = np.array(y)
		plt.title(files[i])

		plt.xlabel('song position')
		plt.ylabel('views')
		plt.scatter(x, y)

def fun2():
	plt.figure()
	for i in range(len(files)):
		plt.subplot(321+i)

		x = []
		y = []
		for key, value in sorted(fileViews[files[i]].items()[:10], key=lambda item: item[1]):
			x.append(str(key+1))
			y.append(value)

		x = np.array(x)
		print(y)
		y = np.array(y)
		plt.title(files[i])

		plt.xlabel('song title')
		plt.ylabel('views')
		plt.bar(x, y)

	with open('youtube_top100\\20151109_1800_data.json') as json_file:
		    data = json.load(json_file)
		    for p in range(10):
		    	print(str(p+1)+": "+data[p]['snippet']['title'])
fun1()	
fun2()
plt.show()