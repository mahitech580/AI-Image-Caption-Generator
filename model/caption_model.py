import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

class CaptionModel:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model.to(self.device)
        self.model.eval()

    def generate_caption(self, image_path: str) -> str:
        image = Image.open(image_path).convert("RGB")
        inputs = self.processor(images=image, return_tensors="pt")
        inputs = {key: value.to(self.device) for key, value in inputs.items()}
        with torch.no_grad():
            output = self.model.generate(**inputs, max_new_tokens=40, num_beams=5, early_stopping=True)
        return self.processor.decode(output[0], skip_special_tokens=True).strip()
