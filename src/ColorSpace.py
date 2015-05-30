import random
from math import floor
import numpy as np
from skimage import data, io, filter
from skimage.transform import rescale
import ColorNaming as cn

def transformColorSpace(Im, options):
  # space convertion to the 11-D potentials space
  # space conversion: [0, 255]^3 --> [0, 1]^11

  if options['colorSpace'] == 'Potentials':
    ImOut = cn.ImColorNamingTSELabDescriptor(Im)
  elif options['colorSpace'] == 'Cie-Lab':
    ImOut = cn.ImsRGB2Lab(Im)
  elif options['colorSpace'] == 'HSV':
    ImOut = RGB2HSV(Im)
    
    #For testing purposes:
    #print ImOut
    #print HSV2RGB_2(ImOut)
  else:
    ImOut = Im
  
  # type conversion and flattening
  ImOut = ImOut.reshape(ImOut.shape[0]*ImOut.shape[1], ImOut.shape[2])
  return ImOut

def RGB2HSV(Im):
  #print "RGB2HSV"
  for row in Im:
    for column in row:
      #print "BEFORE:"
      #print column
      r = column[0]
      g = column[1]
      b = column[2]
      
      if (r==g==b):
	#Fix for achromatic (greyscale, no saturation) colors
	h = 0
	s = 0
	v = (float(r)/255.0)*100.0
	
      else:      
	m = min([r,g,b])
	M = max([r,g,b])
	v = M			#Value
	
	delta = M-m
	
	if M != 0:
	  s = delta/M		#Saturation
	  #print s
	  
	  if r == M:		#between yellow & magenta
	    #print "R==M"
	    h = (g-b)/delta
	    #print h
	  elif g == M:		#between cyan & yellow
	    #print "G==M"
	    h = 2 + (b-r)/delta
	  else:			#between magenta & cyan
	    h = 4 + (r-g)/delta
	    
	  h *= 60			#degrees
	  #print h
	  
	  if h<0:
	    h += 360
	else:
	  # R=G=B=0, black?
	  h=0
	  s=0
	  v=0
	
      column[0] = h
      column[1] = s
      column[2] = v
      #print "AFTER:"
      #print column
  return Im
  
def HSV2RGB(Im):
  for group in Im:
    h = group[0]
    s = group[1]
    v = group[2]
    
    if s == 0:
      #Achromatic (grey)
      r = g = b = v
    
    else:
      h /= 60			#sector 0 to 5
      i = int(floor(h))
      f = h - i			#factorial part of h
      p = v * (1 - s)
      q = v * (1 - s*f)
      t = v * (1 - s * (1 - f))
      
      if i == 0:
	r = v
	g = t
	b = p
      elif i == 1:
	r = q
	g = v
	b = p
      elif i == 2:
	r = p
	g = v
	b = t
      elif i == 3:
	r = p
	g = q
	b = v
      elif i == 4:
	r = t
	g = p
	b = v
      else:
	r = v
	g = p
	b = q
    
    group[0] = r
    group[1] = g
    group[2] = b
  return Im

#Version for use directly with ImOut (before reshaping), for testing purposes
  
#def HSV2RGB_b(Im):
  #for row in Im:
    #for column in row:
      #h = column[0]
      #s = column[1]
      #v = column[2]
      
      #if s == 0:
	##Achromatic (grey)
	#r = g = b = v
      
      #else:
	#h /= 60			#sector 0 to 5
	#i = floor(h)
	#f = h - i		#factorial part of h
	#p = v * (1 - s)
	#q = v * (1 - s*f)
	#t = v * (1 - s * (1 - f))
	
	#if i == 0:
	  #r = v
	  #g = t
	  #b = p
	#elif i == 1:
	  #r = q
	  #g = v
	  #b = p
	#elif i == 2:
	  #r = p
	  #g = v
	  #b = t
	#elif i == 3:
	  #r = p
	  #g = q
	  #b = v
	#elif i == 4:
	  #r = t
	  #g = p
	  #b = v
	#else:
	  #r = v
	  #g = p
	  #b = q
      
      #column[0] = r
      #column[1] = g
      #column[2] = b
      
  #return Im