import tkinter as tk
from tkinter import filedialog, messagebox
from metadata.exif_handler import handle_image_metadata
from metadata.pdf_handler import handle_pdf_metadata
from metadata.office_handler import handle_office_metadata
import os

class MetadataCleanerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Privacy Metadata Cleaner")
        self.root.geometry("500x300")

        self.label = tk.Label(root, text="Select a file to clean:")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Browse", command=self.browse_file)
        self.select_button.pack()

        self.status = tk.Label(root, text="", fg="blue")
        self.status.pack(pady=20)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if not file_path:
            return

        ext = os.path.splitext(file_path)[1].lower()
        try:
            if ext in ['.jpg', '.jpeg', '.png']:
                handle_image_metadata(file_path)
            elif ext == '.pdf':
                handle_pdf_metadata(file_path)
            elif ext in ['.docx', '.xlsx', '.pptx']:
                handle_office_metadata(file_path)
            else:
                messagebox.showwarning("Unsupported", f"File type {ext} is not supported.")
                return
            self.status.config(text="Metadata cleaned successfully!", fg="green")
        except Exception as e:
            self.status.config(text=f"Error: {str(e)}", fg="red")
