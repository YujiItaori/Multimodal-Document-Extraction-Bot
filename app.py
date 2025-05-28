# app.py improvements
from flask import Flask, render_template, request, jsonify
import os
from utils.ocr import perform_ocr
from utils.classifier import classify_document
from utils.extractor import extract_fields
from werkzeug.utils import secure_filename
import uuid
import time

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf', 'tiff'}
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Create upload folder if not exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def generate_unique_filename(filename):
    ext = filename.rsplit('.', 1)[1].lower()
    unique_id = uuid.uuid4().hex
    timestamp = int(time.time())
    return f"{timestamp}_{unique_id}.{ext}"

def clean_text_for_display(text):
    """Clean and format text for better display"""
    if not text:
        return "No text extracted from the document."
    
    # Remove excessive whitespace while preserving structure
    lines = text.split('\n')
    cleaned_lines = []
    
    for line in lines:
        line = line.strip()
        if line:  # Only add non-empty lines
            cleaned_lines.append(line)
    
    # Join lines with proper spacing
    cleaned_text = '\n'.join(cleaned_lines)
    
    # Limit text length for display (optional)
    if len(cleaned_text) > 5000:
        cleaned_text = cleaned_text[:5000] + "\n\n... (text truncated for display)"
    
    return cleaned_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        if 'document' not in request.files:
            return jsonify({"error": "No file part"}), 400
        
        file = request.files['document']
        
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        
        if not file or not allowed_file(file.filename):
            return jsonify({"error": "File type not allowed. Please upload PDF, JPG, PNG, or TIFF files."}), 400
        
        # Generate unique filename to prevent collisions
        filename = generate_unique_filename(secure_filename(file.filename))
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            # Processing pipeline with error handling
            print(f"Processing file: {filepath}")
            
            # Perform OCR
            extracted_text = perform_ocr(filepath)
            if not extracted_text or not extracted_text.strip():
                return jsonify({"error": "OCR failed to extract text from the document. Please ensure the document contains readable text."}), 400
            
            print(f"Extracted text length: {len(extracted_text)}")
            
            # Classify document
            doc_type = classify_document(extracted_text)
            print(f"Document classified as: {doc_type}")
            
            # Extract fields
            fields = extract_fields(doc_type, extracted_text)
            print(f"Extracted fields: {fields}")
            
            # Clean text for display
            cleaned_text = clean_text_for_display(extracted_text)

            # Return results including the extracted text
            return jsonify({
                "success": True,
                "doc_type": doc_type,
                "fields": fields,
                "extracted_text": cleaned_text
            })
        
        except Exception as processing_error:
            print(f"Processing error: {str(processing_error)}")
            return jsonify({"error": f"Error processing document: {str(processing_error)}"}), 500
        
        finally:
            # Clean up - remove processed file
            try:
                if os.path.exists(filepath):
                    os.remove(filepath)
                    print(f"Cleaned up file: {filepath}")
            except Exception as cleanup_error:
                print(f"Cleanup error: {str(cleanup_error)}")
    
    except Exception as e:
        print(f"Upload error: {str(e)}")
        return jsonify({"error": f"Upload failed: {str(e)}"}), 500

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "Document Extractor API is running"})

@app.errorhandler(413)
def too_large(e):
    return jsonify({"error": "File too large. Maximum size is 16MB."}), 413

@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal server error occurred."}), 500

if __name__ == '__main__':
    print("Starting Document Extractor Flask App...")
    print(f"Upload folder: {UPLOAD_FOLDER}")
    print(f"Max file size: {MAX_FILE_SIZE / (1024*1024)}MB")
    print(f"Allowed extensions: {ALLOWED_EXTENSIONS}")
    app.run(debug=True, host='0.0.0.0', port=5000)