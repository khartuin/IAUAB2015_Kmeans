import random
import numpy as np
from skimage import data, io, filter
from skimage.transform import rescale
import ColorNaming as cn

def processData(Im, options):
	ImOut = None

	if options['rescale']:
		ImOut = 255*rescale(Im, options['scaleFactor'])
        else:
           	ImOut = 255*Im
	return ImOut

def sortCentroids(centroids, clusters):
	s = []
	centroidsOut = []
	for c in range(len(clusters)):
		s.append(len(clusters[c]))
	keys = sorted(range(len(s)), key=lambda k: s[k], reverse=True)
	for k in keys:
		centroidsOut.append(centroids[k])	
	return centroidsOut


def selectSeeds(X, K, opts):
	if opts['method'] == 'random':
		return selectSeedsRandom(X, K, opts)



def selectSeedsRandom(X, K, opts):
	"TODO"
	return Seeds

