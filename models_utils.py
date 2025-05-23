import docx2txt
import textract
import re

def extract_text(uploaded_file):
    try:
        if uploaded_file.name.endswith('.pdf'):
            text = textract.process(uploaded_file, extension='pdf').decode('utf-8')
        elif uploaded_file.name.endswith('.docx'):
            text = docx2txt.process(uploaded_file)
        elif uploaded_file.name.endswith('.txt'):
            text = uploaded_file.read().decode('utf-8')
        else:
            return ""
        return text
    except:
        return ""

def extract_skills(text):
    skill_keywords = ["python", "django", "html", "css", "aws", "mysql", "bootstrap", "javascript", "rest api"]
    text = text.lower()
    skills_found = [skill for skill in skill_keywords if skill in text]
    return skills_found
if __name__ == "__main__":
    train_and_save_model()
