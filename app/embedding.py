from flask import Flask
from transformers import CLIPProcessor, CLIPModel
import torch

app = Flask(__name__)

# Load model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch16")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch16")

def get_image_embedding(image):
    #TODO implement
    return ""


def get_text_embedding(text):
    #TODO implement
    return ""
