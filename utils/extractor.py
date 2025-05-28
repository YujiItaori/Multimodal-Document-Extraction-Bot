import re
import spacy
from dateparser import parse as parse_date

nlp = spacy.load("en_core_web_sm")

def extract_fields(doc_type, text):
    fields = {}
    doc = nlp(text)
    
    if doc_type == "Invoice":
        # Improved date extraction
        dates = [ent.text for ent in doc.ents if ent.label_ == "DATE"]
        fields["Date"] = parse_date(dates[0]).strftime("%Y-%m-%d") if dates else "Not found"
        
        # Improved total amount extraction
        amounts = [ent.text for ent in doc.ents if ent.label_ == "MONEY"]
        fields["Total"] = amounts[-1] if amounts else "Not found"
        
        # Extract invoice number
        invoice_no = re.search(r'(invoice|inv)\.?\s*(no|number|#)?\s*[:]?\s*([A-Z0-9-]+)', text, re.I)
        fields["Invoice Number"] = invoice_no.group(3) if invoice_no else "Not found"

    elif doc_type == "Resume":
        # Improved name extraction using NER
        names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
        fields["Name"] = names[0] if names else "Not found"
        
        # Extract all emails and phones
        emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
        phones = re.findall(r'(\+?\d[\d\s-]{7,}\d)', text)
        fields["Email"] = emails[0] if emails else "Not found"
        fields["Phone"] = phones[0] if phones else "Not found"
        
        # Extract skills (simple version)
        skills = ["Python", "Java", "SQL", "Machine Learning"]  # Expand this list
        found_skills = [skill for skill in skills if skill.lower() in text.lower()]
        fields["Skills"] = ", ".join(found_skills) if found_skills else "Not found"

    elif doc_type == "ID Document":
        # Extract ID numbers
        id_numbers = re.findall(r'[A-Z0-9]{6,}', text)
        fields["ID Number"] = id_numbers[0] if id_numbers else "Not found"
        
        # Extract expiration date
        dates = [ent.text for ent in doc.ents if ent.label_ == "DATE"]
        if len(dates) > 1:
            fields["Expiration Date"] = parse_date(dates[1]).strftime("%Y-%m-%d")

    else:
        fields["Raw Text"] = text[:500]
    
    return fields