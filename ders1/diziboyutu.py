# Bu çalışmada dizi boyutu belli olmayan bir resmin boyutunun nasıl bulunacağı anlatılmıştır. 
from pylab import *
from PIL import Image 


im = array(Image.open("resim.jpg").convert("L")) # Resim gray scale olarak açıldı ve diziye dönüştürüldü. 
print("Görüntünün dizi boyutu = ", im.shape)

