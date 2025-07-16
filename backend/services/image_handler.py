# from transformers import BlipProcessor, BlipForConditionalGeneration
import io
from PIL import Image
import pytesseract
from ollama import Client

# Set path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

client = Client(host='http://localhost:11434')  # Ollama endpoint

def handle_image_query(file_bytes: bytes) -> str:
    image = Image.open(io.BytesIO(file_bytes)).convert('RGB')
    extracted_text = pytesseract.image_to_string(image)
    
    response = client.chat(
        model="llama2",
        messages=[{"role": "user", "content": f"Summarize this image: {extracted_text}"}]
    )
    
    return response['message']['content']


# processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
# model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# def handle_image_query(file):
#     image = Image.open(io.BytesIO(file)).convert("RGB")
#     inputs = processor(images=image, return_tensors="pt")
#     out = model.generate(**inputs)
#     caption = processor.decode(out[0], skip_special_tokens=True)
#     return caption
