import sys
import numpy as np
from PIL import Image
import imagehash

im=Image.open(sys.argv[1])
a=np.asarray(im)
print(a.shape)
a=a/255.
a_hash=imagehash.average_hash(im)
print(a_hash)

im2=Image.open(sys.argv[2])
b=np.asarray(im2)
print(b.shape)

im3=Image.fromarray(b)
im3.show()

b=b/255.
b_hash=imagehash.average_hash(im2)
print(b_hash)

simi=np.linalg.norm(a-b)
print(simi)
hash_simi=a_hash-b_hash
print(hash_simi)