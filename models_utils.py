import docx2txt
import textract
import os
import tempfile

def extract_text(uploaded_file):
    try:
        # Save uploaded file to a temporary file
        suffix = os.path.splitext(uploaded_file.name)[-1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        if uploaded_file.name.endswith('.pdf'):
            text = textract.process(tmp_path).decode('utf-8')
        elif uploaded_file.name.endswith('.docx'):
            text = docx2txt.process(tmp_path)
        elif uploaded_file.name.endswith('.txt'):
            with open(tmp_path, "r", encoding="utf-8") as f:
                text = f.read()
        else:
            text = ""

        os.remove(tmp_path)  # Clean up
        return text.strip()
    except Exception as e:
        print(f"Error during text extraction: {e}")
        return ""
