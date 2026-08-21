from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
import numpy as np
import requests
from PIL import Image
import io
from dotenv import load_dotenv
import os
import pickle
load_dotenv()  


from pydantic import BaseModel
from chatbot.rag import get_chatbot_response

MODEL_PATH = "best_model_b3_final.weights.h5"
MODEL_URL ="https://huggingface.co/Laibatahir/dermascan-b3-weights/resolve/main/best_model_b3_final.weights.h5"


if not os.path.exists(MODEL_PATH):
    print("Downloading model weights...")
    with requests.get(MODEL_URL, stream=True) as r:
        r.raise_for_status()
        with open(MODEL_PATH, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print("Model downloaded!")
    
app = FastAPI()


class ChatRequest(BaseModel):
    message: str
    condition: str = ""


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================
# Load Config
# ==========================

with open('class_names.pkl', 'rb') as f:
    class_names = pickle.load(f)

with open('config.pkl', 'rb') as f:
    config = pickle.load(f)

IMG_SIZE = config['IMG_SIZE']


# ==========================
# Skin Disease Model
# ==========================

data_augmentation = tf.keras.Sequential([
    tf.keras.layers.RandomFlip("horizontal"),
    tf.keras.layers.RandomRotation(0.15),
    tf.keras.layers.RandomZoom(0.15),
    tf.keras.layers.RandomContrast(0.15),
    tf.keras.layers.RandomBrightness(0.15),
])

base_model = tf.keras.applications.EfficientNetB3(
    include_top=False,
    weights=None,
    input_shape=(IMG_SIZE, IMG_SIZE, 3)
)

model = tf.keras.Sequential([
    data_augmentation,
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(
        len(class_names),
        activation="softmax"
    )
])

model.build(
    input_shape=(None, IMG_SIZE, IMG_SIZE, 3)
)

model.load_weights(
    "best_model_b3_final.weights.h5"
)

print("Skin model loaded!")


# ==========================
# MobileNet Object Detector
# ==========================

print("Loading MobileNet...")

general_model = tf.keras.applications.MobileNetV2(
    weights="imagenet"
)

print("MobileNet loaded!")


# ==========================
# Risk Mapping
# ==========================

HIGH_RISK = [
    "Melanoma Skin Cancer Nevi and Moles",
    "Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions"
]

MEDIUM_RISK = [
    "Lupus and other Connective Tissue diseases",
    "Systemic Disease",
    "Vasculitis Photos",
    "Bullous Disease Photos"
]


def get_risk_level(disease):
    if disease in HIGH_RISK:
        return "HIGH"
    elif disease in MEDIUM_RISK:
        return "MEDIUM"
    return "LOW"


# ==========================
# Non Skin Keywords
# ==========================

non_skin_keywords = [
    "bottle", "jar", "can", "cup", "box", "carton",
    "bag", "basket", "bucket", "envelope", "container", "book", "paper", "notebook", "folder","page","screenshort","screenshot","screen shot","screencap","screencapture","screengrab",

    "chair", "table", "desk", "sofa", "bed",

    "laptop", "phone", "computer",
    "monitor", "keyboard", "mouse",
    "camera", "tablet","paper_towel","book_jacket","car_wheel",

    "car", "vehicle", "bicycle",
    "motorcycle", "truck", "bus",

    "dog", "cat", "bird", "horse",
    "cow", "elephant",

    "banana", "apple", "pizza",
    "cake", "bread",

    "book", "shoe", "umbrella",
    "clock", "watch", "glasses",

    "shirt", "jacket", "jean", "sock"
]


# ==========================
# Object Check Function
# ==========================

def is_non_skin_object(image):
    try:
        img_resized = image.resize((224, 224))

        img_array = tf.keras.applications.mobilenet_v2.preprocess_input(
            np.expand_dims(
                np.array(img_resized).astype(np.float32),
                axis=0
            )
        )

        preds = general_model.predict(
            img_array,
            verbose=0
        )

        decoded = tf.keras.applications.mobilenet_v2.decode_predictions(
            preds,
            top=5
        )[0]

        print("MobileNet prediction:", decoded)

        for _, label, confidence in decoded:
            if (
                any(keyword in label.lower()
                    for keyword in non_skin_keywords)
                and confidence > 0.15
            ):
                return True, label, float(confidence)

        return False, None, None

    except Exception as e:
        print("MobileNet error:", e)

        # Don't crash the whole API
        return False, None, None


# ==========================
# Routes
# ==========================

@app.get("/")
def read_root():
    return {
        "message": "API running"
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()

    # Empty file
    if not contents:
        return {
            "error": True,
            "message": "No file uploaded. Please upload an image."
        }

    # Corrupt / invalid image
    try:
        image = Image.open(io.BytesIO(contents)).convert("RGB")
    except Exception:
        return {
            "error": True,
            "message": "Invalid or corrupted file. Please upload a valid image."
        }

    # ==========================
    # Non Skin Check
    # ==========================

    is_object, detected_label, obj_confidence = is_non_skin_object(image)

    if is_object:
        return {
            "error": True,
            "message": f"This does not appear to be a skin image. Detected object: {detected_label}"
        }

    # ==========================
    # Skin Prediction
    # ==========================

    image_resized = image.resize((IMG_SIZE, IMG_SIZE))

    img_array = np.array(image_resized)
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(
        img_array,
        verbose=0
    )[0]

    predicted_index = np.argmax(predictions)

    confidence = round(
        float(predictions[predicted_index]) * 100,
        2
    )

    disease = class_names[predicted_index]

    return {
        "disease": disease,
        "confidence": confidence,
        "risk_level": get_risk_level(disease),
        "disclaimer": "This is an AI-generated screening result, not a medical diagnosis. Please consult a certified dermatologist for accurate diagnosis and treatment."
    }

    
@app.post("/chat")
def chat(request: ChatRequest):
    response = get_chatbot_response(
        user_message=request.message,
        condition=request.condition
    )

    return {
        "response": response
    }

