# PIL: Python Imaging Library

# http://effbot.org/imagingbook/image.htm

# Load Image module
from PIL import Image

# Open jpg file
im = Image.open('pickie.jpg')

# Display image
im.show() # think works

# Resize image
width = 200
height = 100
low_q_im = im.resize((width, height), Image.ANTIALIAS)

# Save newly defined image to file in current directory
low_q_img.save('imgName.jpg')

# Create jpg image (from nparray)
# trick is to start with an image and get its shape
# btw, (I think) max rgb value is 255
import numpy as np
existingImg = Image.open('imgname.jpg') # get jpg data
monoNpImg = np.array(existingImg)       # in np format
monoNpImg[:] = 0                        # make changes
monoImg = Image.fromarray(monoNpImg)    # back into jpg
monoImg.save('mono_1.jpg')              # save




