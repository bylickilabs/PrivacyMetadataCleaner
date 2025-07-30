from PIL import Image
import piexif

def handle_image_metadata(file_path):
    try:
        piexif.remove(file_path)
    except Exception as e:
        raise Exception(f"EXIF removal failed: {e}")
