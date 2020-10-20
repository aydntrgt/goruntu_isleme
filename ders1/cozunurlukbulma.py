# Bu çalışmada bir resmin çözünürlük değerini bulma anlatılmıştır.

from PIL import Image

goruntu = Image.open("resim.jpg")
cozunurluk=goruntu.info['jfif_density'] # Görüntünün çözünürlük değerini DPI olarak okumak için kullanılır.
print("Çözünürlük = ", cozunurluk)

