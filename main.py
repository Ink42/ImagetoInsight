from PIL import Image
import pytesseract
from transformers import pipeline

model ="Falconsai/text_summarization"
task ="summarization"

def load_image(image_path:str):
    image = Image.open(image_path)
    text:str = pytesseract.image_to_string(image)
    return summarizer(text)

def summarizer(text:str)-> str:
    # Is i encounted here was that it would not return an interger rather it would return a float causing errors hence the reason i ended up using round to turn the output into a whole number

    max_length:int = round(len(text.split(" ")) / 2)
    min_length:int = round(max_length/2)
    summarizer = pipeline(task, model=model)
    return summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']

if __name__=="__main__":
   print(load_image("sample_images/ww.jpeg"))