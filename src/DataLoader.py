# encoding: utf-8

import os
import sys
import glob
from skimage import data, io

def loadImages(imageFolder):
	imageList = []
	imageNames = sorted(glob.glob(str(imageFolder) + "/*.jpg"))
	for imname in imageNames:
		imageList.append(data.imread(imname))
	return imageList

def loadGT(filename):
	# GT is a list of tuples (Name, [list-of-labels])
	GT = []
	fd = open(filename, 'r')
	for line in fd:
		
		splitLine = line.split(' ')
		name = splitLine[0]
		labels = []
		for i in range(1, len(splitLine)-1):
			labels.append(splitLine[i])
		GT.append( (name, labels) )
	return GT
