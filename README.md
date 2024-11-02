# ImagetoInsight

*ImagetoInsight* is designed to make text extraction and summarization effortless. By simply taking a photo of a document, article, or any text-heavy image, users can instantly receive a concise, easy-to-read summary. Leveraging advanced OCR (Optical Character Recognition) and natural language processing, ImagetoInsight accurately extracts text from images, identifies key points, and delivers summaries that are ideal for quick understanding. It's perfect for students, professionals, or anyone looking to save time on reading long documents.

---

## Setup Guide

### 1. Prerequisites

**For Linux:**  
To enable OCR capabilities, install Tesseract OCR:

```bash
sudo apt update
sudo apt install tesseract-ocr
```

### 2. Python Environment Setup

1. **Create a Virtual Environment (recommended)**  
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

2. **Install Python Libraries**  
   You’ll need `pytesseract` and `pillow` for image processing, and other dependencies for summarization.

   ```bash
   pip install pytesseract pillow
   ```

3. **Install Additional Requirements**  
   If you have a `requirements.txt` file, you can install all necessary libraries at once:

   ```bash
   pip install -r requirements.txt
   ```

With these installed, *ImagetoInsight* will be fully set up and ready to extract text and summarize documents from images, *It really sucks when it comes to understanding doctors handwriting*🫣
