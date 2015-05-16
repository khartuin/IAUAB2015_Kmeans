# encoding: utf-8
import random
import numpy
from scipy.spatial import distance

def KMeans (X, K):
  centroids = setStartingCentroids(X, K)
  pointDict = fillPointDict(X)
  bChangedClusters = True
  i = 0
  while(bChangedClusters):
    print "iter: " + str(i)
    bChangedClusters = updateClusters(centroids, pointDict, X)
    if(bChangedClusters):
      moveCentroids(centroids, pointDict, X)
    i += 1
  
  clusterDict = getClusters(pointDict,K)
  
  return (centroids, clusterDict)
  
def setStartingCentroids(X,K):
  centroidList = []
  random.seed()
  
  for i in range (K):
    r = random.randint(0,len(X)-1)
    centroidList.append(X[r])
    
  return centroidList

def fillPointDict(X):
  pointDict = {}
  for i in range(len(X)):
    pointDict[i] = [-1,0]	#Pos 0: cluster number (initially -1), Pos 1: distance to centroid
  
  return pointDict

def updateClusters(centroids, pointDict, X):
  bChangedClusters = False
  
  for point in pointDict:
    distances = []
    print "Checking Point " + str(point)
    for cent in centroids:
      print "Checking Centroid " + str(cent)
      d = distance.euclidean(point,cent)
      distances.append(d)
        
    if min(distances) != pointDict[point][1]:
      centroid = distances.index(min(distances))
      pointDict[point][0] = centroid + 1	#Cluster numbers are 1-k
      pointDict[point][1] = min(distances)
      bChangedClusters = True
      print "New centroid for point " + str(point) + " is " + str(centroids[centroid])
  
  return bChangedClusters

def moveCentroids(centroidList, pointDict, X):
  
  for centroid in range(len(centroidList)):
    print "Checking for centroid " + str(centroid)
    coordsX=[]
    coordsY=[]
    coordsZ=[]
    i = 0
    for point in X:
      if pointDict[i][0] == (centroid + 1):
	print "Checking point " + str(i) + " at " + str(point)
	coordsX.append(point[0])
	print "X: " + str(point[0])
	coordsY.append(point[1])
	print "Y: " + str(point[1])
	coordsZ.append(point[2])
	print "Z: " + str(point[2])
      i += 1
    newX = numpy.mean(numpy.array(coordsX))
    newY = numpy.mean(numpy.array(coordsY))
    newZ = numpy.mean(numpy.array(coordsZ))
    print "New coords for centroid " + str(centroid) + "is:"
    print str(newX)
    print str(newY)
    print str(newZ)
    
    centroidList[centroid] = [newX,newY, newZ]
    
def getClusters(pointDict,K):
  clusterDict = {}
  
  for cluster in range(1,K+1):
    aux = []
    
    for point in pointDict:
      if pointDict[point][0] == cluster:
	aux.append(point)
	
    cluster[cluster] = aux
    
  return clusterDict
	