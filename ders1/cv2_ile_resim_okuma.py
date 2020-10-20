import cv2 
from pylab import*
import PIL

goruntu = cv2.imread("resim.jpg") # OpenCv kütüphanesindeki imread komutu ile resmi oku. 
cv2.imshow("Orjinal Goruntu",goruntu) # Resmi pencerede göster. 
lineer_interpolasyon = cv2.resize(goruntu,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_LINEAR)
bicubic_interpolasyon=cv2.resize(goruntu,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_CUBIC )
cv2.imshow("Linear Interpolasyon",lineer_interpolasyon)
cv2.imshow("Bicubic Interpolasyon",bicubic_interpolasyon)
alan_interpolasyon=cv2.resize(goruntu,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA )

goruntu=PIL.Image.open("resim.jpg")
K_nn_interpolasyon=goruntu.resize((300,400),resample=PIL.Image.NEAREST)
cv2.imshow("AREA Interpolasyon",alan_interpolasyon)
K_nn_interpolasyon.show()