from docx import Document
import os

def handle_office_metadata(file_path):
    try:
        ext = os.path.splitext(file_path)[1].lower()
        if ext == ".docx":
            doc = Document(file_path)
            core_props = doc.core_properties
            core_props.author = None
            core_props.last_modified_by = None
            core_props.title = None
            doc.save(file_path)
    except Exception as e:
        raise Exception(f"Office metadata removal failed: {e}")
