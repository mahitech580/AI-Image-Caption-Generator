from pathlib import Path
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
MAX_FILE_SIZE = 10 * 1024 * 1024
def is_allowed_file(filename): return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS
def is_valid_size(file):
    file.seek(0, 2); size = file.tell(); file.seek(0); return size <= MAX_FILE_SIZE
