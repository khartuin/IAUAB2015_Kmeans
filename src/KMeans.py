# encoding: utf-8
import random
import numpy
from scipy.spatial import distance

def KMeans (X, K):
  centroids = setStartingCentroids(X,K)
  pointDict = fillPointDict(X)
  bChangedClusters = True
  
  while(bChangedClusters):
    bChangedClusters = updateClusters(centroids,pointDict)
    if(bChangedClusters):
      moveCentroids(centroids, pointDict)
  
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
  for i in X:
    pointDict[i] = [-1,0]
  
  return pointDict

def updateClusters(centroids, pointDict):
  bChangedClusters = False
  
  for point in pointDict:
    distances = []
    
    for cent in centroids:
      d = distance.euclidean(point,cent)
      distances.append(d)
        
    if min(distances) != pointDict[point][1]:
      centroid = distances.index(min(distances))
      pointDict[point][0] = centroid + 1
      pointDict[point][1] = min(distances)
      bChangedClusters = True
  
  return bChangedClusters

def moveCentroids(centroids, pointDict):
  
  for cent in range(len(centroids)):
    coordsX=[]
    coordsY=[]
    coordsZ=[]
    for point in pointDict:
      if pointDict[point][0] == (centroid + 1):
	coordsX.append(point[0])
	coordsY.append(point[1])
	coordsZ.append(point[2])
    newX = numpy.median(numpy.array(coordsX))
    newY = numpy.median(numpy.array(coordsY))
    newZ = numpy.median(numpy.array(coordsZ))
    
    centroids[cent] = [newX,newY, newZ]
    
def getClusters(pointDict,K):
  clusterDict = {}
  
  for cluster in range(1,K+1):
    aux = []
    
    for point in pointDict:
      if pointDict[point][0] == cluster:
	aux.append(point)
	
    cluster[cluster] = aux
    
  return clusterDict
	