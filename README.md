# 📄 Multimodal Document Extraction Bot

A professional web application for intelligently extracting structured fields and raw text from uploaded documents (PDFs or images). Powered by OCR and NLP pipelines, this bot enables users to seamlessly upload and analyze documents via a sleek, responsive interface.

![Screenshot 2025-05-28 124136](https://github.com/user-attachments/assets/134a3152-ad65-4134-b0bf-6ffcdef8c9a9)
![Screenshot 2025-05-28 124148](https://github.com/user-attachments/assets/ad1424ad-01e4-44a1-a485-027ff759dcc2)

## 🚀 Features

- 📁 **Upload Support**: Drag-and-drop or browse for PDFs, JPG, PNG, TIFF (Max 16MB)
- 🔍 **Real-Time Processing**: Extract text and key-value pairs on-the-fly
- 🧠 **Multimodal Analysis**: Handles scanned documents and PDFs with both text and image data
- 📦 **File Storage**: Automatically saves all uploaded files securely
- 🎯 **Result Interface**: Clean UI with tabs for extracted fields and raw OCR text
- 📋 **Copy Feature**: Instantly copy raw text to clipboard

---

## 🖥️ Frontend Preview

<!-- Document Extractor Highlights -->
✔️ Drag-and-drop upload
✔️ Live progress bar
✔️ Two-tab result view (Fields + Raw Text)
✔️ Error alerts for unsupported file types/sizes

---

## 🛠️ Tech Stack
Component	Technology
Frontend	HTML, Bootstrap 5, FontAwesome
Backend	Flask (Python)
OCR Engine	Tesseract / PaddleOCR / PyMuPDF
NLP Extraction	spaCy / Transformers (optional)
Storage	Local filesystem

---

## 📂 Project Structure

Multimodal-Document-Extraction-Bot/
├── static/
│   └── styles.css           # Custom styles
├── templates/
│   └── index.html           # Main frontend
├── uploads/                 # Saved files
├── app.py                   # Main Flask app
├── extractor.py             # OCR + field extraction logic
├── requirements.txt
└── README.md

---

## ⚙️ Setup Instructions
1 Clone the repository
git clone https://github.com/YujiItaori/Multimodal-Document-Extraction-Bot.git
cd Multimodal-Document-Extraction-Bot

2 Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3 Install dependencies
pip install -r requirements.txt

4 Run the application
python app.py

5 Visit the app
Open your browser at: http://localhost:5000

---

## 📤 Usage Workflow
Launch the app and open the webpage.

Drag and drop or click to upload a document (PDF or image).

Wait for the document to process (progress bar will animate).

View extracted fields and raw text in the result tabs.

All uploaded files are automatically saved in the /uploads directory.

---

## 📌 Notes
Max upload file size: 16MB

Supported formats: PDF, JPG, JPEG, PNG, TIFF

Extraction quality may vary with image clarity

---

## 🧠 Future Enhancements
✅ Support Japanese and multilingual document extraction

✅ Named Entity Recognition (NER) tagging

⏳ Add document type classifier

⏳ Cloud storage and authentication support

---

## 🙌 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

---

## 📄 License
MIT License

---

## 👨‍💻 Author
Yash Vishwas
GitHub: @YujiItaori
LinkedIn: linkedin.com/in/yash-vishwas

Let me know if you'd like the README to include a GIF demo, API usage, or deployment instructions.
