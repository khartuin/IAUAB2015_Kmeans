# encoding: utf-8
from __future__ import division
from sets import Set

def evaluate(EST, GT, metric):
	Scores = []
	overall = 0
	for i in range(len(GT)):
		(gt_name, gt_elem) = GT[i]
		est_elem 	   = EST[i]
		
		if metric == 'basic':
			score = 100.0*metricBasic(est_elem, gt_elem)
			Scores.append(score)
			overall += (1.0/len(GT))*score

	return (Scores, overall)
	
def metricBasic(Est, GT):
	S1 = Set(Est)
	S2 = Set(GT)

	return len(S1.intersection(S2)) / max(len(S1), len(S2))

