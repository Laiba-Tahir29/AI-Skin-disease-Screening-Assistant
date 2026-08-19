<h1 align="center">🩺 AI Skin Disease Screening Assistant</h1>

<p align="center">
  <strong>AI-powered preliminary skin screening using Deep Learning, Computer Vision & RAG</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/TensorFlow-2.x-orange?style=for-the-badge&logo=tensorflow" alt="TensorFlow">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react" alt="React">
  <img src="https://img.shields.io/badge/Vite-Build%20Tool-646CFF?style=for-the-badge&logo=vite" alt="Vite">
  <img src="https://img.shields.io/badge/FAISS-RAG-4B8BBE?style=for-the-badge" alt="FAISS">
</p>

<br>

<p align="center">
  An end-to-end AI/ML web application that analyzes uploaded skin images,
  provides a preliminary screening result, assigns an application-level risk
  category, and provides an AI-powered medical information chatbot.
</p>

---

## ⚠️ Medical Disclaimer

> **This application is NOT a medical diagnostic tool.**
>
> The system provides an AI-generated **preliminary screening result** for educational and experimental purposes. Results should not replace professional medical advice, diagnosis, or treatment from a qualified dermatologist or healthcare professional.

---

# 📌 Table of Contents

* [Project Overview](#-project-overview)
* [Objectives](#-objectives)
* [Key Features](#-key-features)
* [Complete Workflow](#-complete-workflow)
* [System Architecture](#-system-architecture)
* [Dataset](#-dataset)
* [Data Preprocessing](#-data-preprocessing)
* [Model Development](#-model-development)
* [EfficientNetB3](#-efficientnetb3)
* [Model Training](#-model-training)
* [Model Evaluation](#-model-evaluation)
* [MobileNetV2 Object Detection](#-mobilenetv2-object-detection)
* [Confidence & Risk Assessment](#-confidence--risk-assessment)
* [RAG Chatbot](#-rag-chatbot)
* [FAISS Vector Search](#-faiss-vector-search)
* [Gemini Integration](#-gemini-integration)
* [Chatbot Safety Layer](#-chatbot-safety-layer)
* [Frontend](#-frontend)
* [Backend](#-backend)
* [API Endpoints](#-api-endpoints)
* [Project Structure](#-project-structure)
* [Technologies Used](#-technologies-used)
* [Environment Variables](#-environment-variables)
* [Local Installation](#-local-installation)
* [Deployment](#-deployment)
* [Limitations](#-limitations)
* [Future Improvements](#-future-improvements)
* [Conclusion](#-conclusion)

---

# 🧠 Project Overview

The **AI Skin Disease Screening Assistant** is a full-stack AI/ML application designed to provide a preliminary screening of uploaded skin images.

The system combines multiple technologies:

<table>
<tr>
<th>Component</th>
<th>Technology</th>
<th>Purpose</th>
</tr>

<tr>
<td>🧠 Skin Classification</td>
<td><b>EfficientNetB3</b></td>
<td>Predicts the skin-condition category</td>
</tr>

<tr>
<td>🔍 Object Detection</td>
<td><b>MobileNetV2</b></td>
<td>Detects obvious non-skin objects</td>
</tr>

<tr>
<td>💬 AI Chatbot</td>
<td><b>Gemini API</b></td>
<td>Generates contextual responses</td>
</tr>

<tr>
<td>📚 Knowledge Retrieval</td>
<td><b>FAISS</b></td>
<td>Retrieves relevant knowledge</td>
</tr>

<tr>
<td>🔢 Text Embeddings</td>
<td><b>Sentence Transformers</b></td>
<td>Converts questions into vectors</td>
</tr>

<tr>
<td>⚡ Backend</td>
<td><b>FastAPI</b></td>
<td>Handles AI inference and API requests</td>
</tr>

<tr>
<td>🎨 Frontend</td>
<td><b>React + Vite</b></td>
<td>Provides the user interface</td>
</tr>

<tr>
<td>📦 Version Control</td>
<td><b>GitHub</b></td>
<td>Stores and manages source code</td>
</tr>

<tr>
<td>🤗 Model Storage</td>
<td><b>Hugging Face</b></td>
<td>Stores large model weights</td>
</tr>

<tr>
<td>☁️ Backend Deployment</td>
<td><b>Render</b></td>
<td>Hosts the FastAPI backend</td>
</tr>

<tr>
<td>▲ Frontend Deployment</td>
<td><b>Vercel</b></td>
<td>Hosts the React frontend</td>
</tr>

</table>

---

# 🎯 Objectives

The project was developed with the following objectives:

* Build an end-to-end AI/ML healthcare application.
* Train a deep learning model for skin-condition classification.
* Process and validate uploaded images.
* Detect obvious non-skin images before classification.
* Provide prediction confidence.
* Provide an application-level risk category.
* Build an AI-powered medical information chatbot.
* Implement Retrieval-Augmented Generation (RAG).
* Use FAISS for semantic retrieval.
* Add a chatbot safety layer.
* Connect the ML system with a modern web application.
* Deploy the application online.

---

# ✨ Key Features

### 🧠 AI Skin Screening

Upload a skin image and receive a preliminary AI-generated screening result.

### 🔍 Non-Skin Image Detection

MobileNetV2 checks for obvious objects such as:

* Phones
* Laptops
* Cars
* Animals
* Books
* Chairs
* Tables
* Shoes
* Bottles
* Other common objects

### 📊 Confidence Score

The application displays the confidence associated with the predicted class.

### 🚦 Risk Classification

Predictions are mapped to application-level:

* HIGH
* MEDIUM
* LOW

risk categories.

### 💬 AI Chatbot

Users can ask questions about the screening result and related skin conditions.

### 📚 RAG Knowledge Retrieval

The chatbot retrieves relevant information from a custom knowledge base before generating its response.

### 🛡️ Safety Layer

User messages are checked before continuing through the chatbot pipeline.

### 🌐 Full-Stack Architecture

The project combines:

```text
React
   ↓
Axios
   ↓
FastAPI
   ↓
Machine Learning Models
   ↓
Prediction
```

and:

```text
User Question
   ↓
Safety
   ↓
Embeddings
   ↓
FAISS
   ↓
Knowledge Base
   ↓
Gemini
   ↓
Response
```

---

# 🔄 Complete Workflow

The complete project workflow is:

```text
                    ┌──────────────────────┐
                    │    DermNet Dataset   │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Data Cleaning &      │
                    │ Preprocessing        │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Data Augmentation    │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ EfficientNetB3        │
                    │ Training + Fine-tune │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Model Evaluation     │
                    └──────────┬───────────┘
                               ↓
                        Trained Weights
                               ↓
        ┌──────────────────────┴──────────────────────┐
        ↓                                             ↓
┌───────────────────┐                       ┌───────────────────┐
│    MobileNetV2    │                       │  EfficientNetB3   │
│ Non-Skin Check    │                       │ Skin Prediction   │
└─────────┬─────────┘                       └─────────┬─────────┘
          └──────────────────┬────────────────────────┘
                             ↓
                    ┌───────────────────┐
                    │   FastAPI Backend │
                    └─────────┬─────────┘
                              ↓
                    ┌───────────────────┐
                    │ Confidence + Risk │
                    └─────────┬─────────┘
                              ↓
                    ┌───────────────────┐
                    │   React Frontend  │
                    └───────────────────┘
```

---

# 🏗️ System Architecture

```text
                         USER
                          │
                          ▼
                 ┌─────────────────┐
                 │ React Frontend  │
                 │    + Vite       │
                 └────────┬────────┘
                          │
                        Axios
                          │
                          ▼
                 ┌─────────────────┐
                 │ FastAPI Backend │
                 └────────┬────────┘
                          │
             ┌────────────┴────────────┐
             │                         │
             ▼                         ▼
    ┌─────────────────┐       ┌─────────────────┐
    │  Skin Screening │       │    Chatbot      │
    │     Pipeline    │       │      RAG        │
    └────────┬────────┘       └────────┬────────┘
             │                         │
       ┌─────┴─────┐              ┌────┴────┐
       │           │              │         │
       ▼           ▼              ▼         ▼
 MobileNet   EfficientNet       FAISS    Gemini
    V2           B3
       │           │              │
       └─────┬─────┘              │
             │                    │
             ▼                    ▼
      Prediction + Risk       Chat Response
             │                    │
             └─────────┬──────────┘
                       ▼
                  USER RESULT
```

---

# 📊 Dataset

The model was trained using a dermatology image dataset based on **DermNet**.

### Dataset Statistics

| Property          |     Value |
| ----------------- | --------: |
| Categories        |        23 |
| Files identified  |   ~15,557 |
| Training images   |    12,446 |
| Validation images |     3,111 |
| Image size        | 224 × 224 |
| Channels          |       RGB |

A separate test set was used to evaluate the trained models.

---

# 🧹 Data Preprocessing

Images were prepared before being passed to the model.

### Image Processing

Each image was:

1. Loaded using PIL.
2. Converted to RGB.
3. Resized to `224 × 224`.
4. Converted into numerical image data.
5. Preprocessed for EfficientNet.

### Data Augmentation

The training pipeline included:

```text
Random Horizontal Flip
Random Rotation
Random Zoom
Random Contrast
Random Brightness
```

Augmentation helps expose the model to different variations in image appearance.

---

# 🧠 Model Development

Different deep-learning approaches were explored during development.

The project experimented with architectures including:

* EfficientNet
* ResNet

The final system uses:

## EfficientNetB3

EfficientNetB3 was selected as the primary skin-condition classifier.

---

# 🧬 EfficientNetB3

The model architecture used in the application is:

```text
Input
  ↓
Data Augmentation
  ↓
EfficientNetB3
  ↓
Global Average Pooling
  ↓
Dropout
  ↓
Dense Layer
  ↓
Softmax
  ↓
23 Classes
```

The EfficientNetB3 base was created without its original classification head.

A custom classification head was then added.

The final Dense layer contains:

```text
Number of neurons = number of classes
```

The class names are loaded from:

```text
class_names.pkl
```

---

# 🔬 Model Training

The training process used **transfer learning** followed by **fine-tuning**.

## Phase 1 — Feature Extraction

The EfficientNetB3 base layers were initially frozen.

The classification head was trained first.

```text
EfficientNetB3
      ↓
Frozen Feature Extractor
      ↓
Trainable Classification Head
```

## Phase 2 — Fine-Tuning

Selected layers were then unfrozen.

A smaller learning rate was used to allow the model to adapt gradually to the dermatology dataset.

Additional experiments included:

* Different fine-tuning depths
* Batch Normalization freezing
* Class weights
* Different learning rates
* Different training configurations

---

# 📈 Model Evaluation

Multiple model configurations were evaluated during development.

The best recorded configuration achieved:

<table>
<tr>
<td><b>Test Accuracy</b></td>
<td><b>47.60%</b></td>
</tr>
<tr>
<td><b>Test Loss</b></td>
<td><b>1.8260</b></td>
</tr>
</table>

These numbers represent performance on the project's test dataset.

### Why accuracy is not enough

A healthcare image classifier must be evaluated carefully because:

* Visual appearance of diseases can overlap.
* Real-world images vary greatly.
* Lighting and camera quality affect images.
* Dataset diversity affects generalization.
* Some conditions have fewer representative examples.
* A model's test accuracy does not equal clinical reliability.

Therefore, the application is designed for **preliminary screening**, not diagnosis.

---

# 🔍 MobileNetV2 Object Detection

A second model was added to improve input validation.

## Why MobileNetV2?

The skin classifier could technically receive any image.

For example:

```text
Laptop image
      ↓
EfficientNetB3
      ↓
Forced to choose a skin-condition class
```

This is undesirable.

To reduce this problem, MobileNetV2 is used as an additional object-recognition layer.

```text
Uploaded Image
      ↓
MobileNetV2
      ↓
Top 5 Predictions
      ↓
Compare against Non-Skin Keywords
      ↓
Obvious Non-Skin Object?
      ↓
Yes → Reject
No  → Continue
```

The application checks for common objects such as:

```text
bottle
phone
laptop
computer
chair
table
car
dog
cat
book
shoe
keyboard
mouse
camera
tablet
and others
```

The object detector is therefore a **validation layer**, not a medical classifier.

---

# 🎯 Confidence & Risk Assessment

After EfficientNetB3 produces its predictions, the class with the highest probability is selected.

```text
Model Predictions
       ↓
Highest Probability
       ↓
Predicted Class
       ↓
Confidence %
```

The backend then maps the predicted condition to an application-level risk category.

### High Risk

Current examples include:

* Melanoma Skin Cancer / Nevi and Moles
* Actinic Keratosis / Basal Cell Carcinoma and other malignant lesions

### Medium Risk

Current examples include:

* Lupus and other connective tissue diseases
* Systemic Disease
* Vasculitis Photos
* Bullous Disease Photos

### Low Risk

Other classes currently fall into the application's LOW category.

> **Important:** These categories are application-level screening labels and are not clinical risk assessments.

---

# 💬 RAG Chatbot

The application also includes an AI chatbot.

The chatbot uses **Retrieval-Augmented Generation (RAG)**.

Instead of directly sending every user question to Gemini, the application first searches a custom knowledge base.

---

# 🔄 RAG Workflow

```text
                 User Question
                       ↓
                Safety Check
                       ↓
              Text Embedding
                       ↓
                FAISS Search
                       ↓
             Top Relevant Chunks
                       ↓
              Prompt Construction
                       ↓
                 Gemini API
                       ↓
              Generated Response
```

---

# 🔢 Text Embeddings

The user's question is converted into a numerical vector.

The project uses an embedding pipeline producing:

```text
384-dimensional vectors
```

Example:

```text
"What is eczema?"
        ↓
Embedding Model
        ↓
[384-dimensional vector]
```

This vector is then used for semantic similarity search.

---

# 🔎 FAISS Vector Search

FAISS is used to search the knowledge base.

The project stores:

```text
chatbot/
└── vector_db/
    ├── knowledge_base.index
    └── documents.json
```

### Configuration

```text
Embedding Dimensions: 384
Top K Results: 3
```

The system retrieves the three most relevant chunks for the user's question.

---

# 📚 Knowledge Base

The vector database contains the project's stored knowledge.

`knowledge_base.index` stores vector representations.

`documents.json` stores the corresponding original text.

The retrieved documents are inserted into the chatbot prompt.

This creates a grounded generation pipeline:

```text
Question
   ↓
Search Knowledge Base
   ↓
Relevant Information
   ↓
Gemini
   ↓
Response
```

---

# 🤖 Gemini Integration

After retrieval, the system builds a safety-aware prompt containing:

* User question
* Current screening condition
* Retrieved knowledge
* Safety instructions

The prompt is sent to Gemini through the Google GenAI SDK.

Gemini generates the final natural-language response.

---

# 🛡️ Chatbot Safety Layer

A safety layer was added before the normal chatbot pipeline.

The system checks whether a user message contains blocked content.

```text
User Message
     ↓
Safety Check
     ↓
Blocked?
  ↙       ↘
YES       NO
 ↓         ↓
Safety    RAG
Response  Pipeline
```

This provides an additional layer of protection around chatbot interactions.

The chatbot also uses a safety-aware prompt when generating responses.

---

# ⚡ Backend

The backend was developed using **FastAPI**.

FastAPI is responsible for:

* Receiving image uploads
* Validating images
* Running MobileNetV2
* Running EfficientNetB3
* Calculating confidence
* Assigning risk levels
* Handling chatbot requests
* Communicating with the frontend

---

# 🌐 API Endpoints

## `GET /`

Health-check endpoint.

### Response

```json
{
  "message": "API running"
}
```

---

## `POST /predict`

Accepts an image file and performs the screening pipeline.

### Processing

```text
Upload
 ↓
Read File
 ↓
Validate Image
 ↓
MobileNetV2 Check
 ↓
EfficientNetB3
 ↓
Confidence
 ↓
Risk Level
 ↓
JSON Response
```

### Example Response

```json
{
  "disease": "Predicted Condition",
  "confidence": 72.45,
  "risk_level": "MEDIUM",
  "disclaimer": "This is an AI-generated screening result..."
}
```

---

## `POST /chat`

Receives a chatbot message.

### Request

```json
{
  "message": "What does this condition mean?",
  "condition": "Predicted Condition"
}
```

### Response

```json
{
  "response": "AI generated response..."
}
```

---

# 🎨 Frontend

The frontend was developed using:

* React
* Vite
* React Router
* Axios

The frontend provides the user interface for:

* Home page
* Image screening
* Results
* About page
* Chatbot interaction

### Frontend Flow

```text
             User
               ↓
        React Interface
               ↓
         Upload Image
               ↓
             Axios
               ↓
        FastAPI Backend
               ↓
          AI Pipeline
               ↓
          JSON Result
               ↓
        Result Interface
```

---

# 🔗 Frontend ↔ Backend Communication

Axios is used for API communication.

During local development:

```text
Frontend
http://localhost:5173
        │
        │ Axios
        ▼
Backend
http://127.0.0.1:8000
```

For deployment, the backend URL is stored in an environment variable:

```text
VITE_API_URL
```

This avoids hardcoding the production backend URL into the frontend.

---

# 🗂️ Project Structure

```text
AI-Skin-Screening-Assistant/
│
├── skin_backend/
│   │
│   ├── main.py
│   ├── requirements.txt
│   ├── class_names.pkl
│   ├── config.pkl
│   │
│   └── chatbot/
│       ├── rag.py
│       ├── embeddings.py
│       ├── safety.py
│       │
│       └── vector_db/
│           ├── knowledge_base.index
│           └── documents.json
│
├── skin_frontend/
│   │
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   ├── Screen.jsx
│   │   │   ├── Result.jsx
│   │   │   ├── About.jsx
│   │   │   └── chatbot.jsx
│   │   │
│   │   ├── services/
│   │   └── App.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

# 🧰 Technologies Used

## Machine Learning

<table>
<tr>
<th>Technology</th>
<th>Purpose</th>
</tr>

<tr>
<td>Python</td>
<td>ML and backend development</td>
</tr>

<tr>
<td>TensorFlow / Keras</td>
<td>Deep learning</td>
</tr>

<tr>
<td>EfficientNetB3</td>
<td>Skin-condition classification</td>
</tr>

<tr>
<td>MobileNetV2</td>
<td>General object recognition</td>
</tr>

<tr>
<td>NumPy</td>
<td>Numerical computation</td>
</tr>

<tr>
<td>PIL</td>
<td>Image processing</td>
</tr>
</table>

## Backend

<table>
<tr>
<th>Technology</th>
<th>Purpose</th>
</tr>

<tr>
<td>FastAPI</td>
<td>REST API backend</td>
</tr>

<tr>
<td>Uvicorn</td>
<td>ASGI server</td>
</tr>

<tr>
<td>Pydantic</td>
<td>Request validation</td>
</tr>

<tr>
<td>python-dotenv</td>
<td>Environment variables</td>
</tr>

<tr>
<td>Requests</td>
<td>Model weight download</td>
</tr>
</table>

## RAG / Generative AI

<table>
<tr>
<th>Technology</th>
<th>Purpose</th>
</tr>

<tr>
<td>FAISS</td>
<td>Vector similarity search</td>
</tr>

<tr>
<td>Sentence Transformers</td>
<td>Text embeddings</td>
</tr>

<tr>
<td>Google GenAI / Gemini</td>
<td>Response generation</td>
</tr>
</table>

## Frontend

<table>
<tr>
<th>Technology</th>
<th>Purpose</th>
</tr>

<tr>
<td>React</td>
<td>User interface</td>
</tr>

<tr>
<td>Vite</td>
<td>Development and build tooling</td>
</tr>

<tr>
<td>React Router</td>
<td>Client-side routing</td>
</tr>

<tr>
<td>Axios</td>
<td>API communication</td>
</tr>
</table>

## Deployment

<table>
<tr>
<th>Technology</th>
<th>Purpose</th>
</tr>

<tr>
<td>GitHub</td>
<td>Source code and version control</td>
</tr>

<tr>
<td>Hugging Face</td>
<td>Large model-weight storage</td>
</tr>

<tr>
<td>Render</td>
<td>FastAPI backend hosting</td>
</tr>

<tr>
<td>Vercel</td>
<td>React frontend hosting</td>
</tr>
</table>

---

# 🔐 Environment Variables

API keys are stored using environment variables instead of being hardcoded.

## Backend

Create:

```text
.env
```

Example:

```env
GEMINI_API_KEY=your_api_key_here
```

## Frontend

Example:

```env
VITE_API_URL=http://127.0.0.1:8000
```

For production:

```env
VITE_API_URL=https://your-backend.onrender.com
```

> Never commit API keys or `.env` files containing secrets to GitHub.

---

# 📦 Model Storage

The trained model weights are stored separately:

```text
best_model_b3_final.weights.h5
```

The weights are hosted on Hugging Face because the file is relatively large.

At backend startup:

```text
Backend starts
      ↓
Check local model file
      ↓
File exists?
   ↙       ↘
 YES       NO
 ↓          ↓
Load      Download
weights   from Hugging Face
              ↓
         Save locally
              ↓
         Load weights
```

The EfficientNetB3 architecture is recreated in the backend before the weights are loaded.

---

# 🚀 Deployment Architecture

The final deployment uses separate services for the frontend and backend.

```text
                      USER
                        │
                        ▼
                ┌───────────────┐
                │    Vercel     │
                │ React + Vite  │
                └───────┬───────┘
                        │
                      Axios
                        │
                        ▼
                ┌───────────────┐
                │    Render     │
                │    FastAPI    │
                └───────┬───────┘
                        │
          ┌─────────────┼─────────────┐
          │             │             │
          ▼             ▼             ▼
   EfficientNetB3   MobileNetV2     RAG
          │             │             │
          │             │        ┌────┴────┐
          │             │        ▼         ▼
          │             │      FAISS    Gemini
          │
          ▼
    Skin Prediction
          │
          ▼
   Risk + Confidence
```

---

# 🤗 Hugging Face Model Storage

The trained model weights are stored in a Hugging Face repository.

The backend downloads the weights when required.

This keeps the large model file separate from the main source-code repository.

---

# 🛠️ Local Installation

## 1. Clone Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>

cd AI-Skin-Screening-Assistant
```

---

## 2. Backend

```bash
cd skin_backend
```

Create a Conda environment:

```bash
conda create -n skinapp python=3.11
```

Activate:

```bash
conda activate skinapp
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env`:

```env
GEMINI_API_KEY=your_api_key_here
```

Start backend:

```bash
uvicorn main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

---

# 💻 Frontend Setup

Open another terminal:

```bash
cd skin_frontend
```

Install dependencies:

```bash
npm install
```

Create:

```text
.env
```

Add:

```env
VITE_API_URL=http://127.0.0.1:8000
```

Start:

```bash
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# 🧪 Testing Workflow

A complete local test follows:

```text
1. Start FastAPI
       ↓
2. Start React
       ↓
3. Open application
       ↓
4. Upload image
       ↓
5. Validate image
       ↓
6. MobileNetV2 object check
       ↓
7. EfficientNetB3 prediction
       ↓
8. Calculate confidence
       ↓
9. Assign risk category
       ↓
10. Display result
       ↓
11. Ask chatbot question
       ↓
12. Safety check
       ↓
13. Generate embedding
       ↓
14. Search FAISS
       ↓
15. Retrieve knowledge
       ↓
16. Send context to Gemini
       ↓
17. Display chatbot response
```

---

# ⚠️ Limitations

## Model Performance

The best recorded test accuracy was approximately:

```text
47.60%
```

Therefore, the model should not be treated as clinically reliable.

## Dataset

The model depends on the quality and diversity of its training data.

The dataset may not represent:

* Every skin tone
* Every camera type
* Every lighting condition
* Every geographical population
* Every real-world presentation of a disease

## Object Detection

MobileNetV2 is a general object-recognition model.

It cannot determine whether an image is medically suitable for diagnosis.

It primarily helps reject obvious non-skin objects.

## Chatbot

The chatbot may produce incorrect or incomplete information.

RAG improves grounding but does not guarantee perfect factual accuracy.

## Hosting

TensorFlow, EfficientNetB3, MobileNetV2, FAISS, and embedding models can require significant memory and computational resources.

---

# 🔮 Future Improvements

Future versions could include:

* Larger and more diverse dermatology datasets
* Better dataset cleaning
* Improved class balancing
* More advanced image preprocessing
* Model calibration
* Better uncertainty detection
* Skin segmentation
* Dedicated skin-image quality assessment
* Improved object detection
* Additional medical knowledge sources
* More advanced RAG retrieval
* Source citations in chatbot responses
* Better hallucination control
* GPU-based production infrastructure
* Clinical validation with medical professionals

---

# 📊 Final Pipeline Summary

```text
                 ┌─────────────────┐
                 │     DermNet     │
                 │     Dataset     │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Preprocessing   │
                 │ + Augmentation  │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ EfficientNetB3  │
                 │ Training        │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Fine-Tuning     │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Model Evaluation│
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │  Model Weights  │
                 └────────┬────────┘
                          ↓
             ┌────────────┴────────────┐
             ↓                         ↓
      ┌─────────────┐          ┌──────────────┐
      │ MobileNetV2 │          │ EfficientNet │
      │ Object Check│          │     B3       │
      └──────┬──────┘          └──────┬───────┘
             └────────────┬───────────┘
                          ↓
                   ┌─────────────┐
                   │   FastAPI   │
                   └──────┬──────┘
                          ↓
              ┌──────────────────────┐
              │ Confidence + Risk    │
              └──────────┬───────────┘
                         ↓
                  ┌─────────────┐
                  │ React + Vite│
                  └─────────────┘


                 CHATBOT PIPELINE

                User Question
                      ↓
                Safety Check
                      ↓
               Text Embedding
                      ↓
                  FAISS
                      ↓
             Knowledge Retrieval
                      ↓
             Contextual Prompt
                      ↓
                  Gemini
                      ↓
              Final Response
```

---

# 🧑‍💻 Development Summary

This project combines machine learning, backend engineering, frontend development, retrieval systems, generative AI, and deployment into a single application.

The development process involved:

```text
Dataset Collection
        ↓
Data Preparation
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Model Integration
        ↓
Object Detection
        ↓
Risk System
        ↓
FastAPI Backend
        ↓
RAG Chatbot
        ↓
React Frontend
        ↓
GitHub
        ↓
Hugging Face
        ↓
Render
        ↓
Vercel
```

---

# 🏁 Conclusion

The **AI Skin Disease Screening Assistant** demonstrates an end-to-end approach to building an AI-powered healthcare application.

The project combines:

**Deep Learning**

→ EfficientNetB3

**Computer Vision**

→ MobileNetV2

**Backend Development**

→ FastAPI

**Retrieval-Augmented Generation**

→ Embeddings + FAISS

**Generative AI**

→ Gemini

**Frontend Development**

→ React + Vite

**Deployment**

→ GitHub + Hugging Face + Render + Vercel

The application is designed as a **preliminary screening and educational system**, with the goal of demonstrating how machine learning and generative AI can be integrated into a complete web application.

---

<p align="center">
  <strong>🩺 AI Skin Disease Screening Assistant</strong>
  <br>
  Built with Deep Learning, RAG & Generative AI
</p>

<p align="center">
  <i>For educational and preliminary screening purposes only.</i>
</p>
