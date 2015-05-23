# encoding: utf-8
import random
from numpy import *
from scipy.spatial import distance
import sys

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
  
def setStartingCentroids(X, K, method = 'random'):
  centroidList = []
  
  if method == 'random':
    checklist = []
    random.seed()
    for i in range(K):
      r = random.randint(0,len(X)-1)
      if r in checklist:
	while r in checklist:
	  r = random.randint(0,len(X)-1)
      checklist.append(r)
      centroidList.append(X[r])
      
    #elif method == 'random_minDist':
      #checklist = []
      #distList
      #random.seed()
      #for i in range(K):
	#r = random.randint(0,len(X)-1)
	#if r in checklist:
	  #while r in checklist:
	    #r = random.randint(0,len(X)-1)
	#for i 
	#checklist.append(r)
	#centroidList.append(X[r])
	
      #else:
	#raise NotImplemented
	
  return centroidList

def fillPointDict(X):
  pointDict = {}
  for i in range(len(X)):
    pointDict[i] = [-1,-1]	#Pos 0: cluster number (initially -1), Pos 1: distance to centroid
  
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
      pointDict[point][0] = centroid	#Cluster numbers are 1-k
      pointDict[point][1] = min(distances)
      #print "Point " + str(point) + " at " + str(X[point]) + " belongs to " + str(pointDict[point][0])
      bChangedClusters = True
  
  return bChangedClusters

def moveCentroids(centroidList, pointDict, X):
  for centroid in range(len(centroidList)):
    coords = zeros(len(X[0]))
    i = 0
    for point in X:
      #print "Checking with point " + str(i) + ", it belongs supposedly to: " + str(pointDict[i][0])
      if pointDict[i][0] == (centroid):
	#print "MATCH"
	coords+=point
      i += 1
    divArray = i*ones(len(X[0]))  
    meanCoords = coords/divArray
    centroidList[centroid] = meanCoords
  
def getClusters(pointDict, K, X):
  clusterDict = {}
  
  for cluster in range(K):
    aux = []
    
    for point in pointDict:
      if pointDict[point][0] == cluster:
	aux.append([point,X[point]])
	
    clusterDict[cluster] = aux
    
  return clusterDict
	