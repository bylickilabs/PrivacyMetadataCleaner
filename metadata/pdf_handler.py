import pikepdf

def handle_pdf_metadata(file_path):
    try:
        pdf = pikepdf.Pdf.open(file_path)
        pdf.docinfo.clear()
        pdf.save(file_path)
        pdf.close()
    except Exception as e:
        raise Exception(f"PDF metadata removal failed: {e}")
