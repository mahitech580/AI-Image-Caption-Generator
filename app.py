import time
from pathlib import Path
from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename
from model.caption_model import CaptionModel
from database.database import initialize_database, save_caption, get_history, delete_caption
from utils.validators import is_allowed_file, is_valid_size
BASE_DIR = Path(__file__).resolve().parent
UPLOAD_FOLDER = BASE_DIR / "uploads"; UPLOAD_FOLDER.mkdir(exist_ok=True)
app = Flask(__name__); app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER; app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024
print("Loading AI caption model..."); caption_model = CaptionModel(); print(f"Model loaded successfully on: {caption_model.device}"); initialize_database()
@app.route("/")
def home(): return render_template("index.html")
@app.route("/api/health")
def health(): return jsonify(success=True, status="healthy", device=caption_model.device)
@app.route("/api/caption", methods=["POST"])
def generate_caption():
    if "image" not in request.files: return jsonify(success=False, error="No image was uploaded."), 400
    image = request.files["image"]
    if not image or image.filename == "": return jsonify(success=False, error="Please select an image."), 400
    if not is_allowed_file(image.filename): return jsonify(success=False, error="Unsupported file format. Use JPG, JPEG, PNG, or WEBP."), 400
    if not is_valid_size(image): return jsonify(success=False, error="File is too large. Maximum size is 10 MB."), 400
    original_filename = secure_filename(image.filename); saved_filename = f"{int(time.time()*1000)}_{original_filename}"; image_path = UPLOAD_FOLDER / saved_filename
    try:
        image.save(image_path); start_time = time.perf_counter(); caption = caption_model.generate_caption(str(image_path)); processing_time = round(time.perf_counter()-start_time, 2); save_caption(original_filename, caption, processing_time)
        return jsonify(success=True, filename=original_filename, caption=caption, processing_time=processing_time)
    except Exception as error:
        print("Caption generation error:", error); return jsonify(success=False, error="Unable to generate the caption."), 500
    finally:
        if image_path.exists():
            try: image_path.unlink()
            except OSError: pass
@app.route("/api/history")
def history():
    try: return jsonify(success=True, history=get_history())
    except Exception as error: print("History error:", error); return jsonify(success=False, error="Unable to load history."), 500
@app.route("/api/history/<int:caption_id>", methods=["DELETE"])
def remove_history(caption_id):
    try:
        if not delete_caption(caption_id): return jsonify(success=False, error="History item not found."), 404
        return jsonify(success=True, message="History item deleted.")
    except Exception as error: print("Delete error:", error); return jsonify(success=False, error="Unable to delete history item."), 500
@app.errorhandler(413)
def request_entity_too_large(error): return jsonify(success=False, error="File is too large. Maximum size is 10 MB."), 413
if __name__ == "__main__": app.run(host="127.0.0.1", port=5000, debug=True)
