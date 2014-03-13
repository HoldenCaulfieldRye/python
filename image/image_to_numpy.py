
from PIL import Image
from PIL import ImageOps


# from jpg to numpy

# from numpy to jpg
img_np = batch[0].copy() # is this image demeaned?
img_jpg = Image.fromarray(img_np)



# open image
>>> im = Image.open('/home/alex/Pictures/nexus1.jpg')


# image metadata
>>> im
<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=155x207 at 0x1985758>
>>> im.mode
'RGB'
>>> im.size
(155, 207)


# to numpy
im_data = np.array(im)  # incredibly simple!
>>> im_data.shape
(207, 155, 3)           # 207x155 image with (3) RGB channels

# how are values accessed/stored?
# take a miniature version and look
>>> a = np.array([im_data[0][0:4],im_data[1][0:4],im_data[2][0:4]])
# each pixel is a 3-uple
# each row of pixels is stored as an array of 3-uples
# the image is stored as an array of these pixel rows
>>> a
array([[[156, 122, 110],
        [163, 129, 117],
        [165, 133, 120],
        [162, 130, 117]],

       [[156, 122, 110],
        [163, 129, 117],
        [168, 136, 123],
        [169, 137, 124]],

       [[158, 126, 111],
        [163, 131, 116],
        [169, 137, 122],
        [174, 142, 127]]], dtype=uint8)
# or, look at dimensions
# rows
>>> len(im_data[0])
155
>>> len(im_data[1])
155
# columns
>>> len(im_data[:,0])
207
>>> len(im_data[:,1])
207

# one pixel
>>> im_data[206][154]
array([163, 150, 157], dtype=uint8)


# reshape jpg data
im = ImageOps.fit(im, size, Image.ANTIALIAS)


# reshape numpy array
>>> im_data = im_data.T.reshape(3,-1).reshape(-1)
# what's changed?
>>> len(im_data[0])     
155                 # not changed
>>> len(im_data[:,0])
207                 # not changed
>>> im_data[206][154]
array([163, 150, 157], dtype=uint8) # not changed


# to understand convdata.CroppedCIFARDataProvider.__trim_borders(),
# first emulate x, to be datadic['data'] 
# no idea how data is stored, so find out by
# generating hypotheses and running code below
# to see if it works
y = x.reshape(3, 32, 32, x.shape[1])

# hyp1: a batch of shape[1] 32x32 RGB images
# test: with shape[1]==20
>>> batch = np.zeros([3, 20, 32, 32], int)
>>> y= batch.reshape(3,32,32,batch.shape[1])
>>> 
# that works so maybe that's how data is stored
# but this ordering is v strange
# and but maybe other hyps work too.

# hyp2:
batch = np.zeros([32, 20, 32, 3], int)
# also works

# hyp 3:
batch = np.zeros([32, 20, 3, 32], int)
# also works

# hyp 1 most likely because you want all R pixels first, then G pixels, then B pixels

# select a patch!
def patch(tlcoordinates, brcoordinates):
    

