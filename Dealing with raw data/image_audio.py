#intro to image and audio
from scipy import misc
img=misc.imread('/home/aaaa/Pictures/Wallpapers/19.jpg')
print(type(img))
print(img.shape)
print(img.dtype)
img=img[::2, ::2]
print(img)
img=(img/255.).reshape(-1,4 )
red=img[:,0]
green=img[:,1]
blue=img[:,2]
grey=0.299*red + 0.587*green + 0.114*blue
print(img.shape)
print(grey.shape)
print(img)
print(grey)

import scipy.io.wavfile as wavfile
sample_rate, audio_data=wavfile.read("/home/aaaa/Downloads/movinout.wav")
print(sample_rate)
print(audio_data)

