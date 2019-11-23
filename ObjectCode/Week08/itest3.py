import sys
import os
import numpy as np
from PIL import Image
from heapq import heappush
from heapq import heappop
import matplotlib.pyplot as plt

def norm_simi(ima,imb):
	a=np.asarray(ima)
	b=np.asarray(imb)
	if a.shape == b.shape:
		return np.linalg.norm(a-b)
	else:
		return float('inf')

#load images
imflist=[]
for root,dirs,files in os.walk(sys.argv[1]):
	for file in files:
		if file.find('.ppm')>0:
			#print(os.path.join(root,file))
			imflist.append(os.path.join(root,file))

input_img=Image.open(sys.argv[2])

simi_images=[]

for imf in imflist:
	im=Image.open(imf)
	simi=norm_simi(input_img,im)
	heappush(simi_images,(simi,imf))

plt.figure()
plt.subplot(4,3,2)
plt.imshow(input_img)
plt.axis('off')
for i in range(9):
	image=heappop(simi_images)
	im=Image.open(image[1])
	print(image[0])
	plt.subplot(4,3,i+4)
	plt.imshow(im)
	plt.axis('off')
plt.show()

