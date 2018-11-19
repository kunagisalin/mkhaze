import random
import math
import cv2
import numpy as np

def mkhaze(m):
	a = random.uniform(0.7,1)
	b = random.uniform(0.6,1.8)
	t = math.exp(-b)
	Y = np.zeros(m.shape)
	for k in range(3):
		Y[:,:,k] = m[:,:,k]*(1-t)+a*t
	return Y,a,b




if __name__ == '__main__':
	m,a,b = mkhaze(cv2.imread('kire.png')/255.0)
	m = m*255.0
	a = str(round(a,2))
	b = str(round(b,2))
	str = 'haze'+a+'_'+b+'.jpg'
	cv2.imwrite(str, m)