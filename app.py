from flask import Flask, request, render_template
import os
from abe import encrypt, decrypt
from models import get_attributes, is_revoked
from config import UPLOAD_FOLDER

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        attrs = request.form["attributes"].split(",")

        content = file.read().decode()
        encrypted = encrypt(content, attrs)

        with open(os.path.join(UPLOAD_FOLDER, file.filename), "w") as f:
            f.write(encrypted)

        return "File Uploaded Securely"

    return render_template("upload.html")

@app.route("/download", methods=["GET", "POST"])
def download():
    if request.method == "POST":
        filename = request.form["filename"]
        username = request.form["username"]

        if is_revoked(username):
            return "User Access Revoked"

        user_attrs = get_attributes(username)

        with open(os.path.join(UPLOAD_FOLDER, filename), "r") as f:
            encrypted = f.read()

        decrypted = decrypt(encrypted, user_attrs)

        return f"Decrypted Content: {decrypted}"

    return render_template("download.html")

if __name__ == "__main__":
    app.run(debug=True)
