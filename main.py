import tkinter as tk
from tkinter import filedialog, messagebox
from ui.app_gui import MetadataCleanerApp

def main():
    root = tk.Tk()
    app = MetadataCleanerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
