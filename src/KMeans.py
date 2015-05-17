# encoding: utf-8
import random
import numpy
from scipy.spatial import distance

def KMeans (X, K, Seeds):
  centroids = Seeds	#setStartingCentroids(X, K)
  pointDict = fillPointDict(X)
  bChangedClusters = True

  while(bChangedClusters):
    bChangedClusters = updateClusters(centroids, pointDict, X)
    if(bChangedClusters):
      moveCentroids(centroids, pointDict, X)
  
  clusterDict = getClusters(pointDict, K, X) #Cluster Dict: keys are clusters, values are lists with [pointNumber,pointPosition]
  
  return (centroids, clusterDict)
  
def setStartingCentroids(X,K):
  centroidList = []
  random.seed()
  
  for i in range (K):
    r = random.randint(0,len(X)-1)
    centroidList.append(X[r])
    
  return centroidList
range
def fillPointDict(X):
  pointDict = {}
  for i in range(len(X)):
    pointDict[i] = [-1,0]	#Pos 0: cluster number (initially -1), Pos 1: distance to centroid
  
  return pointDict

def updateClusters(centroids, pointDict, X):
  bChangedClusters = False
  
  for point in pointDict:
    distances = []
    
    for cent in centroids:
      d = distance.euclidean(X[point],cent)
      distances.append(d)
      
    if min(distances) != pointDict[point][1]:
      centroid = distances.index(min(distances))
      pointDict[point][0] = centroid + 1	#Cluster numbers are 1-k
      pointDict[point][1] = min(distances)
      bChangedClusters = True
    numbers[pointDict[point][0] - 1] += 1
  
  return bChangedClusters

def moveCentroids(centroidList, pointDict, X):
  
  for centroid in range(len(centroidList)):
    coordsX=[]
    coordsY=[]
    coordsZ=[]
    i = 0
    
    for point in X:
      if pointDict[i][0] == (centroid + 1):
	coordsX.append(point[0])
	coordsY.append(point[1])
	coordsZ.append(point[2])
      i += 1
      
    newX = numpy.mean(numpy.array(coordsX))
    newY = numpy.mean(numpy.array(coordsY))
    newZ = numpy.mean(numpy.array(coordsZ))
    
    centroidList[centroid] = [newX,newY, newZ]
    
def getClusters(pointDict, K, X):
  clusterDict = {}
  
  for cluster in range(1,K+1):
    aux = []
    
    for point in pointDict:
      if pointDict[point][0] == cluster:
	aux.append([point,X[point]])
	
    clusterDict[cluster] = aux
    
  return clusterDict
	