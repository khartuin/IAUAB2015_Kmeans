# encoding: utf-8
import DataLoader as dl
import DataProcessor as dp
import ColorSpace as ce

# !!! TO-DO: Define a module called KMeans
# !!!	     and implement the K-Means method
from KMeans import *

from Evaluator import *
import ColorNaming as cn

# !!! TO-DO: Define a module called Fisher
# !!!	     and implement the Fisher method
import Fisher as fs

#define the datasets
ImageFolder 	= '../ImagesReduced'
GTFile		= '../ImagesReduced/LABELS.gt'


# set up the process
colorSpace	= 'RGB'		# RGB | Potentials | HSV | Cie-Lab
rescale		= True		#
scaleFactor	= 0.1		# rescaling factor for speeding-up the method!
seedSelection	= 'random'	# random initialization or something more sophisticated
K		= 2	#2		# if -1 then K it's automatically adjusted
maxK		= 8		# max number of clusters for the Fisher heuristic
labelsType	= 2		# 1 (simple) | 2 (composed labels!)

labelThrs	= 0.1
# evaluation parameters
metric 		= 'basic'	# "basic" union-set metric | others




#############################################
# 1. load data & set options up
#############################################
# Images is a list of numpy
Images 	= dl.loadImages(ImageFolder)
# GT (ground truth) is a list of tuples (fname, [list-of-labels])
GT	= dl.loadGT(GTFile)

# Setting up all the options!
opts_prepro = {'rescale':rescale, 'scaleFactor':scaleFactor, 'colorSpace':colorSpace}
opts_seeds = {'method':seedSelection}
opts_labeller = {'labelsType':labelsType, 'labelThrs':labelThrs, 'colorSpace':colorSpace}

#############################################
# 2. Now it's time to play with the data
#############################################
gt_index = 0
TLabels = []
for im in Images:
	#############################################
	# 2.1. Data preprocessing & transformation
	#############################################
	imprep 	 = dp.processData(im, opts_prepro)
	#############################################
	# 2.2. Color space transformation (from Image to np.ndarray X)
	#############################################
	X = ce.transformColorSpace(imprep, opts_prepro)
	#############################################
	# 2.3. Selection of K (number of clusters)
	#############################################
	#Done already below for K == -1

	#############################################
	# 2.4. Selection of the K seeds --> Seeds
	#############################################
	if K == -1:
	  resultList = []
	  fisherList = []
	  for k in range(2, maxK+1):
	    Seeds = setStartingCentroids(X, k)

	#############################################
	# 2.5. Run K-Means 
	# --> (centroids, clusters) = KMeans(X, K, Seeds)
	#############################################
	    centroids, clusters = KMeans(X, k, Seeds)
	     
	#############################################
	# 2.6. Evaluate clusters according to Fisher
	#      Not required in a first implementation
	#      but recommended once K-Means is correctly
	#      implemented!
	#############################################
	    fDisc= fs.Fisher(centroids, clusters)
	    print "Result for k: " + str(k) + " is: " + str(fDisc)
	    resultList.append([centroids,clusters])
	    fisherList.append(fDisc)
	  
	  bestResult = resultList[fisherList.index(min(fisherList))]
	  centroids = bestResult[0]
	  print "Best Result is " + str(min(fisherList)) + " with k=" + str(len(centroids))
	  
	else:
	  Seeds = setStartingCentroids(X, K)
	  centroids, clusters = KMeans(X, K, Seeds)
	
	#############################################
	# 2.7. Assign labels to centroids by color naming
	#############################################
	(labels, weights) = cn.ClusterColorNaming(centroids, opts_labeller)
	TLabels.append(labels);

	print labels
	print GT[gt_index]
	gt_index = gt_index + 1

#############################################
# 3. Let's analyse the results
#############################################
(scores, overall) = evaluate(TLabels, GT, metric)
for i in range(len(scores)):
	(imgName, imgLabels) = GT[i]
	sc = scores[i]
	print imgName + ' [' + str(sc) + '%] of accuracy'
print '** Overall accuracy is = [' + str(overall) + '%]'
