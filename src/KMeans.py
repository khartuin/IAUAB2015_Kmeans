# encoding: utf-8
import random
from scipy.spatial import distance

def KMeans (X, K):
  centroids = setStartingCentroids(X,K)
  pointDict = fillPointDict(X)
  bChangedClusters = True
  
  while(bChangedClusters):
    bChangedClusters = updateClusters(centroids,pointDict)
    if(bChangedClusters):
      moveCentroids(centroids, pointDict)
  
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
  for i in 
