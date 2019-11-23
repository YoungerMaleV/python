import sys
import os
#import numpy as np
from PIL import Image
import imagehash
from heapq import heappush
from heapq import heappop
import matplotlib.pyplot as plt
import numpy as np

def norm_simi(ima,imb):
	a=np.asarray(ima)
	b=np.asarray(imb)
	return np.linalg.norm(a-b)

im_hash_map={}
for root,dirs,files in os.walk(sys.argv[1]):
	for file in files:
		if file.find('.ppm')>0:
			#print(os.path.join(root,file))
			im=Image.open(os.path.join(root,file))
			#im_array=np.asarray(im)
			#print(a.shape)
			im_a_hash=imagehash.average_hash(im)
			im_hash_map[os.path.join(root,file)]=im_a_hash

im=Image.open(sys.argv[2])
imhash=imagehash.average_hash(im)
simi_images=[]
for image in im_hash_map:
	simi=im_hash_map[image]-imhash
	heappush(simi_images,(simi,image))

plt.figure()
plt.subplot(4,3,2)
plt.imshow(im)
plt.axis('off')
for i in range(9):
	image=heappop(simi_images)
	im=Image.open(image[1])
	print(image[0])
	plt.subplot(4,3,i+4)
	plt.imshow(im)
	plt.axis('off')
plt.show()

'''
Method: 
  ahash:      Average hash
  phash:      Perceptual hash
  dhash:      Difference hash
  whash-haar: Haar wavelet hash (whash)
  whash-db4:  Daubechies wavelet hash(whash(im,mode='db4'))
 '''
