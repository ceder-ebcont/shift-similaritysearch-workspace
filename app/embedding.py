from flask import Flask
from transformers import CLIPProcessor, CLIPModel
import torch

# Load model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch16")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch16")

def get_image_embedding(image):
    #TODO implement

    return ""


def get_text_embedding(text):   
    inputs = processor(text=[text], return_tensors="pt", padding=True) # Preprocess the text and return PyTorch tensors.
    with torch.no_grad(): # Disable gradient tracking for faster computation and to save memory.
        text_embedding = model.get_text_features(**inputs) # Extract text features
    return text_embedding.numpy().flatten().tolist() # Convert the tensor to a numpy array, flatten it, and return it as a list.
 