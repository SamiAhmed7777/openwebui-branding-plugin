# branding_api.py
# Backend API for managing branding assets

from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.getenv("BRANDING_UPLOAD_FOLDER", "static")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/api/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files["file"]
    filename = request.form.get("filename", file.filename)
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    return jsonify({"message": "File uploaded successfully", "filename": filename})

@app.route("/api/branding/<filename>", methods=["GET"])
def get_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route("/api/config", methods=["GET"])
def get_config():
    config_path = os.path.join(UPLOAD_FOLDER, "config.json")
    if os.path.exists(config_path):
        with open(config_path, "r") as config_file:
            return jsonify(json.load(config_file))
    return jsonify({"error": "Config file not found"}), 404

@app.route("/api/config", methods=["POST"])
def update_config():
    config_data = request.json
    config_path = os.path.join(UPLOAD_FOLDER, "config.json")
    with open(config_path, "w") as config_file:
        json.dump(config_data, config_file, indent=4)
    return jsonify({"message": "Configuration updated successfully"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
