# 🖼️ AI Image Caption Generator

> An AI-powered web application that analyzes uploaded images and automatically generates natural-language captions using a pre-trained BLIP vision-language model.

**Built by Mahendra Kondaveeti**

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask)](https://flask.palletsprojects.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-ee4c2c?logo=pytorch)](https://pytorch.org/)
[![Transformers](https://img.shields.io/badge/Hugging%20Face-Transformers-yellow?logo=huggingface)](https://huggingface.co/docs/transformers)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📌 Overview

**AI Image Caption Generator** is a full-stack computer vision application that converts visual content into natural-language descriptions.

Users can upload an image through a web interface, and the application processes the image with a pre-trained **BLIP (Bootstrapping Language-Image Pre-training)** model to generate an AI-based caption.

Generated captions are stored in a local **SQLite database**, allowing users to view and manage their caption history.

The project combines:

* Computer Vision
* Vision-Language Models
* Deep Learning
* Natural Language Generation
* REST API development
* Web application development
* Database persistence

---

## ✨ Features

### 🤖 AI Caption Generation

Upload an image and generate a natural-language description using a pre-trained BLIP model.

### 🖼️ Image Upload

Supports common image formats:

* JPG
* JPEG
* PNG
* WEBP

### 👀 Image Preview

Preview the selected image before sending it for AI processing.

### ⚡ Processing Time

Displays the approximate AI inference time for each generated caption.

### 📋 Copy Caption

Copy the generated caption directly to the clipboard.

### ⬇️ Download Caption

Download the generated caption as a text file.

### 🔄 Regenerate

Generate a caption again for the selected image.

### 🗃️ Caption History

Generated captions are stored in SQLite with:

* Filename
* Caption
* Processing time
* Creation timestamp

### 🗑️ Delete History

Remove individual records from caption history.

### 🔌 REST API

The application provides API endpoints for:

* Health checks
* Caption generation
* Caption history
* History deletion

### 🛡️ Input Validation

The application validates:

* File type
* File size
* Empty uploads
* Invalid requests

---

## 🏗️ Architecture

```text
                         ┌──────────────────────┐
                         │       User           │
                         │   Uploads Image      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   HTML / CSS / JS    │
                         │      Frontend        │
                         └──────────┬───────────┘
                                    │
                                    │ POST /api/caption
                                    ▼
                         ┌──────────────────────┐
                         │       Flask          │
                         │      Backend         │
                         └──────────┬───────────┘
                                    │
                            Validate Image
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   BLIP Processor     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      BLIP Model      │
                         │       PyTorch        │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │  Generated Caption   │
                         └──────────┬───────────┘
                                    │
                         ┌──────────┴───────────┐
                         │                      │
                         ▼                      ▼
                ┌─────────────────┐    ┌─────────────────┐
                │   SQLite DB     │    │    Frontend     │
                │ Caption History │    │ Display Result  │
                └─────────────────┘    └─────────────────┘
```

---

## 🧰 Tech Stack

| Technology                | Purpose                   |
| ------------------------- | ------------------------- |
| Python                    | Core programming language |
| Flask                     | Web backend and REST API  |
| PyTorch                   | Deep learning framework   |
| Hugging Face Transformers | Model and processor       |
| BLIP                      | Image captioning model    |
| Pillow                    | Image processing          |
| SQLite                    | Caption history database  |
| HTML                      | Page structure            |
| CSS                       | UI styling                |
| JavaScript                | Frontend interaction      |
| Pytest                    | API testing               |

---

## 🧠 AI Model

This project uses:

**`Salesforce/blip-image-captioning-base`**

BLIP is a vision-language model designed for image understanding and image-to-text generation.

The application uses the pre-trained model rather than training a large image-captioning model from scratch.

### Inference Flow

```text
Input Image
     ↓
RGB Conversion
     ↓
BLIP Processor
     ↓
Tensor Representation
     ↓
BLIP Model
     ↓
Token Generation
     ↓
Token Decoding
     ↓
Natural-Language Caption
```

---

## 📂 Project Structure

```text
AI-Image-Caption-Generator/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── model/
│   └── caption_model.py
│
├── database/
│   └── database.py
│
├── utils/
│   └── validators.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
├── uploads/
│   └── .gitkeep
│
└── tests/
    └── test_api.py
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/mahitech580/AI-Image-Caption-Generator.git
```

```bash
cd AI-Image-Caption-Generator
```

---

### 2. Create a virtual environment

#### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

#### macOS / Linux

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

---

### 4. Run the application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

## ⚠️ First Run

On the first startup, Hugging Face downloads the pre-trained BLIP model.

The model is approximately **1 GB**, so the first launch may take longer and requires an internet connection.

After the model has been cached locally, subsequent launches normally reuse the cached files.

---

## 🔌 API Documentation

### Health Check

```http
GET /api/health
```

Example response:

```json
{
  "success": true,
  "status": "healthy",
  "device": "cpu"
}
```

---

### Generate Caption

```http
POST /api/caption
```

Send an image using `multipart/form-data`.

Field:

```text
image=<image-file>
```

Example response:

```json
{
  "success": true,
  "filename": "dog.jpg",
  "caption": "a dog running through a grassy field",
  "processing_time": 2.84
}
```

---

### Get Caption History

```http
GET /api/history
```

Example:

```json
{
  "success": true,
  "history": []
}
```

---

### Delete History Item

```http
DELETE /api/history/<id>
```

Example:

```text
DELETE /api/history/5
```

---

## 🗄️ Database

The application automatically creates:

```text
caption_history.db
```

with the following table:

### `caption_history`

| Column          | Type    | Description          |
| --------------- | ------- | -------------------- |
| id              | INTEGER | Primary key          |
| filename        | TEXT    | Uploaded filename    |
| caption         | TEXT    | Generated caption    |
| processing_time | REAL    | Model inference time |
| created_at      | TEXT    | Creation timestamp   |

---

## 🧪 Testing

Run the test suite:

```bash
pytest
```

The tests currently cover basic application and API behavior, including:

* Home page
* Health endpoint
* Missing-image validation

---

## 🔒 Validation & Error Handling

The application checks uploaded files before processing.

### Supported extensions

```text
.jpg
.jpeg
.png
.webp
```

### Maximum upload size

```text
10 MB
```

The application also handles invalid requests and AI processing failures without exposing internal error details to the user.

---

## 💻 CPU & GPU

The application automatically checks whether CUDA is available.

```python
device = "cuda" if torch.cuda.is_available() else "cpu"
```

Therefore, the model can run on:

```text
CPU
```

or:

```text
CUDA-compatible GPU
```

depending on the local PyTorch environment.

CPU inference will generally take longer than GPU inference.

---

## 📸 Example

```text
User uploads image
        ↓
AI analyzes image
        ↓
Generated caption
        ↓
"A dog is running through a grassy field."
```

---

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

* Python application development
* Flask backend development
* REST API design
* Computer vision
* Vision-language models
* PyTorch inference
* Hugging Face Transformers
* Image preprocessing
* SQLite database integration
* Frontend/backend integration
* File validation
* Automated testing
* Git and GitHub workflow

---

## 🔮 Future Improvements

Possible extensions include:

* Multiple caption generation strategies
* Caption length controls
* More advanced vision-language models
* User authentication
* Cloud database support
* Image history management
* Docker containerization
* Production WSGI deployment
* Cloud deployment
* API documentation with Swagger/OpenAPI
* Performance benchmarking
* Batch image captioning

---

## ⚠️ Limitations

This project uses a pre-trained image-captioning model. Generated captions may occasionally:

* Miss visible details
* Describe an object incorrectly
* Produce incomplete descriptions
* Interpret ambiguous scenes incorrectly

The generated caption should therefore be treated as an AI prediction rather than guaranteed ground truth.

---

## 🔐 Privacy

Uploaded images are processed locally by the application when running locally.

The application does not include a third-party image storage service by default.

Temporary uploaded files are removed after processing, while caption metadata is stored in the local SQLite database.

---

## 📜 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.

---

## 👨‍💻 Author

**Mahendra Kondaveeti**

Computer Science Engineering Graduate
Interested in:

* Artificial Intelligence
* Machine Learning
* Data Science
* Python Development
* Full-Stack Development

### GitHub

https://github.com/mahitech580

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

### Project

**AI Image Caption Generator**

Built with **Python + Flask + PyTorch + Hugging Face Transformers + BLIP + SQLite**.
