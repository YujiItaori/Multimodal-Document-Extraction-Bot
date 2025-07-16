# 📄 Multimodal Document Extraction Bot

A professional web application for intelligently extracting structured fields and raw text from uploaded documents (PDFs or images). Powered by OCR and NLP pipelines, this bot enables users to seamlessly upload and analyze documents via a sleek, responsive interface.

## 🚀 Features

- 📁 **Upload Support**: Drag-and-drop or browse for PDFs, JPG, PNG, TIFF (Max 16MB)
- 🔍 **Real-Time Processing**: Extract text and key-value pairs on-the-fly
- 🧠 **Multimodal Analysis**: Handles scanned documents and PDFs with both text and image data
- 📦 **File Storage**: Automatically saves all uploaded files securely
- 🎯 **Result Interface**: Clean UI with tabs for extracted fields and raw OCR text
- 📋 **Copy Feature**: Instantly copy raw text to clipboard

## 🖥️ Frontend Preview

**Document Extractor Highlights:**
- ✔️ Drag-and-drop upload
- ✔️ Live progress bar
- ✔️ Two-tab result view (Fields + Raw Text)
- ✔️ Error alerts for unsupported file types/sizes

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | HTML, Bootstrap 5, FontAwesome |
| **Backend** | Flask (Python) |
| **OCR Engine** | Tesseract / PaddleOCR / PyMuPDF |
| **NLP Extraction** | spaCy / Transformers (optional) |
| **Storage** | Local filesystem |

## 📂 Project Structure

```
Multimodal-Document-Extraction-Bot/
├── static/
│   └── styles.css           # Custom styles
├── templates/
│   └── index.html           # Main frontend
├── uploads/                 # Saved files directory
├── app.py                   # Main Flask application
├── extractor.py             # OCR + field extraction logic
├── requirements.txt         # Python dependencies
└── README.md               # Project documentation
```

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/YujiItaori/Multimodal-Document-Extraction-Bot.git
cd Multimodal-Document-Extraction-Bot
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```

### 5. Visit the app
Open your browser at: `http://localhost:5000`

## 📤 Usage Workflow

1. **Launch the app** and open the webpage
2. **Drag and drop** or click to upload a document (PDF or image)
3. **Wait for processing** - progress bar will animate during extraction
4. **View results** in the extracted fields and raw text tabs
5. **Access files** - all uploaded files are automatically saved in the `/uploads` directory

## 📌 Technical Notes

- **Max upload file size**: 16MB
- **Supported formats**: PDF, JPG, JPEG, PNG, TIFF
- **Extraction quality**: May vary with image clarity and document structure
- **Processing time**: Depends on document size and complexity

## 🧠 Future Enhancements

- ✅ **Multilingual Support**: Japanese and other language document extraction
- ✅ **Named Entity Recognition (NER)**: Advanced entity tagging
- ⏳ **Document Classifier**: Automatic document type detection
- ⏳ **Cloud Integration**: Cloud storage and authentication support
- ⏳ **API Endpoints**: RESTful API for programmatic access
- ⏳ **Batch Processing**: Multiple document processing capability

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🛡️ Privacy & Security

- **Local Processing**: All document processing is done locally
- **File Storage**: Uploaded files are stored securely in the local filesystem
- **No External Transmission**: Documents are not sent to external services
- **Data Protection**: No personal data is transmitted or stored remotely

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Yash Vishwas**
- GitHub: [@YujiItaori](https://github.com/YujiItaori)
- LinkedIn: [linkedin.com/in/yash-vishwas](https://linkedin.com/in/yash-vishwas)

## 🙏 Acknowledgments

- Thanks to the open-source OCR and NLP communities
- Special thanks to contributors and testers
- Inspired by the need for accessible document processing tools

---

⭐ **Star this repository if you find it helpful!** ⭐

*"Information is not knowledge. Knowledge is not wisdom. Wisdom is not truth." - Frank Zappa*

---

*Let me know if you'd like the README to include a GIF demo, API usage, or deployment instructions.*

![Screenshot 2025-05-28 124136](https://github.com/user-attachments/assets/134a3152-ad65-4134-b0bf-6ffcdef8c9a9)
![Screenshot 2025-05-28 124148](https://github.com/user-attachments/assets/ad1424ad-01e4-44a1-a485-027ff759dcc2)
