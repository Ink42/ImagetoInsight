from PIL import Image
import pytesseract
 
def load_image():

    image_path = 'rrrrrrrrrr.png'
    image = Image.open(image_path)

    text = pytesseract.image_to_string(image)


    print(text)
    

if __name__=="__main__":
    pass