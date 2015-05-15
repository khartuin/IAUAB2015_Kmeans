import random
import numpy as np
from skimage import data, io, filter
from skimage.transform import rescale
import ColorNaming as cn

def transformColorSpace(Im, options):
	# space convertion to the 11-D potentials space
	# space conversion: [0, 255]^3 --> [0, 1]^11
	if options['colorSpace'] == 'Potentials':
		ImOut = cn.ImColorNamingTSELabDescriptor(Im)
	else:
		ImOut = Im
	
	# type conversion and flattening
        ImOut = ImOut.reshape(ImOut.shape[0]*ImOut.shape[1], ImOut.shape[2])
	return ImOut
