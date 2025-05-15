import sys
import os
import base64
import socket
import webbrowser
import tkinter as tk
from tkinter import filedialog
from flask import Flask, render_template

app = Flask(__name__)

IMAGE_FOLDER = None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        IMAGE_FOLDER = sys.argv[1]
    else:
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        IMAGE_FOLDER = filedialog.askdirectory(title="Choose a folder…")
        if not IMAGE_FOLDER:
            sys.exit("No folder chosen, exit.")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/result")
def result():
    if not IMAGE_FOLDER:
        return "No folder specified. Start with: python app.py /path/to/folder", 400

    # List all files in the specified folder
    files = sorted(os.listdir(IMAGE_FOLDER))
    images = []
    for fname in files:
        if fname.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')):
            path = os.path.join(IMAGE_FOLDER, fname)
            with open(path, "rb") as img:
                b64 = base64.b64encode(img.read()).decode('utf-8')
            # Save both the base64 string and the file extension
            images.append({
                'name': fname,
                'data': b64,
                'ext': fname.rsplit('.', 1)[1].lower()
            })

    return render_template("result.html", images=images)

if __name__ == "__main__":
    # Find a free port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    port = s.getsockname()[1]
    s.close()

    # Open the default web browser
    webbrowser.open(f"http://127.0.0.1:{port}")

    # Start the Flask server
    app.run(host="0.0.0.0", port=port, use_reloader=False)