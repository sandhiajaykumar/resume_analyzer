import PyPDF2
import re

def extract_text_from_pdf(uploaded_file):
    try:
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        
        # Basic parsing using regular expressions
        name_match = re.search(r"([A-Z][a-z]+)\s+([A-Z][a-z]+)", text)
        email_match = re.search(r"[\w\.-]+@[\w\.-]+", text)
        skills_match = re.search(r"Skills\s*([\s\S]*)", text, re.IGNORECASE)

        resume_data = {
            "name": f"{name_match.group(1)} {name_match.group(2)}" if name_match else "Unknown",
            "email": email_match.group(0) if email_match else "Unknown",
            "skills": skills_match.group(1).strip().split('\n') if skills_match else []
        }
        
        return resume_data
    except Exception as e:
        return {"error": str(e)}
