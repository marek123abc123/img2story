import eel
import os
import io
import base64
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from pyllamacpp.model import Model

eel.init('web')

model_path = 'C:/Users/..../AppData/Local/nomic.ai/GPT4All/ggml-v3-13b-hermes-q5_1.bin'
image_caption = ""

@eel.expose
def process_image(image_base64):
    global image_caption

    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    # Convert base64 image to PIL Image
    image_data = base64.b64decode(image_base64.split(',')[1])
    image = Image.open(io.BytesIO(image_data))
    image = image.convert('RGB')

    # Perform image captioning
    text = ""
    inputs = processor(image, text, return_tensors="pt")
    out = model.generate(**inputs)
    image_caption = processor.decode(out[0], skip_special_tokens=True)

    return image_caption

@eel.expose
def generate_story():
    global image_caption

    story = ""
    if image_caption:
        story_model = Model(model_path=model_path)
        for token in story_model.generate("make a fairy tale about: " + image_caption):
            story += token

    return story

eel.start('index.html', size=(500, 400))
