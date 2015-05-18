from scipy.spatial import distance

def Fisher (centroidList, clusterDict):
  print "Fisher"
  k = len(centroidList)
  
  #IntraClusterDistances
  sumOfMeanDistances = 0.0
  for cluster in range(k):
    mc = float(len(clusterDict[cluster]))
    sumOfDistances = 0.0
    for point in clusterDict[cluster]:
      distanceToCenter = distance.euclidean(point[1],centroidList[cluster])
      sumOfDistances += distanceToCenter
    try:
      sumOfMeanDistances += sumOfDistances/mc
    except ZeroDivisionError:
      print "NAN in cluster: " + str(cluster)
      continue
  
  #InterClusterDistances
  i = 1
  sumOfMeanDistanceOfPairs = 0.0
  for a in range(k):
    for b in range(i,k):
      distanceOfPair = distance.euclidean(centroidList[a],centroidList[b])
      sumOfMeanDistanceOfPairs += distanceOfPair
      i += 1
  print sumOfMeanDistances
  print sumOfMeanDistanceOfPairs
  res = sumOfMeanDistances/sumOfMeanDistanceOfPairs 	
  #res = (((float(k)-1.0)/2.0)*sumOfMeanDistances)/sumOfMeanDistanceOfPairs
  
  return res
