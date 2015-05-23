from scipy.spatial import distance
from numpy import *

def Fisher (centroidList, clusterDict):
  K = len(clusterDict)
  l = 0
  sumOfPointDistances = 0.0
  for cluster in range(K):
    mc = len(clusterDict[cluster])
    sumOfDistances = 0.0
    if len(clusterDict[cluster])>0:
      l+=1
      for point in clusterDict[cluster]:
	distanceToCentroid = distance.euclidean(point[1],centroidList[cluster])
	sumOfDistances += distanceToCentroid	
      sumOfPointDistances += sumOfDistances/mc
    else:
      print "Cluster " + str(cluster) + " is empty"
  
  sumOfPointDistances = sumOfPointDistances/l
  print sumOfPointDistances
      
  sumOfPairDistances = 0.0
  x=0
  for i in range(K):
    for j in range(i+1,K):
      if clusterDict[i] and clusterDict[j]:
	x+=1
	pairDistance = distance.euclidean(centroidList[i],centroidList[j])
	sumOfPairDistances += pairDistance
      
  print sumOfPairDistances
  
  res = ((l-1.0)/2.0)*sumOfPointDistances/sumOfPairDistances
  

  return res
      
  #i = array(centroidList)
  #j = array(centroidList)
    
  
  #print "Fisher"
  #k = len(centroidList)
  
  ##IntraClusterDistances
  #sumOfMeanDistances = 0.0
  #for cluster in range(k):
    #mc = float(len(clusterDict[cluster]))
    #sumOfDistances = 0.0
    #for point in clusterDict[cluster]:
      #distanceToCenter = distance.euclidean(point[1],centroidList[cluster])
      #sumOfDistances += distanceToCenter
    #try:
      #sumOfMeanDistances += sumOfDistances/mc
    #except ZeroDivisionError:
      #print "Cluster " + str(cluster) + " is empty"
      #continue
  
  ##InterClusterDistances
  #i = 1
  #sumOfMeanDistanceOfPairs = 0.0
  #for a in range(k):
    #for b in range(i,k):
      #distanceOfPair = distance.euclidean(centroidList[a],centroidList[b])
      #sumOfMeanDistanceOfPairs += distanceOfPair
      #i += 1
  #print sumOfMeanDistances
  #print sumOfMeanDistanceOfPairs
  #res = sumOfMeanDistances/sumOfMeanDistanceOfPairs 	
  ##res = (((float(k)-1.0)/2.0)*sumOfMeanDistances)/sumOfMeanDistanceOfPairs
  
  #return res
