import fitz
from PIL import Image
import pytesseract
import io


def extract_resume_text(uploaded_file):
    text = ""
    try:
        # Try reading as PDF
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        for page in doc:
            page_text = page.get_text("text")
            text += page_text
            
            # If no text is found, do OCR on page image
            if not page_text.strip():
                pix = page.get_pixmap()
                img = Image.open(io.BytesIO(pix.tobytes("png")))
                text += pytesseract.image_to_string(img)
                
    except fitz.fitz.FileDataError:
        # If it's not a PDF, treat it as an image
        uploaded_file.seek(0)
        image = Image.open(uploaded_file)
        text = pytesseract.image_to_string(image)
    
    return text

def extract_skills_from_resume(resume_text):
    # Basic skill keywords (can be expanded)
    skills_db = [
    # CS/IT
    "Python","SQL","Machine Learning","Deep Learning","Java","C++","React","AWS","Cloud","Testing",
    # Pharma/Medical
    "Pharmacology","Drug Discovery","Clinical Trials","Medical Research","Biotechnology",
    "Pharmacy","Pharmacovigilance","Toxicology","Biochemistry","Molecular Biology",
    # Core Engineering
    "Electrical Engineering","Circuits","Power Systems","Mechanical Design","Civil Structures","Thermodynamics"
    ]

    found_skills = [s for s in skills_db if s.lower() in resume_text.lower()]
    return found_skills
