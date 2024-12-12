import bentoml
from bentoml.io import Image, JSON
from transformers import CLIPProcessor, CLIPModel
import numpy as np

# Load the model and processor globally
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Define the BentoML service
vectorization = bentoml.Service(name="clip_image_vectorizer")

@vectorization.api(input=Image(), output=JSON())
def vectorize(image):
    """
    API endpoint to process an image and return its vector representation.
    """
    inputs = processor(images=image, return_tensors="pt")
    outputs = model.get_image_features(**inputs)
    vector = outputs[0].detach().numpy()
    return {"vector": vector.tolist()}
