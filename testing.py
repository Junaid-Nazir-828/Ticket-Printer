from docx import Document

# Load the existing docx file
doc = Document("Format v2\\ticket version 71.docx")

# Iterate through all the paragraphs in the document
for paragraph in doc.paragraphs:
    for run in paragraph.runs:
        # Check if the run contains a textbox
        if run._r.xml.startswith('<w:object '):
            # Iterate through the runs inside the textbox
            for textbox_run in run._r:
                if textbox_run.xml.startswith('<w:t>'):
                    # Replace text within the textbox
                    textbox_run.text = textbox_run.text.replace('DATE', '12.12.2012')


# Save the modified document
doc.save("Edited Docx v2\\edited_document.docx")